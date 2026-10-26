"""Exact exhaustive certification for four-element quasigroups.
Run with: python3 verify.py. Uses only Python standard library.
"""
from itertools import permutations, product
from collections import Counter

N = 4
PERMS = list(permutations(range(N)))


def latin_squares():
    """Enumerate all Latin tables by row permutations with disjoint columns."""
    def add(rows):
        if len(rows) == N:
            yield tuple(c for r in rows for c in r)
        else:
            for p in PERMS:
                if all(p[j] != r[j] for r in rows for j in range(N)):
                    yield from add(rows + (p,))
    return list(add(()))


def relabel(t, p):
    """Conjugate the binary operation by the permutation old -> new."""
    inv = [0] * N
    for old, new in enumerate(p):
        inv[new] = old
    return tuple(p[t[N * inv[i] + inv[j]]]
                 for i in range(N) for j in range(N))


def canonical(t):
    return min(relabel(t, p) for p in PERMS)


def passes_necessary_equations(t):
    """Required counts: P(xy=yx), P(xx=yy), P(xx=x), P(x(xx)=x)."""
    binary_counts = (
        sum(t[N*x+y] == t[N*y+x] for x,y in product(range(N),repeat=2)),
        sum(t[N*x+x] == t[N*y+y] for x,y in product(range(N),repeat=2)),
    )
    unary_counts = (
        sum(t[N*x+x] == x for x in range(N)),
        sum(t[N*x + t[N*x+x]] == x for x in range(N)),
    )
    return (all(v in (4,16) for v in binary_counts)
            and all(v in (1,4) for v in unary_counts))


# F4 = F2[omega] with omega^2=omega+1, elements encoded as 0,1,omega,omega+1.
MUL = ((0,0,0,0), (0,1,2,3), (0,2,3,1), (0,3,1,2))
COEFFICIENTS = ((1,1), (2,1), (1,2), (2,2), (2,3))


def affine_table(a, b):
    return tuple(MUL[a][x] ^ MUL[b][y]
                 for x in range(N) for y in range(N))


def run():
    tables = latin_squares()
    assert len(tables) == 576
    all_classes = Counter(canonical(t) for t in tables)
    assert len(all_classes) == 35
    survivors = [t for t in tables if passes_necessary_equations(t)]
    surviving_classes = Counter(canonical(t) for t in survivors)
    assert len(survivors) == 30
    assert len(surviving_classes) == 5
    assert sorted(surviving_classes.values()) == [2,4,8,8,8]
    affine_classes = {canonical(affine_table(a,b)) for a,b in COEFFICIENTS}
    assert len(affine_classes) == 5
    assert set(surviving_classes) == affine_classes
    for a,b in COEFFICIENTS:
        assert passes_necessary_equations(affine_table(a,b))
    # Non-Latin groupoids: four constant tables; projections x and y;
    # eight one-fixed-point/three-cycle unary permutations in either orientation.
    one_fixed_three_cycle = [p for p in PERMS
                             if sum(p[i] == i for i in range(N)) == 1]
    assert len(one_fixed_three_cycle) == 8
    non_latin_labeled = 4 + 2 + 2*len(one_fixed_three_cycle)
    assert non_latin_labeled == 22
    assert len(survivors) + non_latin_labeled == 52
    print('VERIFY_OK latin=576 latin_isotypes=35 qualifying_latin=30 '
          'qualifying_quasigroup_isotypes=5 non_latin_isotypes=5 '
          'all_isotypes=10 labeled_minimal_groupoids=52')
    print('affine_coefficients=', COEFFICIENTS)
    print('quasigroup_isomorphism_orbits=', sorted(surviving_classes.values()))


if __name__ == '__main__':
    run()
