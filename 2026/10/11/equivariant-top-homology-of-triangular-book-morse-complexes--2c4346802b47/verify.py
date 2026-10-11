#!/usr/bin/env python3
"""Reproduce the finite checks for the Morse complex of triangle books.

Only the Python standard library is required. This script enumerates oriented
rooted forests directly from the defining no-directed-cycle condition, computes
automorphism traces on augmented simplex chains, and independently computes
mod-2 boundary ranks for the first few page counts. Its finite checks corroborate,
but do not replace, the all-page proof in RESULT.md.
"""
from collections import defaultdict
from itertools import product


def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
    else:
        if maximum is None:
            maximum = n
        for j in range(min(n, maximum), 0, -1):
            for rem in integer_partitions(n-j, j):
                yield (j,) + rem


def leaf_permutation(cycle_lengths):
    k = sum(cycle_lengths)
    out = list(range(k))
    start = 0
    for ell in cycle_lengths:
        for i in range(ell):
            out[start + i] = start + ((i+1) % ell)
        start += ell
    return out


def graph_and_faces(k):
    n = k+2
    edges = [(0,1)] + [(h,i) for i in range(2,n) for h in (0,1)]
    arcs = sorted([(a,b) for a,b in edges]+[(b,a) for a,b in edges])
    index = {arc:i for i,arc in enumerate(arcs)}
    opts = [[None]+[index[(u,v)] for v in range(n) if (u,v) in index] for u in range(n)]
    faces=[]
    for choices in product(*opts):
        face = tuple(sorted(q for q in choices if q is not None))
        parent = {arcs[q][0]:arcs[q][1] for q in face}
        valid = True
        for x in parent:
            visited=set()
            while x in parent:
                if x in visited:
                    valid=False
                    break
                visited.add(x)
                x=parent[x]
            if not valid:
                break
        if valid:
            faces.append(face)
    assert len(faces)==len(set(faces))
    assert () in faces
    return arcs,faces


def trace(k,arc_list,faces,cycle_lengths,swap):
    n = k+2
    p=list(range(n))
    if swap:
        p[0],p[1]=1,0
    p[2:]=[u+2 for u in leaf_permutation(cycle_lengths)]
    index={a:i for i,a in enumerate(arc_list)}
    induced=[index[(p[u],p[v])] for u,v in arc_list]
    total=0
    for face in faces:
        shifted=[induced[q] for q in face]
        if set(face)!=set(shifted):
            continue
        ordered=sorted(face)
        places={a:i for i,a in enumerate(ordered)}
        permutation=[places[q] for q in shifted]
        inversions=sum(permutation[i]>permutation[j]
                       for i in range(len(face)) for j in range(i+1,len(face)))
        total += (-1)**(len(face)+inversions)
    # The trace on top reduced homology equals (-1)^(k+1) times
    # the signed invariant-face sum including the empty face.
    return (-1)**(k+1)*total


def expected(k,cycle_lengths,swap):
    f=cycle_lengths.count(1)
    if not swap:
        sign=(-1)**(k-len(cycle_lengths))
        return sign*(f+1)**2
    e=sum(ell%2==0 for ell in cycle_lengths)
    t=cycle_lengths.count(2)
    return (-1)**(k+1+e)*(1-f+2*t)


def binary_rank(columns):
    pivots={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p]=v
                break
    return len(pivots)


def check_homology(k,faces):
    cells=defaultdict(list)
    for face in faces:
        if face:
            cells[len(face)-1].append(face)
    maxdim=max(cells)
    ranks={}
    for d in range(1,maxdim+1):
        positions={a:i for i,a in enumerate(cells[d-1])}
        boundary=[]
        for face in cells[d]:
            vec=0
            for i in range(len(face)):
                sub=face[:i]+face[i+1:]
                vec ^= (1<<positions[sub])
            boundary.append(vec)
        ranks[d]=binary_rank(boundary)
    for d in range(maxdim+1):
        betti=len(cells[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
        assert betti==(k+1)**2 if d==k else betti==0,(k,d,betti)
    return [len(cells[d]) for d in range(maxdim+1)],ranks


def run():
    total_conjugacy_checks=0
    for k in range(2,7):
        arcs,faces=graph_and_faces(k)
        for cycle_lengths in integer_partitions(k):
            for swap in (False,True):
                got=trace(k,arcs,faces,cycle_lengths,swap)
                want=expected(k,cycle_lengths,swap)
                assert got==want,(k,cycle_lengths,swap,got,want)
                total_conjugacy_checks+=1
        trivial = (1,)*k
        assert trace(k,arcs,faces,trivial,False)==(k+1)**2
        if k<=4:
            f_vector,ranks=check_homology(k,faces)
            print('k=',k,'f_vector=',f_vector,'binary_boundary_ranks=',ranks)
        print('k=',k,'nonempty_faces=',len(faces)-1,
              'conjugacy_classes=',len(tuple(integer_partitions(k))))
    assert total_conjugacy_checks==2*sum(len(tuple(integer_partitions(k))) for k in range(2,7))
    print('CONJUGACY_CHECKS=',total_conjugacy_checks)
    print('VERIFY_OK')

if __name__=='__main__':
    run()
