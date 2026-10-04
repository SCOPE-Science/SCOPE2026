from itertools import combinations_with_replacement
from math import comb, prod

def pg_formula(ds):
    c = len(ds)
    S = sum(ds)
    m = S - c - 4
    assert m > 0
    D = prod(ds)
    R = m * m + sum(d * d for d in ds) - c - 4
    num = m * D * R
    assert num % 48 == 0
    return 1 + num // 48

def pg_hilbert(ds):
    c = len(ds)
    S = sum(ds)
    m = S - c - 4
    assert m > 0
    total = 0
    for mask in range(1 << c):
        shift = 0
        bits = 0
        for i, d in enumerate(ds):
            if (mask >> i) & 1:
                shift += d
                bits += 1
        q = m - shift
        if q >= 0:
            total += (-1) ** bits * comb(q + c + 3, c + 3)
    return total

def balanced(c, S):
    q, r = divmod(S, c)
    return tuple([q] * (c - r) + [q + 1] * r)

def extreme(c, S):
    return tuple([2] * (c - 1) + [S - 2 * (c - 1)])

tuple_checks = 0
move_checks = 0
zero_move_types = set()

for c in range(2, 7):
    for ds in combinations_with_replacement(range(2, 11), c):
        if sum(ds) <= c + 4:
            continue
        p = pg_formula(ds)
        assert p == pg_hilbert(ds)
        tuple_checks += 1

        for i in range(c):
            for j in range(i + 1, c):
                if ds[j] - ds[i] < 2:
                    continue

                a, b = ds[i], ds[j]
                delta = b - a - 1
                nd = list(ds)
                nd[i] += 1
                nd[j] -= 1
                nd = tuple(sorted(nd))

                diff = pg_formula(nd) - p
                assert diff >= 0

                # Replay the exact symbolic factorization.
                r = c - 2
                u = a - 2
                t = b - a - 2
                others = [ds[k] for k in range(c) if k not in (i, j)]
                ws = [z - 2 for z in others]
                W = sum(ws)
                factor = (
                    (r - 1) * (r + 4)
                    + 4 * u * (r + u + t)
                    + 2 * t * (r + t + 1)
                    + 2 * W * (r + 2 * u + t + 2)
                    + W * W
                    + sum(w * w for w in ws)
                )

                S = sum(ds)
                m = S - c - 4
                R = m * m + sum(d * d for d in ds) - c - 4
                assert factor == R - 2 * a * b - 2 * delta

                P = 1
                for k, d in enumerate(ds):
                    if k not in (i, j):
                        P *= d
                assert diff * 48 == m * P * delta * factor

                if diff == 0:
                    zero_move_types.add((ds, nd))
                move_checks += 1

expected_zero = {
    ((2, 5), (3, 4)),
    ((3, 5), (4, 4)),
    ((2, 2, 4), (2, 3, 3)),
}
# The bounded scan sees the (2,2,4) move twice because either equal 2 can be selected.
assert {(a, b) for a, b in zero_move_types} == expected_zero

family_checks = 0
tie_records = []
for c in range(2, 8):
    S0 = max(2 * c, c + 5)
    for S in range(S0, S0 + 25):
        fam = [
            ds
            for ds in combinations_with_replacement(range(2, S + 1), c)
            if sum(ds) == S
        ]
        if not fam:
            continue

        vals = [(pg_formula(ds), ds) for ds in fam]
        mn = min(v for v, _ in vals)
        mx = max(v for v, _ in vals)

        assert pg_formula(extreme(c, S)) == mn
        assert pg_formula(balanced(c, S)) == mx

        mins = [ds for v, ds in vals if v == mn]
        maxs = [ds for v, ds in vals if v == mx]
        if len(mins) > 1 or len(maxs) > 1:
            tie_records.append((c, S, mins, maxs))
        family_checks += 1

assert tie_records == [
    (2, 7, [(2, 5), (3, 4)], [(2, 5), (3, 4)]),
    (2, 8, [(2, 6)], [(3, 5), (4, 4)]),
    (3, 8, [(2, 2, 4), (2, 3, 3)], [(2, 2, 4), (2, 3, 3)]),
]

assert pg_formula((2, 5)) == 6
assert pg_formula((3, 4)) == 6
assert pg_formula((2, 6)) == 20
assert pg_formula((3, 5)) == 21
assert pg_formula((4, 4)) == 21
assert pg_formula((2, 2, 4)) == 7
assert pg_formula((2, 3, 3)) == 7

print("VERIFY_OK", tuple_checks, move_checks, family_checks)
