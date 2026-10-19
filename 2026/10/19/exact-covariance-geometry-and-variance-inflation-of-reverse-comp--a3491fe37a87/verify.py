#!/usr/bin/env python3
"""Independent, finite checks of perfect reverse-complementary-stem moments.

No external dependencies. Position pairs are zero-based internally.
"""
from fractions import Fraction
from itertools import combinations, product


def b(r):
    return r*(r-1)//2 if r >= 2 else 0


def candidates(n,m,g):
    return [(i,j) for i in range(max(0,n-m+1))
            for j in range(i+m+g,n-m+1)]


def moments(q,n,m,g):
    N=b(n-2*m-g+2)
    E=Fraction(N,q**m)
    V=E*(1-Fraction(1,q**m))
    for d in range(1,m):
        V+=2*b(n-2*m-g-2*d+2)*(Fraction(1,q**(m+d))-Fraction(1,q**(2*m)))
    return E,V


def stems(w,m,g):
    ans=0
    for i,j in candidates(len(w),m,g):
        if all(w[i+r]==(w[j+m-1-r]^1) for r in range(m)):
            ans+=1
    return ans


def brute_moments(q,n,m,g):
    S=S2=0
    for w in product(range(q),repeat=n):
        h=stems(w,m,g)
        S+=h
        S2+=h*h
    E=Fraction(S,q**n)
    return E,Fraction(S2,q**n)-E*E


def rank_two(e,f,m):
    """Return number of independent complement equations (GF2 parity union)."""
    parent={};par={}
    def root(x):
        if x not in parent:
            parent[x]=x;par[x]=0
        if parent[x]!=x:
            y=parent[x]; rr=root(y);par[x]^=par[y];parent[x]=rr
        return parent[x]
    for i,j in (e,f):
        for r in range(m):
            x,y=i+r,j+m-1-r
            a,bb=root(x),root(y)
            if a==bb:
                assert par[x]^par[y]==1, 'inconsistent parity constraint'
            else:
                parent[a]=bb;par[a]=par[x]^par[y]^1
    return len(parent)-len({root(x) for x in parent})


def main():
    tested=0
    for q,max_n in ((2,11),(4,7)):
        for n in range(max_n+1):
            for m in range(1,min(n,4)+1):
                for g in range(4):
                    assert brute_moments(q,n,m,g)==moments(q,n,m,g),(q,n,m,g)
                    tested+=1
    print('Exact rational moment enumerations passed:',tested)

    checked=0
    for m in range(1,7):
        for n in range(2*m,23):
            for g in (0,1,2,4):
                ev=candidates(n,m,g)
                if len(ev)>180:
                    continue
                for e,f in combinations(ev,2):
                    d=abs(e[0]-f[0]);same_center=e[0]+e[1]==f[0]+f[1]
                    expected=2*m-(max(0,m-d) if same_center else 0)
                    actual=rank_two(e,f,m)
                    assert actual==expected,(n,m,g,e,f,expected,actual)
                    checked+=1
    print('Exact joint-constraint rank comparisons passed:',checked)
    print('ALL FINITE CHECKS PASSED (general theorem uses the proof in RESULT.md)')

if __name__=='__main__':
    main()
