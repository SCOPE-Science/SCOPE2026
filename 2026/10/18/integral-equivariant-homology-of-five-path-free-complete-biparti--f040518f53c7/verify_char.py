#!/usr/bin/env python3
"""Separate equivariant Lefschetz-trace verification (no third-party modules)."""
from itertools import permutations
from math import comb

def parity_image(face,perm):
    vals=[perm[x] for x in face]
    return -1 if sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals)))%2 else 1

def paths_avoided(face,m):
    a=sum(x<m for x in face)
    b=len(face)-a
    # Five-vertex alternating path in complete bipartite graph needs (3,2) or (2,3)
    return not (a>=3 and b>=2 or a>=2 and b>=3)

def complex_faces(m,n):
    return [tuple(i for i in range(m+n) if mask>>i &1)
            for mask in range(1,1<<(m+n))
            if paths_avoided(tuple(i for i in range(m+n) if mask>>i &1),m)]

def sq_fixed(g):
    return sum(g[g[i]]==i for i in range(len(g)))

def test(m,n):
    F=complex_faces(m,n)
    actions=0
    for a in permutations(range(m)):
      for b in permutations(range(n)):
        perm=tuple(a)+(tuple(m+x for x in b))
        Lef=0
        for face in F:
            if {perm[x] for x in face}==set(face):
                Lef+=(-1)**(len(face)-1)*parity_image(face,perm)
        x=sum(a[i]==i for i in range(m)); x2=sq_fixed(a)
        y=sum(b[j]==j for j in range(n)); y2=sq_fixed(b)
        wm=(x*x-x2)//2; wn=(y*y-y2)//2
        um=x-1; un=y-1
        # Character of exterior square of the standard (augmentation) rep.
        am=(um*um-(x2-1))//2
        an=(un*un-(y2-1))//2
        predicted=wm*wn-um*un
        decomposed=am*un+um*an+am*an
        assert predicted==decomposed,(m,n,a,b,predicted,decomposed)
        assert 1-Lef==predicted,(m,n,a,b,Lef,predicted)
        actions+=1
    print(f'({m},{n}): all {actions} group actions match character formula; faces={len(F)}')

if __name__=='__main__':
    for m,n in ((3,3),(3,4),(4,4)):
        test(m,n)
    print('ALL EQUIVARIANT LEFSCHETZ CHECKS PASSED')
