"""Standalone reproducibility checks for a triangular three-spin plaquette model.
Standard Python 3 only. The proof of the asymptotic entropy gap is mathematical,
not established by these finite checks.
"""
from collections import Counter
from itertools import combinations
from random import Random


def positions(L):
    return [(i, j) for i in range(L) for j in range(L)]


def index(i, j, L):
    return (i % L) * L + j % L


def plaquettes_of_spin(s, L):
    i, j = s
    return {index(i,j,L), index(i+1,j,L), index(i,j+1,L)}


def defect_mask_from_spin_mask(sm, L):
    d = 0
    for i,j in positions(L):
        v = ((sm >> index(i,j,L)) ^ (sm >> index(i-1,j,L)) ^
             (sm >> index(i,j-1,L))) & 1
        d |= v << index(i,j,L)
    return d


def triangular_adjacency(L):
    return [{index(i+di,j+dj,L) for di,dj in
             ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))}
            for i,j in positions(L)]


def is_independent(mask, adjacency):
    return all(not any(mask >> w & 1 for w in adjacency[v])
               for v in range(len(adjacency)) if mask >> v & 1)


def flip_support_mask(spins, L):
    m = 0
    for s in spins:
        for v in plaquettes_of_spin(s,L):
            m ^= 1 << v
    return m


def change_in_defects(d, spins, L):
    f = flip_support_mask(spins,L)
    return f.bit_count() - 2 * (d & f).bit_count()


def inverse_map_test(L):
    rng = Random(83179 + L)
    # On a power-of-two torus, A^L=I over GF(2): inverse A^(L-1).
    def A(s): return defect_mask_from_spin_mask(s,L)
    for _ in range(40):
        original = rng.getrandbits(L*L)
        current = original
        for step in range(L):
            current = A(current)
        assert current == original, (L, 'dyadic operator power')
    return 40


def run():
    L=4
    adj=triangular_adjacency(L)
    dist=Counter(); stable=0; stable_two=0; disagreement=0
    all_spin_mask=set()
    for sm in range(1 << (L*L)):
        d=defect_mask_from_spin_mask(sm,L)
        # Finiteness + bijection checked independently.
        all_spin_mask.add(d)
        loc = all(change_in_defects(d,[s],L)>0 for s in positions(L))
        indep=is_independent(d,adj)
        assert loc==indep, ('1-spin classification',sm)
        if loc:
            stable+=1
            dist[d.bit_count()]+=1
            assert all(change_in_defects(d,pair,L)>=0
                       for pair in combinations(positions(L),2)), ('2-spin robustness',sm)
            stable_two+=1
        elif indep:
            disagreement+=1
    assert len(all_spin_mask)==2**(L*L), 'Dyadic bijection'
    assert not disagreement
    assert stable==stable_two==201
    assert dict(dist)=={0:1,1:16,2:72,3:96,4:16}

    # Direct three-spin energy lowering with two separated defects.
    for L in (4,8):
        defects=(1<<index(0,0,L)) | (1<<index(2,0,L))
        assert is_independent(defects,triangular_adjacency(L))
        triple=[(0,0),(1,0),(0,1)]
        assert flip_support_mask(triple,L)==sum(1<<index(*p,L) for p in [(0,0),(2,0),(0,2)])
        assert change_in_defects(defects,triple,L)==-1
        assert all(change_in_defects(defects,[s],L)>0 for s in positions(L))
        assert all(change_in_defects(defects,pair,L)>=0 for pair in combinations(positions(L),2))

    # The 5x5 witness is compatible with every exterior independent set.
    for L in (8,16):
        target={(1,2),(3,2)}
        block={(i,j) for i in range(5) for j in range(5)}
        assert all((i+di)%L in range(5) and (j+dj)%L in range(5)
                   for i,j in target
                   for di,dj in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)])
        assert is_independent(sum(1<<index(*p,L) for p in target),triangular_adjacency(L))
        assert (L//5)**2 >= L*L/100
        assert len(block)==25
    checked=inverse_map_test(4)+inverse_map_test(8)+inverse_map_test(16)
    print('PASS: 65,536 spin assignments exhaustively verified on 4x4;')
    print('PASS: dyadic bijection; exact polynomial 1+16z+72z^2+96z^3+16z^4;')
    print('PASS: one- and two-spin stable counts both 201;')
    print('PASS: three-spin lowering witness on 4x4 and 8x8;')
    print('PASS: two valid disjoint-block entropy-gap ingredients;')
    print(f'PASS: {checked} randomized dyadic A^L identity tests.')

if __name__=='__main__':
    run()
