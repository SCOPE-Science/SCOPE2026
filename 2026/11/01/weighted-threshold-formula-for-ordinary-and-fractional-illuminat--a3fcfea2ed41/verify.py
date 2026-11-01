#!/usr/bin/env python3
"""Exact consistency checks for illumination of positively weighted cube caps.
Run: python3 verify.py. Standard library only. The analytic proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def subset_weight(a, mask):
    return sum((w for i,w in enumerate(a) if mask & (1 << i)), F(0))


def cube_vertex(d, mask):
    return tuple(F(1) if mask & (1 << i) else F(-1) for i in range(d))


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))


def formula(a,T):
    return sum(subset_weight(a,mask) <= T for mask in range(1<<len(a))) + sum(w>T for w in a)


def vertices(a,T):
    d=len(a); cap=2*T-sum(a)
    v={cube_vertex(d,mask) for mask in range(1<<d) if subset_weight(a,mask)<=T}
    for mask in range(1<<d):
        sw=subset_weight(a,mask)
        if sw>=T:
            continue
        for i in range(d):
            if mask & (1<<i) or sw+a[i]<=T:
                continue
            w=list(cube_vertex(d,mask))
            w[i]=-1+2*(T-sw)/a[i]
            v.add(tuple(w))
    return v


def directions(a,T):
    d=len(a); A=sum(a)
    D=[]
    for mask in range(1<<d):
        if subset_weight(a,mask)>T: continue
        if mask==0:
            D.append(tuple(F(1) for _ in range(d)))
        else:
            i=next(i for i in range(d) if mask & (1<<i))
            v=[F(-1) if mask & (1<<j) else F(1) for j in range(d)]
            v[i]=-2*A/a[i]
            D.append(tuple(v))
    for i in range(d):
        if a[i]>T:
            v=[F(1)]*d
            v[i]=-2*A/a[i]
            D.append(tuple(v))
    return D


def illuminated(a,T,p,v):
    d=len(a); cap=2*T-sum(a)
    if not all(p[i]!=1 or v[i]<0 for i in range(d)): return False
    if not all(p[i]!=-1 or v[i]>0 for i in range(d)): return False
    if dot(a,p)==cap and dot(a,v)>=0: return False
    return True


def rank_in_vertex(a,T,p):
    d=len(a); cap=2*T-sum(a)
    active=sum(abs(x)==1 for x in p)
    if dot(a,p)==cap: active+=1
    # All generated vertices have at least d independent active facets.
    return active>=d


def eliminate(M,b):
    """Exact square linear system, returns None on singularity."""
    n=len(b); A=[list(map(F,row))+[F(rhs)] for row,rhs in zip(M,b)]
    for j in range(n):
        k=next((k for k in range(j,n) if A[k][j]),None)
        if k is None: return None
        A[j],A[k]=A[k],A[j]
        p=A[j][j]
        A[j]=[z/p for z in A[j]]
        for k in range(n):
            if k!=j:
                f=A[k][j]
                if f:
                    A[k]=[u-f*v for u,v in zip(A[k],A[j])]
    return tuple(row[-1] for row in A)


def independent_vertices(a,T):
    d=len(a); cap=2*T-sum(a)
    facets=[]
    for j in range(d):
        for sign in (-1,1):
            normal=[F(0)]*d; normal[j]=F(sign)
            facets.append((tuple(normal), F(1)))
    facets.append((tuple(a),cap))
    vs=set()
    for chosen in combinations(facets,d):
        x=eliminate([n for n,b in chosen],[b for n,b in chosen])
        if x is not None and all(dot(n,x)<=b for n,b in facets):
            vs.add(x)
    return vs


def run():
    passed=0; systems=0
    special=[(1,1),(3,1,1),(1,1,1),(3,1,1,2),(2,2,4,4),
             (1,2,3,4,5),(2,3,5,7,11),(1,1,1,1,1,1)]
    for d in range(2,7):
        for a0 in special+list(combinations_with_replacement((1,2,3),d))[:6]:
            if len(a0)!=d: continue
            a=tuple(map(F,a0)); A=sum(a)
            boundaries={F(0),A}
            boundaries.update(subset_weight(a,mask) for mask in range(1<<d))
            thresholds={x for x in boundaries if F(0)<x<A}
            sorted_b=sorted(boundaries)
            thresholds.update((x+y)/2 for x,y in zip(sorted_b, sorted_b[1:]) if x<y)
            for T in sorted(thresholds)[::max(1,len(thresholds)//8)]:
                vs=vertices(a,T); D=directions(a,T)
                expected=formula(a,T)
                assert len(D)==expected and len(set(D))==len(D),(a,T,D)
                assert all(rank_in_vertex(a,T,v) for v in vs),(a,T)
                assert all(-1<=x<=1 and dot(a,v)<=2*T-A for v in vs for x in v)
                assert all(any(illuminated(a,T,v,u) for u in D) for v in vs),(a,T)
                # The lower certificate consists of the old vertex orthants
                # and the cut vertices on edges adjacent to the bottom vertex.
                old={cube_vertex(d,m) for m in range(1<<d) if subset_weight(a,m)<=T}
                assert len(old)+sum(w>T for w in a)==expected
                for i,w in enumerate(a):
                    if w>T:
                        v=tuple(F(-1)+2*T/w if j==i else F(-1) for j in range(d))
                        assert v in vs,(a,T,i)
                        assert all(illuminated(a,T,v,u)==False for u in D[:len(old)])
                # For every old vertex, only its opposite sign orthant illuminates it.
                for p in old:
                    assert sum(illuminated(a,T,p,u) for u in D)==1,(a,T,p)
                systems+=1; passed+=len(vs)+len(D)
            # Independently enumerate active-facet intersections for selected small cases.
            if d<=4:
                for T in sorted(thresholds)[::max(1,len(thresholds)//3)]:
                    assert independent_vertices(a,T)==vertices(a,T),(a,T)
                    passed+=1
    # The symmetric caps yield a binomial tail except at the simplex endpoint.
    for d in range(2,11):
        a=(F(1),)*d
        for k in range(d):
            T=F(k)+F(1,2)
            expected=sum(comb(d,j) for j in range(k+1)) + (d if k==0 else 0)
            # For T<1: only the all-negative old cube vertex plus d special caps.
            assert formula(a,T)==expected,(d,k,T)
            passed+=1
    assert formula((F(3),F(1),F(1)),F(5,2))==5
    assert formula((F(1),F(1),F(1)),F(3,2))==4
    print('VERIFY_OK weighted cube-cap illumination:',systems,'exact parameter systems;',passed,'checks')


def combinations_with_replacement(seq,n):
    from itertools import combinations_with_replacement as C
    return C(seq,n)

if __name__=='__main__': run()
