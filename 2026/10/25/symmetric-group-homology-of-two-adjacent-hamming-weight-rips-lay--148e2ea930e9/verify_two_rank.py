#!/usr/bin/env python3
"""Exact equivariant checks for distance-two two-rank Boolean Vietoris--Rips complexes."""
from itertools import combinations, permutations
from collections import Counter
from functools import lru_cache
from math import factorial

@lru_cache(None)
def partitions(n, maximum=None):
    if not n: return ((),)
    if maximum is None: maximum=n
    return tuple((a,)+b for a in range(min(n,maximum),0,-1) for b in partitions(n-a,a))

def representative(cycle_lengths):
    n=sum(cycle_lengths); perm=list(range(n)); off=0
    for length in cycle_lengths:
        for j in range(length): perm[off+j]=off+(j+1)%length
        off+=length
    return perm

def coefficient(cycle_lengths, alpha):
    if min(alpha)<0 or sum(alpha)!=sum(cycle_lengths):return 0
    states={(0,)*len(alpha):1}
    for length in cycle_lengths:
        new={}
        for tuple_state,mult in states.items():
            for j in range(len(alpha)):
                if tuple_state[j]+length>alpha[j]:continue
                v=list(tuple_state);v[j]+=length;v=tuple(v)
                new[v]=new.get(v,0)+mult
        states=new
    return states.get(tuple(alpha),0)

def sign_of_permutation(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1

def schur_character(shape,cycle_lengths):
    d=len(shape); total=0
    for p in permutations(range(d)):
        alpha=tuple(shape[i]-i+p[i] for i in range(d))
        if min(alpha)<0:continue
        total+=sign_of_permutation(p)*coefficient(cycle_lengths,alpha)
    return total

def predicted_specht(n,k,cycles):
    t=min(k,n-k-1)
    r0=min(k-1,n-k-1)
    r1=min(k,n-k-2)
    a=sum(schur_character((n-j-1,j,1),cycles) for j in range(1,t+1))
    b=sum(schur_character((n-j-2,j,1,1),cycles) for j in range(1,r0+1))
    c=sum(schur_character((n-j-2,j,1,1),cycles) for j in range(1,r1+1))
    return a+b+c

def all_faces(n,k):
    verts=[frozenset(v) for a in (k,k+1) for v in combinations(range(n),a)]
    adjacency=[]
    for i,u in enumerate(verts):
        adjacency.append({j for j,v in enumerate(verts) if j>i and len(u.symmetric_difference(v))<=2})
    result=[]
    def visit(cur,candidates):
        for v in sorted(candidates):
            face=cur+(v,);result.append(face)
            visit(face,candidates.intersection(adjacency[v]))
    visit((),set(range(len(verts))))
    return verts,result

def trace_faces(vertices, faces,perm):
    index={v:i for i,v in enumerate(vertices)}
    permvert=[index[frozenset(perm[x] for x in v)] for v in vertices]
    trace=0
    for face in faces:
        image=tuple(permvert[i] for i in face)
        if set(image)!=set(face):continue
        ordered=sorted(image)
        order=[ordered.index(j) for j in image]
        trace+= (-1 if len(face)%2==0 else 1)*sign_of_permutation(order)
    return trace-1

def run():
    cases=[(5,2),(6,2),(6,3),(7,3),(8,3),(8,4)]
    for n,k in cases:
        vertices,faces=all_faces(n,k)
        counts=Counter(len(f) for f in faces)
        for cycles in partitions(n):
            got=trace_faces(vertices,faces,representative(cycles))
            expected=predicted_specht(n,k,cycles)
            assert got==expected,(n,k,cycles,got,expected)
        print(f'n={n} k={k}: vertices={len(vertices)}, faces={len(faces)}, faces_by_size={dict(sorted(counts.items()))}, classes={len(partitions(n))}, H2rank={predicted_specht(n,k,(1,)*n)}')
    print('TWO_RANK_BOOLEAN_EQUIVARIANT_OK')

if __name__=='__main__':run()
