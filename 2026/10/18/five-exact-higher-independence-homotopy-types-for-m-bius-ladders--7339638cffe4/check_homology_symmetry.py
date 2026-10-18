#!/usr/bin/env python3
"""Independently enumerate forbidden connected triples, mod-two ranks, dihedral Lefschetz traces."""
from collections import defaultdict
from itertools import combinations

TOP={4:(2,1),5:(3,9),6:(3,6),7:(4,1),8:(5,31)}

def forbidden_triples(n):
    N=2*n
    ed={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    ed.update((i,i+n) for i in range(n))
    bad=[]
    for triple in combinations(range(N),3):
        e=sum(tuple(sorted((u,v))) in ed for u,v in combinations(triple,2))
        if e>=2:bad.append(sum(1<<v for v in triple))
    return bad

def getfaces(n):
    N=2*n;bad=forbidden_triples(n)
    faces_by_dimension=defaultdict(list)
    allfaces=[]
    # every inadmissible triple witnesses a connected component on >=3 vertices
    for m in range(1,1<<N):
        if all(m&t!=t for t in bad):
            faces_by_dimension[m.bit_count()-1].append(m)
            allfaces.append(m)
    return allfaces,faces_by_dimension,len(bad)

def mod2_ranks(F):
    ranks={}
    for d in range(1,max(F)+1):
        prev_index={f:i for i,f in enumerate(F[d-1])}
        pivots={}
        for high in F[d]:
            boundary=0;rem=high
            while rem:
                bit=rem&-rem;rem-=bit
                boundary^=1<<prev_index[high^bit]
            while boundary:
                k=boundary.bit_length()-1
                if k in pivots:boundary^=pivots[k]
                else:pivots[k]=boundary;break
        ranks[d]=len(pivots)
    betti={d:len(F[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in F}
    return ranks,betti

def parity(img):
    return -1 if sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))%2 else 1

def character(n,allfaces,degree):
    N=2*n
    chars=[]
    for refl in [False,True]:
        row=[]
        for k in range(N):
            transform=[(k-i if refl else k+i)%N for i in range(N)]
            alt=0
            for f in allfaces:
                vertices=[i for i in range(N) if f>>i&1]
                images=[transform[i] for i in vertices]
                if sum(1<<v for v in images)==f:
                    alt+=(-1)**(len(vertices)-1)*parity(images)
            row.append((-1)**degree*(alt-1))
        chars.append(row)
    return chars

def main():
    for n,(degree,multiplicity) in TOP.items():
        allfaces,F,n_bad=getfaces(n)
        rank,betti=mod2_ranks(F)
        assert betti=={**{d:0 for d in F},degree:multiplicity,0:1},(n,betti)
        char=character(n,allfaces,degree)
        rot,ref=char
        assert rot[0]==multiplicity
        assert all(abs(x)<=multiplicity for x in rot+ref)
        assert sum(rot+ref)%(4*n)==0
        invariant=sum(rot+ref)//(4*n)
        assert invariant>=0
        print(f'n={n} connected_triples={n_bad} mod2_reduced_betti={ {d:b for d,b in betti.items() if d and b} } boundary_ranks={rank}')
        print(f'n={n} dihedral_rotation_character={rot} reflection_character={ref} invariant_rank_Q={invariant}')
    print('ALL_INDEPENDENT_HOMOLOGY_AND_CHARACTER_TESTS_PASSED')
if __name__=='__main__':main()
