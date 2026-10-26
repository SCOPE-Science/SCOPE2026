#!/usr/bin/env python3
"""Exact verification of edge correlations in uniform forests of K_{3,n}.

Uses only Python's standard library.  Does not use simulation.
"""
from fractions import Fraction


def totals(n):
    z = 3*n*n + 13*n + 16
    a = 3*n*n + 23*n + 38
    r = 2*n + 6
    ell = 3*n*n + 33*n + 66
    d = 3*n*n + 33*n + 82
    factor = lambda e: Fraction(4)**e
    return tuple(int(factor(n-k)*v) for k,v in
                 [(2,z),(3,a),(2,r),(4,ell),(4,d)])


def predicted(n):
    z = 3*n*n + 13*n + 16
    a = 3*n*n + 23*n + 38
    p = Fraction(a,4*z)
    joint = (Fraction(2*n+6,z),
             Fraction(3*n*n+33*n+66,16*z),
             Fraction(3*n*n+33*n+82,16*z))
    cov = tuple(x-p*p for x in joint)
    explicit = (
        -Fraction((n-1)*(9*n**3+51*n*n+104*n+92),16*z*z),
        -Fraction(41*n*n+181*n+194,8*z*z),
        -Fraction(17*n*n+77*n+66,8*z*z),
    )
    assert cov == explicit
    assert all(x < 0 for x in cov)
    return p,joint,cov


def brute(n):
    """Exhaustive subsets of the labeled edges (i,j), indexed by 3*j+i."""
    edges = [(i,3+j) for j in range(n) for i in range(3)]
    out = [0,0,0,0,0]
    for bits in range(1<<(3*n)):
        parent = list(range(n+3))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        acyclic = True
        for k,(a,b) in enumerate(edges):
            if bits & (1<<k):
                x,y = root(a),root(b)
                if x==y:
                    acyclic=False
                    break
                parent[x] = y
        if not acyclic:
            continue
        out[0]+=1
        if bits&1:
            out[1]+=1
            if bits&2:out[2]+=1
            if n>1:
                if bits&(1<<3):out[3]+=1
                if bits&(1<<4):out[4]+=1
    return tuple(out)


def poly_multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def poly_subtract(a,b):
    m=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
            for i in range(m)]


def symbolic():
    z=[16,13,3]
    a=[38,23,3]
    cs=[[96,32],[66,33,3],[82,33,3]]
    exacts=[[92,12,-53,-42,-9],
            [-388,-362,-82],
            [-132,-154,-34]]
    for c,expected in zip(cs,exacts):
        diff=poly_subtract(poly_multiply(z,c),poly_multiply(a,a))
        while diff and diff[-1]==0:diff.pop()
        assert diff==expected, (diff,expected)


def main():
    assertions=0
    symbolic(); assertions+=3
    for n in range(2,7):
        observed=brute(n)
        required=totals(n)
        assert observed==required,(n,observed,required)
        assertions+=5
        den=observed[0]
        pp, joint,cov=predicted(n)
        assert Fraction(observed[1],den)==pp; assertions+=1
        for k in range(3):
            assert Fraction(observed[k+2],den)==joint[k]
            assert Fraction(observed[k+2],den)-pp*pp==cov[k]
            assertions+=2
    for n in range(2,2001):
        predicted(n); assertions+=4
    print('VERIFICATION_OK', 'exact_comparisons=',assertions,
          'enumerated_n=2..6', 'algebraic_n=2..2000')

if __name__ == '__main__': main()
