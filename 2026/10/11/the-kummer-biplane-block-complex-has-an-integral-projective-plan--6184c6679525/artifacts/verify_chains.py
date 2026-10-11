#!/usr/bin/env python3
"""Independent face enumeration and reduced homology checks over finite fields.

The calculation uses simplicial boundary matrices directly, not Morse pairings.
The complementary prime characteristics detect the factor of two in the Morse
attaching degrees. Rank computations by themselves do not establish homotopy.
"""
from collections import defaultdict


def generate_graph(which):
    vertices = range(16)
    neighbor_sets = []
    for a in vertices:
        i, j = divmod(a, 4)
        neighbors = []
        for b in vertices:
            k, l = divmod(b, 4)
            if which == 'rook':
                relation = ((k == i) != (l == j))
            else:
                delta = ((k-i) % 4, (l-j) % 4)
                relation = delta in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3))
            if relation:
                neighbors.append(b)
        assert len(neighbors) == 6
        neighbor_sets.append(tuple(neighbors))
    return neighbor_sets


def simplices(neighbors):
    faces = defaultdict(set)
    for nbrs in neighbors:
        for selection in range(1, 1 << 6):
            tup = tuple(nbrs[t] for t in range(6) if selection & (1 << t))
            faces[len(tup)-1].add(tup)
    return {d: sorted(s) for d,s in faces.items()}


def matrix_rank_mod_p(columns, p):
    pivots = {}
    rank = 0
    for column in columns:
        vec = {i:(c % p) for i,c in column.items() if c % p}
        while vec:
            pivot = min(vec)
            if pivot in pivots:
                multiple = vec[pivot]
                base = pivots[pivot]
                for r, val in base.items():
                    c = (vec.get(r, 0) - multiple*val) % p
                    if c:
                        vec[r] = c
                    else:
                        vec.pop(r, None)
            else:
                scale = pow(vec[pivot], -1, p)
                pivots[pivot] = {r:val*scale % p for r,val in vec.items()}
                rank += 1
                break
    return rank


def check(name):
    faces = simplices(generate_graph(name))
    dims = sorted(faces)
    assert dims == [0,1,2,3,4,5]
    counts = tuple(len(faces[d]) for d in dims)
    assert counts == (16,120,320,240,96,16),counts
    for prime in (2,3,5):
        ranks = [1]  # Rank of the reduced augmentation C_0 -> C_{-1}
        for d in range(1,6):
            rowmap = {face:i for i,face in enumerate(faces[d-1])}
            boundary = []
            for f in faces[d]:
                boundary.append({rowmap[f[:i] + f[i+1:]]: (-1)**i for i in range(len(f))})
            ranks.append(matrix_rank_mod_p(boundary,prime))
        expected = (1,15,104,160,80,16) if prime == 2 else (1,15,105,160,80,16)
        assert tuple(ranks) == expected,(prime,ranks)
        reduced_betti = []
        for d in range(6):
            r_lo = ranks[d]
            r_hi = ranks[d+1] if d < 5 else 0
            reduced_betti.append(counts[d]-r_lo-r_hi)
        assert tuple(reduced_betti) == ((0,1,56,0,0,0) if prime == 2
                                        else (0,0,55,0,0,0))
        print(f"{name}: F_{prime} ranks={ranks[:-1]} reduced_betti={reduced_betti}")


def main():
    for graph in ('rook','shrikhande'):
        check(graph)
    print('CHAIN_CHECK_OK')


if __name__ == '__main__':
    main()
