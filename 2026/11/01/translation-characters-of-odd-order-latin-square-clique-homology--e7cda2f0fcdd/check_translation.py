#!/usr/bin/env python3
"""Exact fixed-simplex traces for finite odd-order group Latin-square clique complexes.

This program directly enumerates all nonempty cliques and their signed
permutation traces. This is a finite consistency check, not a proof for all
finite abelian groups.
"""
from itertools import product


def case(moduli):
    elements = tuple(product(*(range(m) for m in moduli)))
    n = len(elements)
    assert n >= 5 and all(m % 2 for m in moduli)
    zero = tuple(0 for _ in moduli)
    def add(x, y):
        return tuple((a+b) % m for a,b,m in zip(x,y,moduli))
    cells = tuple(product(elements, repeat=2))
    index = {c:i for i,c in enumerate(cells)}
    N = len(cells)
    adjacent = [set() for _ in range(N)]
    for i,(r,c) in enumerate(cells):
        for j in range(i+1,N):
            s,d = cells[j]
            if r==s or c==d or add(r,c)==add(s,d):
                adjacent[i].add(j)
                adjacent[j].add(i)
    faces=[]
    def extend(face, future):
        for idx,v in enumerate(future):
            f=face+(v,)
            faces.append(f)
            extend(f, [u for u in future[idx+1:] if u in adjacent[v]])
    extend((), list(range(N)))
    by_size={}
    for f in faces: by_size[len(f)]=by_size.get(len(f),0)+1
    def sign_fixed(f, images):
        mapped=[images[x] for x in f]
        if tuple(sorted(mapped)) != f: return 0
        inv=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        return -1 if inv%2 else 1
    for a in elements:
        for b in elements:
            images=[index[(add(r,a),add(c,b))] for r,c in cells]
            trace=sum((1 if len(f)%2 else -1)*sign_fixed(f,images) for f in faces)
            expected_h2=(n*(a==zero)-1)*(n*(b==zero)-1)*(n*(add(a,b)==zero)-1)
            assert trace==1+expected_h2, (moduli,a,b,trace,expected_h2)
    # Compute mod-two Betti numbers from all boundary matrices.
    face_indices={}
    by_degree={}
    for f in faces: by_degree.setdefault(len(f)-1, []).append(f)
    for deg, ff in by_degree.items():
        face_indices[deg]={f:i for i,f in enumerate(ff)}
    ranks={}
    for deg in sorted(by_degree):
        if deg==0:
            ranks[deg]=0
            continue
        rows=face_indices[deg-1]
        pivots={}
        for f in by_degree[deg]:
            bits=0
            for j in range(len(f)):
                bits ^= 1<<rows[f[:j]+f[j+1:]]
            while bits:
                p=bits.bit_length()-1
                if p in pivots: bits ^= pivots[p]
                else:
                    pivots[p]=bits
                    break
        ranks[deg]=len(pivots)
    betti={deg:len(ff)-ranks[deg]-ranks.get(deg+1,0)
           for deg,ff in by_degree.items()}
    assert betti[0]==1 and betti[2]==(n-1)**3 and all(
        b==0 for deg,b in betti.items() if deg not in (0,2)),(moduli,betti)
    # Verify Fourier multiplicities by explicit counting of nontrivial third factors.
    # A finite abelian group is (noncanonically) isomorphic to its character group.
    for alpha in elements:
        for beta in elements:
            multiplicity=sum(g!=zero and g!=alpha and g!=beta for g in elements)
            assert multiplicity == n-len({zero,alpha,beta})
    assert sum(n-len({zero,a,b}) for a in elements for b in elements)==(n-1)**3
    print('PASS moduli=%s vertices=%d cliques=%d dimensions=%s translations=%d multiplicities=%d' %
          (moduli,N,len(faces),by_size,n*n,n*n))
    print('  F2 Betti numbers:', betti)

if __name__=='__main__':
    for moduli in [(5,), (7,), (9,), (3,3)]:
        case(moduli)
