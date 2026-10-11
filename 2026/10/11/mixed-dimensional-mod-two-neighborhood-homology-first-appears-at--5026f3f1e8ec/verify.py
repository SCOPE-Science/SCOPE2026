from itertools import combinations


def triangular_graph_neighborhood_complex(n):
    vertices = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(vertices)}
    facets = []
    for e in vertices:
        facet = [index[f] for f in vertices if f != e and (e[0] in f or e[1] in f)]
        facets.append(tuple(sorted(facet)))
    maxdim = max(len(F) for F in facets) - 1
    faces = [set() for _ in range(maxdim + 1)]
    for F in facets:
        for r in range(1, len(F) + 1):
            for s in combinations(F, r):
                faces[r - 1].add(s)
    return vertices, facets, [sorted(x) for x in faces]


def gf2_rank(columns):
    pivots = {}
    rank = 0
    for x in columns:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in pivots:
                y ^= pivots[p]
            else:
                pivots[p] = y
                rank += 1
                break
    return rank


def boundary_rank(faces, k):
    lower = {s: i for i, s in enumerate(faces[k - 1])}
    cols = []
    for s in faces[k]:
        bits = 0
        for t in combinations(s, k):
            bits ^= 1 << lower[t]
        cols.append(bits)
    return gf2_rank(cols)


def betti_profile(n):
    vertices, facets, faces = triangular_graph_neighborhood_complex(n)
    ranks = [boundary_rank(faces, k) for k in range(1, len(faces))]
    betti = []
    for k in range(len(faces)):
        rk_down = ranks[k - 1] if k else 0
        rk_up = ranks[k] if k < len(ranks) else 0
        betti.append(len(faces[k]) - rk_down - rk_up)
    chi_faces = sum(((-1) ** k) * len(faces[k]) for k in range(len(faces)))
    chi_hom = sum(((-1) ** k) * betti[k] for k in range(len(betti)))
    assert chi_faces == chi_hom
    assert len(vertices) == n * (n - 1) // 2
    assert all(len(F) == 2 * (n - 2) for F in facets)
    return [len(x) for x in faces], ranks, betti

expected = {
    3: [1, 1],
    4: [1, 1, 0, 0],
    5: [1, 0, 0, 11, 0, 0],
    6: [1, 0, 0, 91, 0, 0, 0, 0],
    7: [1, 0, 0, 246, 7, 0, 0, 0, 0, 0],
}

profiles = {}
for n in range(3, 8):
    fvec, ranks, betti = betti_profile(n)
    assert betti == expected[n]
    profiles[n] = (fvec, ranks, betti)

# Reduced homology is obtained by deleting beta_0=1.
for n in range(3, 7):
    nonzero = [k for k, b in enumerate(profiles[n][2][1:], start=1) if b]
    assert len(nonzero) == 1
nonzero7 = [k for k, b in enumerate(profiles[7][2][1:], start=1) if b]
assert nonzero7 == [3, 4]
assert profiles[7][2][3] == 246 and profiles[7][2][4] == 7

print('VERIFY_OK')
for n in range(3, 8):
    fvec, ranks, betti = profiles[n]
    print(f'n={n} f={fvec} boundary_ranks={ranks} betti_F2={betti}')
print('first_mixed_reduced_mod2_homology=n=7 degrees=3,4 ranks=246,7')
