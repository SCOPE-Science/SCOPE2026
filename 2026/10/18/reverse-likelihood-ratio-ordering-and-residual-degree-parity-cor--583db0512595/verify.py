"""Exact finite checks for the parity-class/root-degree law in uniform labeled trees.

Uses only the Python standard library. Independent Prufer-code enumeration tests the
closed-form joint counts. Finite tests do not prove the infinite asymptotic assertions.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, lgamma, log, sqrt


def parity_class_and_degree(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = [[] for _ in range(n)]
    for v in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges[v].append(leaf)
        edges[leaf].append(v)
        degree[v] -= 1
        degree[leaf] -= 1
    a, b = [i for i in range(n) if degree[i] == 1]
    edges[a].append(b)
    edges[b].append(a)
    colors = [-1] * n
    colors[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for w in edges[v]:
            if colors[w] == -1:
                colors[w] = 1 - colors[v]
                stack.append(w)
    return colors.count(0), len(edges[0])


def count(n, k, d):
    m = n-k
    if not (1 <= k < n and 1 <= d <= m):
        return 0
    return comb(n-1,k-1) * m**(k-1) * comb(m-1,d-1) * (k-1)**(m-d)


def marginal(n,k):
    return sum(count(n,k,d) for d in range(1,n))


def exact_finite_checks():
    tests = 0
    for n in range(2,9):
        empirical=Counter(parity_class_and_degree(code,n)
                          for code in product(range(n),repeat=n-2))
        assert sum(empirical.values()) == n**(n-2); tests+=1
        for k in range(1,n):
            m=n-k
            assert marginal(n,k)==comb(n-1,k-1)*k**(m-1)*m**(k-1);tests+=1
            for d in range(1,n):
                assert empirical[k,d]==count(n,k,d),(n,k,d);tests+=1
        assert sum(k*d*v for (k,d),v in empirical.items()) == (n-1)*n**(n-2)
        tests += 1
        print('Prufer enumeration n=%d: %d trees' % (n,n**(n-2)))
    for n in range(2,23):
        total=n**(n-2)
        assert sum(marginal(n,k) for k in range(1,n))==total;tests+=1
        p={k:Fraction(marginal(n,k),total) for k in range(1,n)}
        q={k:p[k]*Fraction(n,2*k) for k in p}
        assert sum(q.values())==1;tests+=1
        assert all(q[k]==q[n-k] for k in q);tests+=len(q)
        eb=sum(k*p[k] for k in p)
        equad=sum(k*k*p[k] for k in p)
        vq=sum((k-Fraction(n,2))**2*q[k] for k in q)
        vp=equad-eb**2
        assert eb==Fraction(n,2)+Fraction(2,n)*vq;tests+=1
        assert vp==vq-Fraction(4,n*n)*vq**2;tests+=1
        ed=Fraction(2*(n-1),n)
        cov=Fraction(n-1,1)-eb*ed
        assert cov== -Fraction(4*(n-1),n*n)*vq;tests+=1
        if n>=3:assert cov<0;tests+=1
        for k in range(1,n):
            for ell in range(k+1,n):
                for d in range(1,n):
                    for e in range(d+1,n):
                        # Reverse total positivity of order two.
                        assert count(n,k,d)*count(n,ell,e)<=count(n,k,e)*count(n,ell,d),(n,k,ell,d,e)
                        tests+=1
    print('exact checks:',tests)
    return tests


def numeric_asymptotics():
    tests=0
    for n in (100,500,1000):
        lps=[]
        for k in range(1,n):
            m=n-k
            lps.append(lgamma(n)-lgamma(k)-lgamma(n-k+1)
                       +(m-1)*log(k)+(k-1)*log(m)-(n-2)*log(n))
        ps=[exp(t) for t in lps]
        z=sum(ps)
        ps=[p/z for p in ps]
        mean=sum(k*p for k,p in enumerate(ps,1))
        variance=sum((k-mean)**2*p for k,p in enumerate(ps,1))
        covariance=(n-1)*(1-2*mean/n)
        var_degree=(n-1)*(n-2)/(n*n)
        scale_corr=sqrt(n)*covariance/sqrt(variance*var_degree)
        assert abs(covariance+0.25)<0.004;tests+=1
        assert abs(variance/n-1/16)<0.0001;tests+=1
        assert abs(scale_corr+1)<0.01;tests+=1
        print('n=%d: covariance=%.9f, var(B)/n=%.9f, sqrt(n)*corr=%.9f' %
              (n,covariance,variance/n,scale_corr))
    return tests


if __name__=='__main__':
    a=exact_finite_checks()
    b=numeric_asymptotics()
    print('PASS:',a+b,'assertions')
