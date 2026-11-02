#!/usr/bin/env python3
"""Independent direct complete FO rank-three type recursion for finite graphs.
No vertex-transitivity assumption or pair-spectrum shortcut is used.
"""
from itertools import product

def graph(lengths):
    V=list(product(*(range(n) for n in lengths)))
    N=len(V); d=len(lengths)
    A=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            diff=[k for k in range(d) if V[i][k]!=V[j][k]]
            if len(diff)==1:
                k=diff[0]
                A[i][j]=A[j][i]=(V[i][k]-V[j][k])%lengths[k] in (1,lengths[k]-1)
    return A

def type3(A):
    N=len(A)
    # q=1 types over ordered pairs, using every possible third vertex.
    pairs=[[None]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            atomset=set()
            for z in range(N):
                code=(int(x==y)<<0)|(int(x==z)<<1)|(int(y==z)<<2)| \
                     (int(A[x][y])<<3)|(int(A[x][z])<<4)|(int(A[y][z])<<5)
                atomset.add(code)
            pairs[x][y]=(int(x==y),int(A[x][y]),tuple(sorted(atomset)))
    # q=2 types over a single selected vertex.
    pointed=[]
    for x in range(N):
        pointed.append(tuple(sorted(set(pairs[x]))))
    # q=3 type over the empty tuple, with all vertex choices.
    return tuple(sorted(set(pointed)))

SAMPLES=[
    (3,), (4,), (5,), (6,), (7,), (8,), (12,),
    (3,3), (3,3,3), (3,3,3,3),
    (3,4), (3,5), (3,3,4),
    (4,4), (4,5), (4,6), (5,5), (3,6),
    (3,4,4), (4,4,4), (4,5,5),
]

def expected_group(L):
    if len(L)==1 and L[0]<=6:return str(L[0])
    if len(L)==1 or all(n>=4 for n in L):return 'triangle-free tail'
    if all(n==3 for n in L):return 'all triangle 2' if len(L)==2 else 'all triangle 3+'
    return 'mixed'

if __name__=='__main__':
    type_to_group={}
    grouped={}
    for L in SAMPLES:
        t=type3(graph(L)); group=expected_group(L)
        if t in type_to_group:assert type_to_group[t]==group,(L,group,type_to_group[t])
        type_to_group[t]=group
        grouped.setdefault(group,set()).add(t)
        assert len(grouped[group])==1,(L,group)
        print(L,'->',group, 'rank-three singleton types:',len(t))
    assert len(type_to_group)==8
    print('PASS: exact three-quantifier recursion finds eight classes across',len(SAMPLES),'graphs')
