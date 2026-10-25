#!/usr/bin/env python3
"""Exact finite linear-algebra certificates for the four-cut cylinder theorem.

Only standard-library Python is needed. All arrays are constructed from definitions.
No case with more than four layers is needed in the infinite-family proof.
"""
from itertools import combinations


def graph(m):
    vertices = tuple((i,j) for i in range(4) for j in range(m))
    adjacency = {v: set() for v in vertices}
    for i,j in vertices:
        for w in (((i+1)%4,j), ((i-1)%4,j), (i,j-1), (i,j+1)):
            if w in adjacency:
                adjacency[i,j].add(w)
    return vertices, adjacency


def connected(subset, adjacency):
    todo = [subset[0]]
    seen = {subset[0]}
    target = set(subset)
    while todo:
        for w in adjacency[todo.pop()]:
            if w in target and w not in seen:
                seen.add(w)
                todo.append(w)
    return len(seen) == len(subset)


def binary_rank(columns):
    basis = {}
    for value in columns:
        while value:
            pivot = value.bit_length()-1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def relative_certificate(m):
    vertices, adj = graph(m)
    last = set((i,m-1) for i in range(4))
    triangles = [t for t in combinations(vertices,3) if last.intersection(t)]
    row = {t:i for i,t in enumerate(triangles)}
    columns = []
    for s in combinations(vertices,4):
        if not last.intersection(s) or not connected(s,adj):
            continue
        value = 0
        for face in combinations(s,3):
            if face in row:
                value ^= (1 << row[face])
        columns.append(value)
    return len(columns), binary_rank(columns)


# Four labels enumerate the even-parity side of a cube. On the odd side,
# label j denotes the unique nonneighbor of even vertex j. Thus edges
# are X_i--Y_j exactly when i != j.
PAIRS = tuple(combinations(range(4), 2))
CROSS_TETRA = tuple((a,b) for a in PAIRS for b in PAIRS if a != b)
SIGNED_CYCLES = (
    (-1,1,1,-1,0,1,-1,0,1,0,-1,1,-1,0,0,-1,0,1,-1,0,1,-1,0,1,0,0,0,0,0,0),
    (-1,1,0,0,-1,1,-1,1,0,1,-1,1,-1,0,0,0,-1,1,0,-1,0,0,0,0,0,1,-1,0,1,0),
    (-1,1,0,0,-1,1,-1,0,1,0,-1,1,0,-1,1,0,0,0,0,0,0,-1,1,0,-1,1,0,-1,0,1),
)


def signed_cube_certificates():
    triples = tuple(combinations(range(8),3))
    row = {s:i for i,s in enumerate(triples)}
    vectors = []
    for coeffs in SIGNED_CYCLES:
        assert len(coeffs) == len(CROSS_TETRA) == 30
        bd = [0]*len(triples)
        support_mask = 0
        for pos,((a,b),coeff) in enumerate(zip(CROSS_TETRA,coeffs)):
            if not coeff:
                continue
            support_mask |= 1<<pos
            tetra = tuple(sorted(a + tuple(4+j for j in b)))
            for omit in range(4):
                face = tetra[:omit] + tetra[omit+1:]
                bd[row[face]] += coeff * (-1 if omit%2 else 1)
        assert all(x==0 for x in bd), 'signed cube cycle boundary not zero'
        assert support_mask.bit_count() == 16
        vectors.append(support_mask)
    assert binary_rank(vectors) == 3
    # Every supported simplex has two vertices on each bipartition side,
    # so it is not a simplex contained in a single horizontal layer.
    return 3


def no_five_faces(m):
    vertices, adj = graph(m)
    for s in combinations(vertices,5):
        if all(connected(t,adj) for t in combinations(s,4)):
            return False
    return True


def main():
    assert signed_cube_certificates() == 3
    expected = {2:(37,34),3:(69,66),4:(73,70)}
    for m,answer in expected.items():
        result = relative_certificate(m)
        assert result==answer,(m,result,answer)
        assert no_five_faces(m)
        print('layers',m,'relative connected 4-sets',result[0],
              'relative boundary rank mod 2',result[1],
              'relative 3-cycle dimension',result[0]-result[1])
    print('CYLINDER_FOURCUT_EXACT_LOCAL_CERTIFICATES_OK')


if __name__ == '__main__':
    main()
