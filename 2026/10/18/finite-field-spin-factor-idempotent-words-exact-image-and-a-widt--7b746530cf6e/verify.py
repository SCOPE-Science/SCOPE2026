#!/usr/bin/env python3
"""Exact finite-field checks for the spin-factor idempotent-word classification.

Uses only the Python standard library; finite enumeration supplements the proof.
"""
from itertools import product
from math import comb


def check_field(p, diagonal):
    n=len(diagonal)
    vecs=list(product(range(p), repeat=n))
    half=pow(2,-1,p)
    quarter=pow(4,-1,p)
    def form(v):return sum(diagonal[i]*v[i]*v[i] for i in range(n))%p
    def bil(v,w):return sum(diagonal[i]*v[i]*w[i] for i in range(n))%p
    nontrivial=[(half,*v) for v in vecs if form(v)==quarter]
    ones=[(0,)+(0,)*n,(1,)+(0,)*n]
    idem=ones+nontrivial
    def mult(x,e):
        a=x[0];b=e[0];v=x[1:];w=e[1:]
        return ((a*b+bil(v,w))%p, *((a*w[i]+b*v[i])%p for i in range(n)))
    for e in idem:assert mult(e,e)==e
    levels={e:1 for e in idem}
    frontier=set(idem)
    for depth in range(2,9):
        fresh={mult(x,e) for x in frontier for e in nontrivial if mult(x,e) not in levels}
        for y in fresh:levels[y]=depth
        frontier=fresh
        if not frontier:break
    minus_det=(-1)
    for a in diagonal:minus_det=minus_det*a%p
    good=pow(minus_det,(p-1)//2,p)==1
    is_bad=n==3 and not good
    missing={(a,*v) for a in range(p) for v in vecs if (a,*v) not in levels}
    predicted={(a,)+(0,)*n for a in range(p) if a not in (0,1)}
    if is_bad:predicted|={(0,*v) for v in vecs if v!=(0,)*n and form(v)==0}
    assert missing==predicted,(p,n,diagonal,len(missing),len(predicted),missing.symmetric_difference(predicted))
    assert max(levels.values())==(6 if p==3 and is_bad else 5)
    return p,n,diagonal,len(idem),len(levels),max(levels.values())


def check_exception_orbits():
    p=3
    def typ(x):return (x[0],sum(v!=0 for v in x[1:]))
    es=[(2,*(1 if j==i else 0 for j in range(3))) for i in range(3)]
    es += [(2,*(2 if j==i else 0 for j in range(3))) for i in range(3)]
    def mul(x,e):
        a=x[0];b=e[0];v=x[1:];w=e[1:]
        return ((a*b+sum(v[i]*w[i] for i in range(3)))%p, *((a*w[i]+b*v[i])%p for i in range(3)))
    orbits={(a,r) for a in range(3) for r in range(4)}
    transition={}
    for a,r in orbits:
        rep=(a,)+(1,)*r+(0,)*(3-r)
        transition[(a,r)]={typ(mul(rep,e)) for e in es}
    reached={(0,0),(1,0),(2,1)}
    minima={key:1 for key in reached}
    front=set(reached)
    for depth in range(2,8):
        new={v for u in front for v in transition[u] if v not in reached}
        for v in new:minima[v]=depth
        reached|=new
        front=new
    assert orbits-reached=={(2,0),(0,3)}
    assert {k:v for k,v in sorted(minima.items())}=={
        (0,0):1,(0,1):3,(0,2):4,(1,0):1,(1,1):4,(1,2):2,
        (1,3):6,(2,1):1,(2,2):5,(2,3):3}
    assert sum(comb(3,r)*2**r for a,r in reached)==72
    return transition

if __name__=='__main__':
    for p,n,d in [
        (3,3,[1,1,1]),(3,3,[1,1,2]),
        (5,3,[1,1,1]),(5,3,[1,1,2]),
        (7,3,[1,1,1]),(7,3,[1,1,3]),
        (3,4,[1,1,1,1]),(5,4,[1,1,1,1])]:
        print('CASE_OK:',check_field(p,d))
    transition=check_exception_orbits()
    print('EXCEPTION_ORBITS_OK:',len(transition),'orbit types, total reachable 72 of 81')
    print('VERIFY_OK: finite-field BFS and exact exceptional orbit-transition certificate')
