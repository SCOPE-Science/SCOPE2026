#!/usr/bin/env python3
"""Exact finite cellular verification for a two-point graph configuration space.

No external packages are required. All rational-rank conclusions follow from
integer cycles and finite-field rank lower bounds. The odd characteristic 101
is used only to establish characteristic-zero lower bounds, not to infer
integral torsion groups.
"""
from itertools import combinations
from fractions import Fraction

CYCLES = [[0, 0, 0, 0, 0, 0, 0, -1, 1, 0, -1, 0, 1, 0, 1, -1, 0, 1, 0, 0, -1, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, -1, 1, 0, -1, 0, 0, 1, 0], [1, -1, 0, 1, 0, 0, -1, 0, 0, -1, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, 0, 0, 0, 0, -1, 0, 0, 1, 0, 1]]

N = 8
edges = sorted(set(tuple(sorted((i, (i + 1) % N))) for i in range(N)) |
               set(tuple(sorted((i, (i + 4) % N))) for i in range(4)))
vertices = list(combinations(range(N), 2))
one = [(v, e) for e in edges for v in range(N) if v not in e]
two = [(e, f) for e, f in combinations(edges, 2) if not (set(e) & set(f))]
idx0 = {a:i for i,a in enumerate(vertices)}
idx1 = {a:i for i,a in enumerate(one)}
idx2 = {a:i for i,a in enumerate(two)}

B1 = [dict() for _ in one]
for j, (v, (a,b)) in enumerate(one):
    B1[j] = {idx0[tuple(sorted((v,b)))]:1,
             idx0[tuple(sorted((v,a)))]:-1}
B2 = [dict() for _ in two]
for j, ((a,b),(c,d)) in enumerate(two):
    for pair, val in [((b,(c,d)),1), ((a,(c,d)),-1),
                      ((d,(a,b)),-1), ((c,(a,b)),1)]:
        i=idx1[pair];B2[j][i]=B2[j].get(i,0)+val

def rank_mod(columns, p=101):
    pivots={}
    for col in columns:
        z={i:(v%p) for i,v in col.items() if v%p}
        while z:
            k=min(z);c=z[k]
            if k not in pivots:
                inv=pow(c,-1,p)
                pivots[k]={i:(v*inv)%p for i,v in z.items()}
                break
            for i,v in pivots[k].items():
                nv=(z.get(i,0)-c*v)%p
                if nv:z[i]=nv
                else:z.pop(i,None)
    return len(pivots)

def rank_rational(columns):
    """Exact rational Gaussian elimination, no finite-field assumptions."""
    pivots={}
    for col in columns:
        z={i:Fraction(v) for i,v in col.items() if v}
        while z:
            k=min(z);c=z[k]
            if k not in pivots:
                pivots[k]={i:v/c for i,v in z.items()}
                break
            for i,v in pivots[k].items():
                nv=z.get(i,0)-c*v
                if nv:z[i]=nv
                else:z.pop(i,None)
    return len(pivots)

def boundary(vec, columns):
    o={}
    for j,a in vec.items():
        for i,b in columns[j].items():
            o[i]=o.get(i,0)+a*b
    return {i:v for i,v in o.items() if v}

def signed_action(cell, dim, group_element):
    k,eps=group_element
    f=lambda i:(k+eps*i)%N
    if dim==0:
        return idx0[tuple(sorted(f(i) for i in cell))],1
    if dim==1:
        v,e=cell
        mapped=tuple(f(i) for i in e)
        oriented=tuple(sorted(mapped))
        return idx1[(f(v),oriented)],1 if mapped==oriented else -1
    e,h=cell
    a=tuple(f(i) for i in e);b=tuple(f(i) for i in h)
    ae=tuple(sorted(a));be=tuple(sorted(b))
    sign=(1 if a==ae else -1)*(1 if b==be else -1)
    if ae>be:
        ae,be=be,ae;sign=-sign
    return idx2[(ae,be)],sign

def apply(cell_vector,dim,g):
    out={}
    cells=[vertices,one,two][dim]
    for j,v in cell_vector.items():
        k,signed=signed_action(cells[j],dim,g)
        out[k]=out.get(k,0)+signed*v
    return {j:v for j,v in out.items() if v}

def invariant_basis(dim, group):
    cells=[vertices,one,two][dim]
    seen=set();basis=[]
    for i in range(len(cells)):
        if i in seen:continue
        d={};inconsistent=False
        for g in group:
            j,sgn=signed_action(cells[i],dim,g)
            if j in d and d[j]!=sgn:inconsistent=True
            d[j]=sgn
        seen.update(d)
        if not inconsistent:basis.append(d)
    return basis

def invariant_betti(group):
    bases=[invariant_basis(k,group) for k in range(3)]
    ranks=[]
    for k,columns in [(1,B1),(2,B2)]:
        reps={min(d):i for i,d in enumerate(bases[k-1])}
        restriction=[]
        for d in bases[k]:
            image=boundary(d,columns)
            restriction.append({j:image[rep] for rep,j in reps.items()
                                if image.get(rep,0)})
        ranks.append(rank_rational(restriction))
    sizes=[len(x) for x in bases]
    return (sizes[0]-ranks[0], sizes[1]-sum(ranks),sizes[2]-ranks[1])

def test():
    assert (len(edges),len(vertices),len(one),len(two))==(12,28,72,42)
    for face in B2:
        assert not boundary(face,B1)
    assert rank_mod(B1)==27
    assert rank_mod(B2)==40
    assert len(CYCLES)==2 and all(len(x)==42 for x in CYCLES)
    assert CYCLES[0][40:]==[1,0]
    assert CYCLES[1][40:]==[0,1]
    assert not boundary({i:v for i,v in enumerate(CYCLES[0]) if v},B2)
    assert not boundary({i:v for i,v in enumerate(CYCLES[1]) if v},B2)
    # Equivariance of both integer cellular boundary operators under all
    # automorphisms: not merely consistency on the chosen cycles.
    for g in [(k,e) for k in range(8) for e in (1,-1)]:
        for dim,columns in [(1,B1),(2,B2)]:
            for j in range(len(columns)):
                assert boundary(apply({j:1},dim,g),columns)==apply(columns[j],dim-1,g)
    assert rank_rational(B1)==27 and rank_rational(B2)==40
    # The two cycles, with projection to coordinates 40 and 41 the identity,
    # form the full integral kernel because its rational dimension is two.
    r=(1,1);s=(0,-1)
    for i in range(2):
        x={j:v for j,v in enumerate(CYCLES[i]) if v}
        rimage=apply(x,2,r);simage=apply(x,2,s)
        assert all(rimage.get(j,0)==-CYCLES[1-i][j] for j in range(42))
        assert all(simage.get(j,0)==CYCLES[1-i][j] for j in range(42))
    assert invariant_betti([(k,e) for k in range(8) for e in (1,-1)])==(1,0,0)
    assert invariant_betti([(k,1) for k in range(8)])==(1,1,1)
    assert invariant_betti([(0,1),(0,-1)])==(1,2,1)
    print('WAGNER_TWO_POINT_INTEGRAL_DIHEDRAL_LATTICE_OK')
    print('CUBICAL_CELLS 28 72 42; BOUNDARY_RANKS 27 40; H2_INTEGER_RANK 2')
    print('QUOTIENT_BETTI_FULL (1,0,0); ROTATIONS (1,1,1); REFLECTION (1,2,1)')

if __name__=='__main__':
    test()
