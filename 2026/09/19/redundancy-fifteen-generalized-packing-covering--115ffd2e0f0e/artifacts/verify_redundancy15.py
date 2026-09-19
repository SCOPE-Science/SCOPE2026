from math import comb

RHO = 15
QS = (2, 3, 4, 5, 7, 8)
EXCEPTIONAL = {(3, 4), (3, 5), (4, 5), (4, 6)}


def dimension_cap(q, rho, t, r):
    a = rho - 2 * r + t - 2
    b = rho - 2 * r - 1
    values = []
    for h in range(a + 1, rho + 1):
        num = (q**h - q**(h - a)) * h - b * (q**h - 1)
        den = q**(h - a) - 1
        values.append((num // den, h))
    return min(values)


def reduced_tuples():
    rows = []
    for t in range(3, RHO - 4):
        for r in range(t + 1, (RHO + t - 3) // 2 + 1):
            if 3 * r >= 2 * RHO:
                continue
            if (t, r) in EXCEPTIONAL:
                continue
            for q in QS:
                if q >= r:
                    continue
                K, h = dimension_cap(q, RHO, t, r)
                N = RHO + K
                low_dimension = K <= 5 * t - 2
                binomial_exclusion = comb(N, r) < q ** (t * (RHO - r))
                rows.append(
                    (q, t, r, K, h, N, low_dimension, binomial_exclusion)
                )
    return rows


def pg52_lines():
    points = range(1, 64)
    lines = set()
    for a in points:
        for b in points:
            if a != b:
                lines.add(tuple(sorted((a, b, a ^ b))))
    return sorted(lines)


def ball_volume(Q, n, r):
    return sum(comb(n, i) * (Q - 1) ** i for i in range(r + 1))


rows = reduced_tuples()
survivors = [
    row for row in rows
    if not row[6] and not row[7]
]
assert len(rows) == 62
assert survivors == [(2, 3, 6, 78, 6, 93, False, False)]

lines = pg52_lines()
assert len(lines) == 651
incidence = {p: 0 for p in range(1, 64)}
for line in lines:
    assert len(line) == 3
    for p in line:
        incidence[p] += 1
assert set(incidence.values()) == {31}

# Sharpness of the underlying z=0 line-load inequality:
# double every point in one affine hyperplane coset and use no columns
# on the complementary projective hyperplane.
multiplicity = {
    p: (2 if (p & 32) else 0)
    for p in range(1, 64)
}
assert sum(multiplicity.values()) == 64
assert max(sum(multiplicity[p] for p in line) for line in lines) <= 4

v = ball_volume(8, 73, 6)
target = 2**45
assert v == 20_282_523_983_828
assert target == 35_184_372_088_832
assert v < target

print(f"reduced tuples at rho=15: {len(rows)}")
print("unique survivor:", survivors[0][:6])
print(
    "PG(5,2):",
    f"points={len(incidence)}",
    f"lines={len(lines)}",
    f"lines_per_point={next(iter(set(incidence.values())))}",
)
print("sharp line-load example: total multiplicity=64, maximum line load=4")
print(f"V_8(73,6)={v} < 2^45={target}")
print("PASS")
