"""Exact verification of three-point degree-tail crossings for uniform labelled trees.

Run: python3 research32_threepoint_verify.py
Uses Python standard library and rational arithmetic throughout.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import comb


def predicted(n, ell):
    assert 3 <= n and 1 <= ell < n
    if ell == n-1:
        return {2: F(1)}
    m = n-ell-2
    a, b = F(ell-1, n-2), F(n-ell-1, n-2)
    out = defaultdict(F)
    for j in range(m+1):
        v = F(comb(m,j)*(n-1)**(m-j),n**m)
        out[1+j] += b*v
        out[2+j] += a*F(ell,ell+1)*v
        out[3+j] += a*F(1,ell+1)*v
    return {k:v for k,v in out.items() if v}


def edge_set_from_prufer(n, code):
    degree = [1]*n
    for v in code: degree[v] += 1
    edges=[]
    for v in code:
        leaf=next(i for i in range(n) if degree[i]==1)
        edges.append((leaf,v))
        degree[leaf]-=1;degree[v]-=1
    rem=[i for i in range(n) if degree[i]==1]
    edges.append(tuple(rem))
    return edges


def count_law(n):
    hist = defaultdict(lambda:defaultdict(int))
    for code in product(range(n),repeat=n-2):
        edges=edge_set_from_prufer(n, code)
        adj=[[] for _ in range(n)]
        for u,v in edges: adj[u].append(v);adj[v].append(u)
        levels={0:0};fr=[0]
        for x in fr:
            for y in adj[x]:
                if y not in levels:levels[y]=levels[x]+1;fr.append(y)
        hist[levels[1]][len(adj[2])]+=1
    for ell,counts in hist.items():
        total=sum(counts.values())
        expected=predicted(n,ell)
        got={k:F(v,total) for k,v in counts.items()}
        assert got==expected,(n,ell,got,expected)
    assert set(hist)==set(range(1,n))


def upper_tail(n,ell,k):
    return sum((v for d,v in predicted(n,ell).items() if d>=k),F(0))


def coefficient_cutoff(n,ell,k):
    # Delta P(degree>=k) between distance ell+1 and ell.
    assert 2 <= ell <= n-3
    h=n-ell-3; j=k-2
    c0=(ell+1)**2*(ell+2)
    c1=2*n-ell**3-ell**2+2*ell
    c2=-(ell+2)*(ell-1)
    # [z^j] (q+p*z)^h (c0+c1*z+c2*z*z) divided by
    # n*(ell+1)*(ell+2)*(n-2).
    acc=F(0)
    for r,c in enumerate((c0,c1,c2)):
        t=j-r
        if 0<=t<=h:
            acc += c*F(comb(h,t)*(n-1)**(h-t),n**h)
    return acc/F(n*(ell+1)*(ell+2)*(n-2))


def check_crossings(n):
    for ell in range(1,n):
        assert sum(predicted(n,ell).values())==1
    if n>=4:
        for k in range(2,n+1):
            assert upper_tail(n,2,k)>=upper_tail(n,1,k)
    for ell in range(2,n-1):
        deltas=[upper_tail(n,ell+1,k)-upper_tail(n,ell,k) for k in range(2,n+1)]
        saw_minus=False
        for d in deltas:
            if d<0: saw_minus=True
            if saw_minus: assert d<=0,(n,ell,'nonmonotone signs',deltas)
        assert deltas[0]>0 and any(d<0 for d in deltas), (n,ell,deltas)
        if ell <= n-3:
            for k in range(2,n+1):
                assert deltas[k-2] == coefficient_cutoff(n,ell,k),(n,ell,k,deltas[k-2],coefficient_cutoff(n,ell,k))
    if n>=4:
        assert upper_tail(n,n-1,2)>upper_tail(n,n-2,2)
        assert upper_tail(n,n-1,3)<upper_tail(n,n-2,3)
    for ell in range(1,n-1):
        a=sum(d*v for d,v in predicted(n,ell).items())
        b=sum(d*v for d,v in predicted(n,ell+1).items())
        assert b>a,(n,ell,'mean')

if __name__=='__main__':
    for n in range(3,8):
        count_law(n)
        print('PRUFER_EXHAUSTIVE_PASS',n,n**(n-2))
    for n in range(3,31):
        check_crossings(n)
    print('EXACT_TAIL_SINGLE_CROSSING_PASS n=3..30')
    print('VERIFY_OK')
