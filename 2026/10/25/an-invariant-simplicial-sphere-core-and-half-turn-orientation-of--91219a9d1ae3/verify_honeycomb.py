#!/usr/bin/env python3
"""Independent finite checks for strip-honeycomb perfect-matching complexes.
Uses the source paper's explicit plane-partition-to-edge formula and no
external dependencies. Finite experiments support, not prove, the theorem.
"""
from itertools import combinations

def facet(n,u,v):
    assert 0<=v<=u<=n
    edges={('a',1,u),('a',2,v)}
    edges|={('b',0,j) for j in range(u+1,n+1)}
    edges|={('b',1,j) for j in range(v+1,u+1)}
    edges|={('b',2,j) for j in range(1,v+1)}
    edges|={('d',0,j) for j in range(u)}
    edges|={('d',1,j) for j in range(n+1) if j>u or j<v}
    edges|={('d',2,j) for j in range(v+1,n+1)}
    return frozenset(edges)

def turn(n,e):
    t,i,j=e
    if t=='a': return (t,3-i,n-j)
    if t=='b': return (t,2-i,n+1-j)
    return (t,2-i,n-j)

def all_faces(n):
    faces={frozenset()}
    parts=[(u,v) for u in range(n+1) for v in range(u+1)]
    facets=[facet(n,u,v) for u,v in parts]
    for f in facets:
        l=list(f)
        for mask in range(1,1<<len(l)):
            faces.add(frozenset(l[i] for i in range(len(l)) if mask>>i&1))
    return faces,parts,facets

def sign_of_turn(n,face):
    arr=sorted(face)
    images=[turn(n,e) for e in arr]
    assert sorted(images)==arr
    inv=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    return -1 if inv%2 else 1

def test(n):
    faces,parts,facets=all_faces(n)
    for (u,v),P in zip(parts,facets):
        assert {turn(n,e) for e in P}==facet(n,n-v,n-u)
    x=('d',0,0);y=('d',2,n)
    D=frozenset(('d',1,j) for j in range(1,n))
    F=frozenset({x,y}|set(D))
    assert F not in faces
    assert all(F-{e} in faces for e in F)
    assert {turn(n,e) for e in F}==F
    remaining=set(faces)
    pairs=[]
    for t in (x,y):
        for f in list(remaining):
            if t not in f:
                g=f|{t}
                if g in remaining:
                    pairs.append((f,g))
                    remaining.remove(f);remaining.remove(g)
    tau=frozenset({y}|set(D))
    assert remaining=={tau},(n,remaining)
    assert all((a<=F)==(b<=F) for a,b in pairs)
    count=0; trace=-1
    for face in faces:
        if not face: continue
        if frozenset(turn(n,e) for e in face)==face:
            count+=1
            trace+=(-1)**(len(face)-1)*sign_of_turn(n,face)
    theoretical=(-1)**(n-1)*(-1)**(1+(n-1)//2)
    assert trace==theoretical,(n,trace,theoretical)
    print('n',n,'facets',len(facets),'faces',len(faces),'relative_pairs',sum(not a<=F for a,b in pairs),'fixed_faces',count,'reduced_L',trace,'degree',(-1)**(1+(n-1)//2))

if __name__=='__main__':
    for n in (2,3,4): test(n)
    print('HONEYCOMB_RELATIVE_COLLAPSE_HALF_TURN_FINITE_CHECKS_OK')

# An independent elementary-collapse replay via dynamic free-face queues.
def direct_collapse(n):
    from collections import deque
    fac=[facet(n,u,v) for u in range(n+1) for v in range(u+1)]
    vertices=sorted(set().union(*fac))
    idx={v:i for i,v in enumerate(vertices)}
    facets=[sum(1<<idx[v] for v in f) for f in fac]
    allmasks={0}
    for f in facets:
        s=f
        while s:
            allmasks.add(s)
            s=(s-1)&f
    x=1<<idx[('d',0,0)];y=1<<idx[('d',2,n)]
    F=x|y|sum(1<<idx[('d',1,j)] for j in range(1,n))
    faces=set(allmasks)
    pairs=[]
    for t in (x,y):
        for f in list(faces):
            if not f&t and f|t in faces:
                pairs.append((f,f|t))
                faces.remove(f);faces.remove(f|t)
    assert faces=={F^x}
    pairs=[(a,b) for a,b in pairs if a&~F]
    active=set(allmasks)
    lowers={a:b for a,b in pairs}
    cnt={a:0 for a in lowers}
    for U in active:
        if U==0:continue
        sub=U
        while sub:
            l=U^(sub&-sub)
            if l in cnt: cnt[l]+=1
            sub^=sub&-sub
    todo=deque(a for a in lowers if cnt[a]==1)
    deleted=0
    while todo:
        a=todo.popleft()
        b=lowers[a]
        if a not in active or b not in active or cnt[a]!=1:continue
        active.remove(a);active.remove(b);deleted+=1
        for U in (a,b):
            sub=U
            while sub:
                l=U^(sub&-sub)
                if l in cnt and l in active:
                    cnt[l]-=1
                    if cnt[l]==1:todo.append(l)
                sub^=sub&-sub
    assert deleted==len(pairs),(n,deleted,len(pairs))
    assert active=={s for s in allmasks if s&~F==0},(n,len(active))
    assert F not in active
    print('n',n,'explicit_elementary_collapses',deleted,'surviving_boundary_faces',len(active))

if __name__=='__main__':
    for n in (2,3,4): direct_collapse(n)
    print('HONEYCOMB_ACTUAL_ELEMENTARY_COLLAPSE_REPLAY_OK')
