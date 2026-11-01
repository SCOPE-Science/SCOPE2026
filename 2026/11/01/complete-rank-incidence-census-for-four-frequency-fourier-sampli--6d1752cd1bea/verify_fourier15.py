"""Exact, exhaustive rank-incidence certificate for the order-15 Fourier matrix.

Run: python3 verify_fourier15.py
Only Python standard library; cyclotomic remainders and all counts use integers.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, gcd

N = 15
PHI = (1,-1,0,1,-1,1,0,-1,1)
UNITS = tuple(a for a in range(N) if gcd(a,N) == 1)
SUBSETS = tuple(combinations(range(N),4))
assert comb(15,4) == len(SUBSETS) == 1365
# x**k mod Phi_15(x), expressed in integral basis 1,...,x**7.
REMAINDERS = []
for k in range(15):
    poly = [0] * (k + 1)
    poly[k] = 1
    for t in range(k, 7, -1):
        coefficient = poly[t]
        for i in range(8):
            poly[t-8+i] -= coefficient * PHI[i]
        poly[t] = 0
    REMAINDERS.append(tuple(poly[i] if i < len(poly) else 0 for i in range(8)))


def minor_zero(rows, cols):
    """True exactly when the corresponding complex Fourier minor vanishes."""
    k = len(rows)
    assert k == len(cols) and 2 <= k <= 4
    polynomial = [0] * N
    for sigma in permutations(range(k)):
        inversions = sum(sigma[i] > sigma[j] for i in range(k) for j in range(i+1,k))
        exponent = sum(rows[i] * cols[sigma[i]] for i in range(k)) % N
        polynomial[exponent] += -1 if inversions % 2 else 1
    return all(sum(polynomial[t] * REMAINDERS[t][j] for t in range(N)) == 0
               for j in range(8))


def minor_rank(rows, cols):
    for k in (4,3,2):
        for a in combinations(rows,k):
            for b in combinations(cols,k):
                if not minor_zero(a,b):
                    return k
    return 1


def orbit_of(subset):
    return frozenset(tuple(sorted((a*x+b) % N for x in subset))
                     for a in UNITS for b in range(N))


def exact_orbits():
    used = set()
    data = []
    for subset in SUBSETS:
        if subset in used:
            continue
        orb = orbit_of(subset)
        assert not (orb & used)
        used.update(orb)
        data.append((subset, tuple(sorted(orb))))
    assert len(used) == len(SUBSETS)
    assert len(data) == 18 and sum(len(orbit) for _, orbit in data) == 1365
    return data


# These 18 row-orbit counts are a small, independently checkable certificate.
EXPECTED = (
    (60, 0, 0), (120, 0, 0), (120, 0, 15), (120, 0, 15),
    (120, 0, 15), (60, 0, 60), (120, 0, 165), (30, 0, 150),
    (120, 0, 150), (120, 0, 75), (60, 0, 45), (60, 0, 75),
    (30, 0, 75), (60, 0, 195), (60, 15, 300), (60, 15, 600),
    (30, 15, 450), (15, 150, 810),
)


def verify():
    orbit_data = exact_orbits()
    counts = Counter()
    matrix = []
    for i, (rows, orb) in enumerate(orbit_data):
        table_row = []
        for j, (_, col_orbit) in enumerate(orbit_data):
            tally = Counter(minor_rank(rows, cols) for cols in col_orbit)
            assert sum(tally.values()) == len(col_orbit)
            table_row.append((tally[2], tally[3], tally[4]))
        matrix.append(table_row)
        row_rank2 = sum(x[0] for x in table_row)
        row_rank3 = sum(x[1] for x in table_row)
        assert (len(orb), row_rank2, row_rank3) == EXPECTED[i], (i, rows, len(orb),row_rank2,row_rank3)
        for rank in (2,3,4):
            counts[rank] += len(orb) * sum(x[rank-2] for x in table_row)
        print(f'{i:2d} {rows!s:18s} orbit={len(orb):3d} '
              f'rank2={row_rank2:3d} rank3={row_rank3:3d} rank4={1365-row_rank2-row_rank3:4d}', flush=True)
    assert counts == Counter({2:4500, 3:161100, 4:1697625}), counts
    assert sum(counts.values()) == 1365**2
    # Transposition symmetry: total pairs across two orbit types is the same in either order.
    for i, (_, oi) in enumerate(orbit_data):
        for j, (_, oj) in enumerate(orbit_data):
            for rank in (2,3,4):
                assert len(oi)*matrix[i][j][rank-2] == len(oj)*matrix[j][i][rank-2]
    print('RANK_TOTALS', dict(sorted(counts.items())))
    print('AFFINE_ORBIT_COUNT', len(orbit_data))
    print('MATRIX_COUNTS rank2/rank3, nonzero entries by row and column orbit')
    for i, row in enumerate(matrix):
        print(i, ' '.join(f'{j}:{x[0]}/{x[1]}' for j,x in enumerate(row) if x[0] or x[1]))
    print('EXACT_CERTIFICATE_OK')


if __name__ == '__main__':
    verify()
