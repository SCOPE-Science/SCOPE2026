#!/usr/bin/env python3
from itertools import combinations
from math import comb


def w_adj(n):
    A = [set() for _ in range(n)]
    for v in range(n):
        for d in (-2,-1,1,2):
            A[v].add((v+d) % n)
    return A


def connected_induced(A, verts):
    verts = set(verts)
    if not verts:
        return False
    seen = {next(iter(verts))}
    stack = list(seen)
    while stack:
        v = stack.pop()
        for w in A[v] & verts:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return seen == verts


def run_lengths(n, S):
    S=set(S)
    if not S:
        return []
    if len(S)==n:
        return [n]
    # starts are selected vertices whose predecessor is not selected
    starts=[v for v in S if (v-1)%n not in S]
    out=[]
    for s in starts:
        r=0
        v=s
        while v in S:
            r+=1
            v=(v+1)%n
        out.append(r)
    return sorted(out, reverse=True)


def check_k(k):
    n=k+5
    A=w_adj(n)
    V=tuple(range(n))
    facets=[]
    for S in combinations(V,5):
        retained=[v for v in V if v not in S]
        disc=not connected_induced(A, retained)
        criterion=sum(r>=2 for r in run_lengths(n,S))>=2
        assert disc == criterion, (k,S,run_lengths(n,S),disc,criterion)
        if disc:
            facets.append(frozenset(S))
    faces=set()
    for F in facets:
        fs=tuple(F)
        for r in range(1,6):
            for T in combinations(fs,r):
                faces.add(frozenset(T))
    fv=[sum(len(F)==r for F in faces) for r in range(1,6)]
    expected=[n,comb(n,2),comb(n,3),n*k*(k+2)//2,n*k*(k-1)//2]
    assert fv==expected,(k,fv,expected)
    red=-1+sum((1 if i%2==0 else -1)*fv[i] for i in range(5))
    expected_red=(k**3-19*k+24)//6
    beta=(k-3)*(k-2)*(k+5)//6
    assert red==expected_red
    assert red+1==beta
    return len(facets),fv,red,beta

for k in range(3,15):
    facets,fv,red,beta=check_k(k)
    print(f"k={k} facets={facets} f={fv} red_chi={red} beta_if_wedge={beta}")
print("SQUARED_CYCLE_FACE_VERIFY_OK")
