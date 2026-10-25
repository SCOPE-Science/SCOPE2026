#!/usr/bin/env python3
"""Finite exhaustive 1-skeleton checks for cycle-target Hom covering maps."""
from collections import deque
from math import gcd


def vertices(m,t):
    out=[]
    def dfs(v):
        if len(v)==m:
            if (v[-1]-v[0])%t in (1,t-1): out.append(tuple(v))
            return
        for a in ((v[-1]-1)%t,(v[-1]+1)%t):dfs(v+[a])
    for a in range(t):dfs([a])
    return out

def walk(m,t):
    vv=vertices(m,t)
    ss=set(vv)
    def adjacent(f):
        for i in range(m):
            for d in (-2,2):
                g=list(f);g[i]=(f[i]+d)%t;g=tuple(g)
                if g!=f and g in ss:yield g
    f=next(x for x in vv if all((x[(i+1)%m]-x[i])%t in (1,t-1) for i in range(m)))
    target=tuple((x+2)%t for x in f)
    pred={f:None};q=deque([f])
    while q and target not in pred:
        x=q.popleft()
        for y in adjacent(x):
            if y not in pred:pred[y]=x;q.append(y)
    assert target in pred,(m,t)
    z=target;path=[]
    while z is not None:path.append(z);z=pred[z]
    path.reverse()
    seq=[]
    order=t//gcd(t,2)
    for shift in range(order):
        seg=[tuple((a+2*shift)%t for a in x) for x in path]
        seq.extend(seg[0 if shift==0 else 1:])
    assert seq[0]==seq[-1]
    return len(vv),seq

def winding(seq,t,v=0):
    s=0
    for a,b in zip(seq,seq[1:]):
        diff=(b[v]-a[v])%t
        if diff==0:continue
        if diff==2:s+=2
        elif diff==t-2:s-=2
        else:raise AssertionError(('bad map edge',t,a[v],b[v]))
    assert s%t==0
    return s//t

def run():
    cases=[(4,5,2),(4,6,2),(4,5,3),(4,5,4),(6,5,2),(6,6,2)]
    for m,n,k in cases:
        t=n*k
        count,path=walk(m,t)
        w=winding(path,t)
        reduced=[tuple(x%n for x in f) for f in path]
        out=winding(reduced,n)
        d=lambda x:2 if x%2 else 1
        expected=k*d(t)//d(n)
        assert w!=0 and out==k*w,(m,n,k,w,out)
        assert abs(w)==d(t) and abs(out)==expected*d(n),(m,n,k,w,out,expected)
        print('VERIFIED',f'm={m},target={t}->{n}',f'vertices={count}',f'source_degree={w}',f'target_degree={out}',f'multiplier={expected}')
    print('CYCLE_COVERING_HOMOLOGY_FINITE_CHECKS_PASSED')

if __name__=='__main__':run()
