#!/usr/bin/env python3
"""Independent finite check of involution-fixed directed forest complexes."""
from itertools import combinations
from math import comb

def arcs_graph(f,t):
    N=f+2*t
    g=list(range(N))
    for i in range(t):g[f+2*i],g[f+2*i+1]=g[f+2*i+1],g[f+2*i]
    arcs=set((u,v) for u in range(N) for v in range(N) if u!=v)
    groups=[]
    while arcs:
        a=min(arcs)
        orbit=tuple(sorted({a,(g[a[0]],g[a[1]])}))
        for b in orbit:arcs.remove(b)
        groups.append(orbit)
    def isforest(arclist):
        incoming={}
        nxt={}
        for u,v in arclist:
            if v in incoming:return False
            incoming[v]=u
        for v in range(N):
            seen=set(); x=v
            while x in incoming:
                if x in seen:return False
                seen.add(x);x=incoming[x]
        return True
    allowed=[o for o in groups if isforest(o)]
    fs={0:[()]}
    for k in range(1,f+t):
        arr=[]
        for face in combinations(range(len(allowed)),k):
            if isforest([e for idx in face for e in allowed[idx]]):arr.append(face)
        fs[k]=arr
    return allowed,fs

def rank2(basis,previous):
    pos={v:i for i,v in enumerate(previous)}
    piv={}
    for face in basis:
        x=0
        for i in range(len(face)):
            sub=face[:i]+face[i+1:]
            x^=1<<pos[sub]
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)

def testcase(f,t):
    allowed,faces=arcs_graph(f,t)
    m=f+t
    fnums=[len(faces[k]) for k in range(m)]
    assert len(allowed)==f*(f-1)+f*t+2*t*(t-1)
    assert len(faces[m-1])>0
    boundaries={0:1}
    for k in range(1,m):
        boundaries[k]=rank2(faces[k],faces[k-1])
    betti={}
    for k in range(1,m):
        b=fnums[k]-boundaries.get(k,0)-boundaries.get(k+1,0)
        if b:betti[k-1]=b
    zeta=sum((-1)**k*fnums[k] for k in range(m))
    expected=(2*t-1)**(t-1) if f==0 else (f-1)**f*(f+2*t-1)**(t-1)
    if f==0 and t==1: expected=1
    predictedEuler=(-1)**(m-2)*expected
    print(f'f={f},t={t},N={f+2*t}; vertices={len(allowed)},fvector={fnums[1:]}, Betti={betti}; predicted rank={expected}; chirel={-zeta}, expectedchi={predictedEuler}')
    assert -zeta==predictedEuler
    assert betti==({m-2:expected} if expected and m>=2 else {})

if __name__=='__main__':
    allowed_empty, unused_faces = arcs_graph(0,1)
    assert not allowed_empty  # fixed geometric realization is empty
    for f,t in [(0,2),(0,3),(1,1),(1,2),(1,3),(2,1),(2,2),(3,1),(3,2),(4,1)]:testcase(f,t)
    print('VERIFY_OK')
