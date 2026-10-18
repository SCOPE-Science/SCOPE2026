"""Exact pure-Python certificate for a quartic line-cover computation."""
from collections import Counter
Q = 25

def add(a, b):
    return ((a % 5 + b % 5) % 5) + 5 * ((a // 5 + b // 5) % 5)

def mul(a, b):
    x, y = a % 5, a // 5
    z, w = b % 5, b // 5
    return ((x * z + 2 * y * w) % 5) + 5 * ((x * w + y * z) % 5)

def power(x, n):
    r = 1
    for _ in range(n):
        r = mul(r, x)
    return r

def field_points():
    return [(1, a, b) for a in range(Q) for b in range(Q)] + [(0, 1, b) for b in range(Q)] + [(0, 0, 1)]

def eval_quartic(P):
    x, y, z = P
    sq = (power(x, 2), power(y, 2), power(z, 2))
    fourth_sum = add(add(power(x, 4), power(y, 4)), power(z, 4))
    mixed = add(add(mul(sq[0], sq[1]), mul(sq[1], sq[2])), mul(sq[2], sq[0]))
    return add(fourth_sum, mul(11, mixed))

def dot(L, P):
    return add(add(mul(L[0], P[0]), mul(L[1], P[1])), mul(L[2], P[2]))

WITNESS = (
    (1, 0, 11), (1, 1, 13), (1, 2, 1), (1, 2, 3),
    (1, 5, 8), (1, 8, 5), (1, 10, 21), (1, 11, 8),
    (1, 13, 19), (1, 15, 15), (1, 16, 6), (1, 19, 0),
    (1, 19, 13), (1, 23, 3),
)

# Each row gives the four affine (Y,Z) pairs with X=1 on its witness line.
WITNESS_AFFINE = (
    ((9,23),(11,23),(19,23),(21,23)),
    ((19,7),(21,10),(23,9),(24,16)),
    ((10,9),(11,7),(14,6),(24,11)),
    ((5,8),(9,7),(22,20),(23,21)),
    ((11,6),(13,18),(14,24),(21,15)),
    ((6,11),(15,21),(18,13),(24,14)),
    ((6,14),(12,17),(22,5),(23,19)),
    ((8,5),(10,21),(11,24),(17,12)),
    ((6,16),(15,9),(19,24),(20,8)),
    ((6,19),(12,13),(13,12),(19,6)),
    ((9,10),(17,18),(20,22),(21,7)),
    ((7,9),(7,11),(7,19),(7,21)),
    ((8,20),(9,15),(16,6),(24,19)),
    ((5,22),(16,24),(18,17),(23,11)),
)


def main():
    V = field_points()
    assert len(V) == 651 and len(set(V)) == 651
    assert len(set(WITNESS)) == 14
    independent_witness = []
    for L, block in zip(WITNESS, WITNESS_AFFINE):
        assert len(block) == 4
        for y,z in block:
            P = (1,y,z)
            assert eval_quartic(P) == 0
            assert dot(L,P) == 0
            independent_witness.append(P)
    assert len(independent_witness) == 56
    assert len(set(independent_witness)) == 56
    # Hasse--Weil for smooth genus 3 over F_25 gives at most 25+1+6*5=56.
    assert mul(5, 5) == 2
    assert add(add(mul(11, 11), mul(3, 11)), 3) == 0  # c^2-2c+3
    C = [P for P in V if eval_quartic(P) == 0]
    assert len(C) == 56
    assert set(C) == set(independent_witness)
    spectrum = Counter()
    per_point = {k: [0] * len(C) for k in (1, 2, 4)}
    for L in V:
        members = [i for i, P in enumerate(C) if dot(L, P) == 0]
        k = len(members)
        spectrum[k] += 1
        if k in per_point:
            for i in members:
                per_point[k][i] += 1
    assert set(per_point[1]) == {3}
    assert set(per_point[2]) == {7}
    assert set(per_point[4]) == {16}
    assert spectrum == {0: 63, 1: 168, 2: 196, 4: 224}
    assert sum(k*v for k,v in spectrum.items()) == 56*26
    assert sum(k*(k-1)//2 *v for k,v in spectrum.items()) == 56*55//2
    seen = set()
    for L in WITNESS:
        indexes = {i for i,P in enumerate(C) if dot(L,P) == 0}
        assert len(indexes) == 4, (L, len(indexes))
        assert not seen.intersection(indexes), L
        seen |= indexes
    assert len(seen) == 56
    assert len(WITNESS) * 4 == 56
    print('PASS: smoothness addressed algebraically in RESULT.md; curve points 56; line spectrum',dict(sorted(spectrum.items())))
    print('PASS: every curve point is on 3 unisecants, 7 bisecants, 16 quadrisecants.')
    print('PASS: 14 distinct rational 4-secants partition all 56 rational curve points; Bezout proves optimality.')

if __name__ == '__main__':
    main()
