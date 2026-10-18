#!/usr/bin/env python3
"""Independent exhaustive finite checks for fair orientations of Cayley trees.

Run: python verify_oriented_trees.py
Standard library only. Finite checks support but do not prove the general theorem.
"""
from itertools import product
from fractions import Fraction
from math import isclose, exp, sqrt


def decode_prufer(seq, n):
    degree = [1] * n
    for v in seq:
        degree[v] += 1
    edges = []
    for v in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    remains = [i for i, d in enumerate(degree) if d == 1]
    assert len(remains) == 2
    edges.append((remains[0], remains[1]))
    return edges


def moments(n):
    s_total = t_total = ss_total = st_total = 0
    cases = 0
    for seq in product(range(n), repeat=n - 2):
        edges = decode_prufer(seq, n)
        for mask in range(1 << (n - 1)):
            incoming = [0] * n
            outgoing = [0] * n
            for j, (a, b) in enumerate(edges):
                if (mask >> j) & 1:
                    a, b = b, a
                outgoing[a] += 1
                incoming[b] += 1
            s = incoming.count(0)
            t = outgoing.count(0)
            s_total += s
            t_total += t
            ss_total += s * s
            st_total += s * t
            cases += 1
    return (Fraction(s_total, cases), Fraction(t_total, cases),
            Fraction(ss_total, cases), Fraction(st_total, cases), cases)


def analytic_moments(n):
    x = (1 - Fraction(1, 2 * n)) ** (n - 2)
    y = (1 - Fraction(1, n)) ** (n - 2)
    es = Fraction(n, 2) * x
    ess = es + Fraction(n * (n - 2), 4) * y
    est = Fraction(n * n, 4) * y
    return es, es, ess, est


def path_cov(n):
    if n == 2:
        return Fraction(0)
    d = [1] + [2] * (n - 2) + [1]
    x = [Fraction(1, 2 ** z) for z in d]
    return -sum(z*z for z in x) + 2*sum(x[i]*x[i+1] for i in range(n-1))


def orientation_cov_fixed(edges, n):
    total_s = total_t = total_st = 0
    ways = 1 << (n-1)
    for mask in range(ways):
        indeg = [0]*n; outdeg=[0]*n
        for j,(a,b) in enumerate(edges):
            if (mask>>j)&1: a,b=b,a
            indeg[b]+=1;outdeg[a]+=1
        s=indeg.count(0);t=outdeg.count(0)
        total_s+=s;total_t+=t;total_st+=s*t
    return Fraction(total_st,ways)-Fraction(total_s*total_t,ways*ways)


def weighted_edge_identity(n, weights):
    total=edge=0
    for seq in product(range(n), repeat=n-2):
        w=1
        for v in seq: w*=weights[v]
        total+=w
        if (0,1) in [tuple(sorted(x)) for x in decode_prufer(seq,n)]:
            edge+=w
    return Fraction(edge,total) == Fraction(weights[0]+weights[1],sum(weights))


def main():
    tests=0
    for n in range(2,8):
        es,et,ess,est,count=moments(n)
        expected=analytic_moments(n)
        assert (es,et,ess,est)==expected,(n,es,et,ess,est,expected)
        tests+=4
        cov=est-es*et
        assert cov==(Fraction(n*n,4)*((1-Fraction(1,n))**(n-2)
                        -(1-Fraction(1,2*n))**(2*n-4)))
        assert (cov==0 if n==2 else cov<0)
        tests+=2
        print('n=',n, 'Cayley trees=', n**(n-2), 'oriented trees=',count,
              'mean=',es, 'cov=',cov, 'var=',ess-es*es)
    for n in range(2,12):
        edges=[(i,i+1) for i in range(n-1)]
        assert path_cov(n)==orientation_cov_fixed(edges,n)
        tests+=1
        if n>=3:
            assert path_cov(n)==Fraction(n-4,16)
            tests+=1
    for n in range(3,7):
        for weights in ([1]*n,[1,2]+[3]*(n-2),[2,5]+[1]*(n-2)):
            assert weighted_edge_identity(n,weights)
            tests+=1
    rho_limit=-1/(8*sqrt(exp(1))-9)
    for n in (1000,10000,100000):
        # Decimal prevents severe relative cancellation for large n.
        from decimal import Decimal, getcontext
        getcontext().prec=45
        N=Decimal(n)
        x=(Decimal(1)-1/(2*N))**(n-2)
        y=(Decimal(1)-1/N)**(n-2)
        mu=N*x/2
        var=mu+N*(N-2)*y/4-mu*mu
        cov=N*N*(y-x*x)/4
        rho=float(cov/var)
        assert abs(rho-rho_limit)<(16/n)
        tests+=1
    print('VERIFIED:',tests,'independent exact/symbolic/asymptotic checks')

if __name__=='__main__':main()
