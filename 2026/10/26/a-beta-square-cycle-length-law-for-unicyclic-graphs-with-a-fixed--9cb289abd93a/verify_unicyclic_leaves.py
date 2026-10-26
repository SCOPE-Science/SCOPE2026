"""Exact independent checks for labelled connected unicyclic graph leaf/cycle laws.
No external packages. Python 3.10+; run: python verify_unicyclic_leaves.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def count_by_surjections(n, k, ell):
    """Cycle+forest rooted-map count via inclusion-exclusion, integer."""
    s = n-k
    if not (3 <= k <= n-ell and 1 <= ell <= s):
        return 0
    a = comb(s,ell)*sum((-1)**j*comb(s-ell,j)*(n-ell-j)**(s-1)
                        for j in range(s-ell+1))
    numer = factorial(n)*a
    assert numer%(2*factorial(s))==0
    return numer//(2*factorial(s))


def poly_mul(a, b, degree):
    c=[Fraction(0)]*(degree+1)
    for i, x in enumerate(a):
        if i>degree: break
        for j,y in enumerate(b):
            if i+j>degree: break
            c[i+j]+=x*y
    return c


def count_by_coefficient(n,k,ell):
    """Independent exponential-coefficient evaluation over exact fractions."""
    s=n-k
    if not (3<=k<=n-ell and 1<=ell<=s): return 0
    d=ell-1
    series=[Fraction(k**j, factorial(j)) for j in range(d+1)]
    f=[Fraction(1, factorial(j+1)) for j in range(d+1)]
    for _ in range(s-ell):
        series=poly_mul(series,f,d)
    value=Fraction(factorial(n)*factorial(s-1), 2*factorial(s-ell)*factorial(ell))*series[d]
    assert value.denominator==1
    return value.numerator


def count_bruteforce(n):
    """Enumerate n-edge simple labelled graphs and independently test connectivity/cycle."""
    edges=list(combinations(range(n),2))
    out=Counter()
    for picks in combinations(range(len(edges)),n):
        deg=[0]*n
        adj=[[] for _ in range(n)]
        for p in picks:
            u,v=edges[p]
            deg[u]+=1;deg[v]+=1
            adj[u].append(v);adj[v].append(u)
        seen={0}; stack=[0]
        while stack:
            for u in adj[stack.pop()]:
                if u not in seen:
                    seen.add(u);stack.append(u)
        if len(seen)!=n: continue
        leaf=sum(d==1 for d in deg)
        cur=deg[:]; stack=[i for i,d in enumerate(cur) if d==1]
        while stack:
            v=stack.pop()
            if cur[v]!=1:continue
            cur[v]=0
            for u in adj[v]:
                if cur[u]>1:
                    cur[u]-=1
                    if cur[u]==1:stack.append(u)
        cyc=sum(d>0 for d in cur)
        assert 3<=cyc<=n
        out[(cyc,leaf)]+=1
    return out


def run():
    nchecks=0
    graphchecks=0
    for n in range(4,17):
        for k in range(3,n):
            for ell in range(1,n-k+1):
                a=count_by_surjections(n,k,ell)
                b=count_by_coefficient(n,k,ell)
                assert a==b, (n,k,ell,a,b)
                if ell==1: assert a==factorial(n)//2
                if ell==2:
                    s=n-k
                    assert a==factorial(n)*(s-1)*(2*n-s-2)//8
                nchecks+=1
    for n in range(4,8):
        direct=count_bruteforce(n)
        for k in range(3,n+1):
            for ell in range(0,n-k+1):
                expected= 1 if ell==0 and k==n else count_by_surjections(n,k,ell)
                # pure labelled n-cycle: (n-1)!/2
                if ell==0 and k==n: expected=factorial(n-1)//2
                assert direct[(k,ell)]==expected, (n,k,ell,direct[(k,ell)],expected)
                graphchecks+=1
    print(f'PASS: {nchecks} exact formula/closed-case checks, {graphchecks} independent raw graph-enumeration checks (n=4..7).')

if __name__=='__main__':
    run()
