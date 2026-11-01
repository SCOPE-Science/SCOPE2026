#!/usr/bin/env python3
"""Exact finite checks for closed-neighborhood complexes of complements of bipartite two-factors.
Usage: python check.py (Python standard library only)."""
from itertools import combinations
from collections import defaultdict

def faces(facets):
    return {tuple(s) for F in facets for j in range(len(F)+1) for s in combinations(sorted(F),j)}

def build(parts):
    n=sum(parts)
    A=set(range(n)); B=set(range(n,2*n))
    forbidden=set(); pos=0
    for m in parts:
        for j in range(m):
            i=pos+j; x=pos+j; y=pos+(j+1)%m
            forbidden.update(((i,n+x),(i,n+y)))
        pos+=m
    edges={(i,n+j) for i in A for j in range(n)}-forbidden
    FA=[{i}|{v for v in B if (i,v) in edges} for i in sorted(A)]
    FB=[{j}|{v for v in A if (v,j) in edges} for j in sorted(B)]
    U,V=faces(FA),faces(FB)
    UB={s for s in U if set(s)<=B}
    VA={s for s in V if set(s)<=A}
    return n,edges,U,V,UB,VA

def rank(cols):
    piv={}
    for x in cols:
        while x:
            hi=x.bit_length()-1
            if hi in piv:x^=piv[hi]
            else:piv[hi]=x;break
    return len(piv)

def betti(F):
    d=defaultdict(list)
    for s in F:
        if s:d[len(s)-1].append(s)
    rs={}
    for i in range(1,max(d)+1):
        idx={s:j for j,s in enumerate(sorted(d[i-1]))}
        cs=[]
        for s in d[i]:
            bit=0
            for k in range(len(s)):bit^=1<<idx[s[:k]+s[k+1:]]
            cs.append(bit)
        rs[i]=rank(cs)
    return {i:b for i,v in d.items() if (b:=len(v)-rs.get(i,0)-rs.get(i+1,0)-(i==0))}

def check():
    cases=((7,),(3,4),(8,),(3,5),(4,4),(9,),(3,6),(4,5),(3,3,3))
    for p in cases:
        n,E,U,V,UB,VA=build(p)
        W=U&V
        assert W=={()}|{(i,) for i in range(2*n)}|E,('intersection',p)
        h=n-2-sum((m+1)//3 for m in p)
        mu=2**sum(m%3==0 for m in p)
        expected={2:n*n-4*n+1,h:2*mu}
        assert betti(UB)=={h:mu},('side homology',p,betti(UB))
        assert betti(VA)=={h:mu},('other side homology',p,betti(VA))
        actual=betti(U|V)
        assert actual==expected,('whole',p,actual,expected)
        assert all(tuple(s) in UB for s in combinations(sorted(range(n,2*n)),3))
        print('cycles',p,'faces',len(U|V),'homology',dict(sorted(actual.items())),flush=True)
    print('VERIFY_OK',len(cases),'two-factors',flush=True)
if __name__=='__main__':check()
