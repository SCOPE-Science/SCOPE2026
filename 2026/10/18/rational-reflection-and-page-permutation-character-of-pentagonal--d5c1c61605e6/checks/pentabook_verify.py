#!/usr/bin/env python3
"""Finite checks of a parameter-uniform Morse matching for polygonal edge-books."""
import collections

def edges(n):
    e=[(0,1)]
    for i in range(n):
        a,b,c = range(2+3*i,5+3*i)
        e.extend([(0,a),(a,b),(b,c),(c,1)])
    return e

def masks(n):
    e=edges(n); inc=[0]*len(e)
    for i,x in enumerate(e):
        for j,y in enumerate(e):
            if i!=j and (x[0] in y or x[1] in y):inc[i] |= 1<<j
    faces=[0]
    for i in range(len(e)):
        faces += [f|(1<<i) for f in faces if not(f&inc[i])]
    return faces

def partner(n,s):
    F=1; C=0
    for i in range(n):
        A=1<<(4*i+1); B=1<<(4*i+2); c=1<<(4*i+3)
        C |=c
        if not (s & (A|c)):
            return s ^ B
    # all pages block the B toggle
    if s==C or s==(C|F):return s^F
    for i in range(n):
        A=1<<(4*i+1); c=1<<(4*i+3)
        t=(C^c)|A; u=C|A
        if s==t or s==u:return s^c
    return None

def verify(n):
    f=masks(n); idx={s:i for i,s in enumerate(f)}
    assert len(idx)==len(f)
    pairs={};crit=[]
    for s in f:
        t=partner(n,s)
        if t is None: crit.append(s);continue
        assert t in idx, (n,s,t)
        assert s^t and ((s^t)&((s^t)-1))==0
        assert partner(n,t)==s
        pairs[s]=t
    expected={(sum(1<<(4*j+3) for j in range(n) if j!=i)|(1<<(4*i+1))|(1<<(4*i+4))) for i in range(n)}
    assert set(crit)==expected,(n,crit,expected)
    # Orient matched covering from smaller face to larger, other incidences from larger to smaller.
    # Compute indegree, then topological sort of the complete directed Hasse graph.
    indegree=[0]*len(f); incoming=collections.defaultdict(list)
    for s in f:
        x=s
        while x:
            bit=x&-x; x-=bit; t=s^bit
            if pairs.get(t)==s: lo=t;hi=s
            else:lo=s;hi=t
            indegree[idx[hi]]+=1
            incoming[lo].append(hi)
    q=collections.deque(s for s in f if indegree[idx[s]]==0)
    visited=0
    while q:
        v=q.popleft();visited+=1
        for w in incoming.get(v,[]):
            iw=idx[w];indegree[iw]-=1
            if indegree[iw]==0:q.append(w)
    assert visited==len(f),(n,visited,len(f))
    assert all(s.bit_count()==n+1 for s in crit)
    return (n,len(f),len(pairs)//2,len(crit),visited)

if __name__=='__main__':
    for n in range(1,8):print('MATCHING_OK',*verify(n),flush=True)
