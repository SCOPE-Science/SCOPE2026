#!/usr/bin/env python3
"""Finite checks of individualized counting refinement on rectangular rook graphs.
This verifies finite instances only; the all-size result requires a proof.
"""
from itertools import product, combinations, permutations
from collections import Counter
import random


def refine(m,n,marks):
    vs=list(product(range(m),range(n)))
    adj=[tuple(j for j,w in enumerate(vs) if v!=w and (v[0]==w[0] or v[1]==w[1])) for v in vs]
    lookup={v:i for i,v in enumerate(vs)}
    c=[0]*len(vs)
    for z,v in enumerate(marks,1): c[lookup[v]]=z
    levels=[c]
    for step in range(1,4):
        sig=[(c[i],tuple(sorted(Counter(c[j] for j in adj[i]).items()))) for i in range(len(vs))]
        dictionary={s:i for i,s in enumerate(sorted(set(sig)))}
        c=[dictionary[s] for s in sig]
        levels.append(c)
        if len(set(c))==len(set(levels[-2])):
            break
    return vs,levels


def orbit_signature(m,n,marks,v):
    rs=tuple(i for i,(r,c) in enumerate(marks) if r==v[0])
    cs=tuple(i for i,(r,c) in enumerate(marks) if c==v[1])
    matching=(len({r for r,c in marks})==len(marks)==len({c for r,c in marks}))
    if m==n and matching: return tuple(sorted((rs,cs)))
    return (rs,cs)


def same_partition(c,sigs):
    return all((c[i]==c[j])==(sigs[i]==sigs[j]) for i in range(len(c)) for j in range(i+1,len(c)))


def full_aut_orbit(m,n,marks):
    vs=list(product(range(m),range(n)))
    at={v:i for i,v in enumerate(vs)}
    par=list(range(m*n))
    def root(a):
        while a!=par[a]:a=par[a]
        return a
    def join(a,b):par[root(a)]=root(b)
    count=0
    for p in permutations(range(m)):
      for q in permutations(range(n)):
       for flip in ([False,True] if m==n else [False]):
        trans=(lambda r,c:(p[c],q[r])) if flip else (lambda r,c:(p[r],q[c]))
        if all(trans(*v)==v for v in marks):
            count+=1
            for v in vs:join(at[v],at[trans(*v)])
    return [root(i) for i in range(len(vs))],count


def check(m,n,marks,group=False):
    vs,levels=refine(m,n,marks)
    sigs=[orbit_signature(m,n,marks,v) for v in vs]
    if not same_partition(levels[-1],sigs):raise AssertionError(('orbit mismatch',m,n,marks,levels[-1],sigs))
    a,b=len({r for r,c in marks}),len({c for r,c in marks})
    t=len(marks)
    if m==n and a==t==b:
        expected=t*(t+1)//2+(t+1)*(t<m)
    else:
        expected=(a+(a<m))*(b+(b<n))
    if len(set(sigs))!=expected:
        raise AssertionError(('class formula',m,n,marks,expected,len(set(sigs))))
    if len(levels)>4: raise AssertionError(('depth > 2',m,n,marks))
    if group:
        orbits,count=full_aut_orbit(m,n,marks)
        if not same_partition(orbits,sigs):raise AssertionError(('automorphism discrepancy',m,n,marks,count))
    return len(levels)-2,len(set(sigs))


def main():
    report=[]
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        vs=list(product(range(m),range(n)))
        ct=Counter();cls=0
        for mask in range(1<<(m*n)):
            marks=[v for i,v in enumerate(vs) if mask>>i&1]
            depth,k=check(m,n,marks,group=(m*n<=9))
            ct[depth]+=1;cls+=1
        report.append((m,n,cls,dict(sorted(ct.items()))))
    rng=random.Random(22062014)
    for m,n,N in [(3,5,500),(4,5,500),(5,5,500),(5,6,500),(6,7,500)]:
        vs=list(product(range(m),range(n)))
        for _ in range(N):
            marks=rng.sample(vs,rng.randrange(0,len(vs)+1))
            check(m,n,marks)
        report.append((m,n,N,'sampled'))
    ex=[(0,0),(0,1),(1,2)]
    _,levels=refine(4,4,ex)
    assert len(levels)-2==2
    print('EXHAUSTIVE',report[:6])
    print('SAMPLED',report[6:])
    print('SHARP_EXAMPLE',{'m':4,'n':4,'marks':ex,'strict_rounds':2})
    print('ALL_TESTS_PASS')

if __name__=='__main__':main()
