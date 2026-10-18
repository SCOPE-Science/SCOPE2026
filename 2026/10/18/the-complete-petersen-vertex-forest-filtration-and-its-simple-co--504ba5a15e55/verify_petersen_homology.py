"""Independent exact finite-field chain check of Petersen forest filtration.
Run in same directory as verify_petersen_forest.py with Python 3 standard library.
Morse matching in the companion verifier proves integral homotopy; this
calculation checks ranks independently and is not an integral certificate.
"""
from collections import defaultdict
from verify_petersen_forest import EDGES, N


def is_face(mask, bound):
    active = {i for i in range(N) if mask & (1 << i)}
    counts = {v: 0 for v in active}
    parent = {v: v for v in active}

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for i, j in EDGES:
        if i in active and j in active:
            counts[i] += 1
            counts[j] += 1
            if counts[i] > bound or counts[j] > bound:
                return False
            ri, rj = root(i), root(j)
            if ri == rj:
                return False
            parent[ri] = rj
    return True


def rank(columns, p):
    pivots = {}
    for col in columns:
        vec = {r: val % p for r, val in col.items() if val % p}
        while vec:
            k = max(vec)
            pivot = pivots.get(k)
            if pivot is None:
                pivots[k] = vec
                break
            alpha = vec[k] * pow(pivot[k], -1, p) % p
            for j, x in pivot.items():
                new = (vec.get(j, 0) - alpha * x) % p
                if new:
                    vec[j] = new
                elif j in vec:
                    del vec[j]
    return len(pivots)


def homology(d, p):
    ff = [m for m in range(1, 1 << N) if is_face(m, d)]
    simplices = defaultdict(list)
    for m in ff:
        simplices[m.bit_count()-1].append(m)
    top = max(simplices)
    ranks = [0] * (top+2)
    for degree in range(1, top+1):
        index = {m: i for i, m in enumerate(simplices[degree-1])}
        boundary = []
        for m in simplices[degree]:
            vertices = [i for i in range(N) if m & (1 << i)]
            boundary.append({index[m ^ (1 << v)]: (-1)**j for j, v in enumerate(vertices)})
        ranks[degree] = rank(boundary, p)
    betti = [len(simplices[d]) - ranks[d] - ranks[d+1] for d in range(top+1)]
    betti[0] -= 1
    return betti, len(ff), ranks


def main():
    expected = {0: [0, 0, 4, 0],
                1: [0, 0, 0, 1, 0, 0],
                2: [0, 0, 0, 1, 0, 0],
                3: [0, 0, 0, 0, 0, 6, 0]}
    for d in range(4):
        for p in (2, 3, 5, 101):
            betti, count, ranks = homology(d, p)
            assert betti == expected[d], (d, p, betti)
            print('degree=%d field=%d faces=%d reduced_betti=%s ranks=%s OK' %
                  (d, p, count, betti, ranks))
    print('HOMOLOGY_CROSSCHECK_OK')


if __name__ == '__main__':
    main()
