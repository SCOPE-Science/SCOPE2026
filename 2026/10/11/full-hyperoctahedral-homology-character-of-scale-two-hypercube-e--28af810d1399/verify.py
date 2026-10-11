#!/usr/bin/env python3
"""Reconstruct Čech cube faces; compare exact Lefschetz traces with cycle-character formula.
This finite computation does not prove the all-dimensions theorem.
"""
from itertools import permutations, combinations
from math import comb

def cube_faces(n):
    face_sets=[set() for _ in range(n+2)]
    for center in range(1<<n):
        neighbors=sorted([center]+[center^(1<<i) for i in range(n)])
        for k in range(1,n+2):
            face_sets[k].update(combinations(neighbors,k))
    return [tuple(sorted(fs)) for fs in face_sets[1:]]

def apply(x,p,b):
    y=b
    for i,j in enumerate(p):
        if x&(1<<i):y^=1<<j
    return y

def cycles(p):
    seen=set(); cs=[]
    for i in range(len(p)):
        if i in seen:continue
        c=[];j=i
        while j not in seen:
            seen.add(j);c.append(j);j=p[j]
        cs.append(tuple(c))
    return cs

def formula(n,p,b):
    cs=cycles(p);r=len(cs)
    a1=sum(len(c)==1 for c in cs)
    a2=sum(len(c)==2 for c in cs)
    parities=[sum((b>>i)&1 for i in c)%2 for c in cs]
    F=(1<<r) if all(not z for z in parities) else 0
    # each invariant binary vector with Hamming weight 1 or 2 is a union
    # of one 1-cycle, two 1-cycles, or one 2-cycle.
    z_supports=[]
    one=[c for c in cs if len(c)==1]
    two=[c for c in cs if len(c)==2]
    z_supports.extend(one)
    z_supports.extend(c1+c2 for c1,c2 in combinations(one,2))
    z_supports.extend(two)
    count=0
    for support in z_supports:
        z=sum(1<<i for i in support)
        if all(sum(((b^z)>>i)&1 for i in c)%2==0 for c in cs):count+=1
    assert count<=len(z_supports)
    # Double the equation to avoid floating point.
    two_L=F*(2-a1+comb(a1,2)-3*a2)+(1<<r)*count
    assert two_L%2==0
    return two_L//2-1

def chain_trace(face_sets,mapping):
    L=0
    for d,faces in enumerate(face_sets):
        S=set(faces);tr=0
        for face in faces:
            perm=[mapping[x] for x in face]
            if tuple(sorted(perm)) not in S:raise AssertionError('not simplicial')
            if tuple(sorted(perm))!=face:continue
            inversions=sum(x>y for i,x in enumerate(perm) for y in perm[i+1:])
            tr+=-1 if inversions%2 else 1
        L+=(-1)**d*tr
    return L-1

for n in range(2,6):
    fs=cube_faces(n)
    tested=0
    for p in permutations(range(n)):
        for b in range(1<<n):
            mapping=[apply(x,p,b) for x in range(1<<n)]
            found=chain_trace(fs,mapping)
            target=formula(n,p,b)
            assert found==target,(n,p,b,found,target)
            tested+=1
    dim=(1<<(n-2))*(n*n-3*n+4)-1
    identity=formula(n,tuple(range(n)),0)
    assert identity==dim
    for p in permutations(range(n)):
        av=sum(formula(n,p,b) for b in range(1<<n))
        assert av%(1<<n)==0
        a1=sum(p[i]==i for i in range(n))
        a2=sum(p[p[i]]==i and p[i]!=i for i in range(n))//2
        assert av//(1<<n)==comb(a1,2)-a2
    print(f'n={n}: {tested} automorphisms, {sum(map(len,fs))} nonempty faces, H2 dimension {dim}, all character traces and invariant exterior-square characters agree')

n=6;fs=cube_faces(n)
ps=[tuple(range(n)),tuple(reversed(range(n))),tuple((i+1)%n for i in range(n)),(1,0,3,2,5,4),(1,2,0,4,5,3)]
bs=[0,1,3,7,10,42,63]
for p in ps:
 for b in bs:
    mapping=[apply(x,p,b) for x in range(1<<n)]
    assert chain_trace(fs,mapping)==formula(n,p,b),(p,b)
print(f'n={n}: {len(ps)*len(bs)} selected automorphisms, {sum(map(len,fs))} nonempty faces, all traces agree')
print('VERIFY_OK')
