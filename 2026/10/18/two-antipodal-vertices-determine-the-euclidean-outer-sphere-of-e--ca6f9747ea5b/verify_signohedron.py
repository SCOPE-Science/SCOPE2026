"""Exact-rational checks for the minimum enclosing sphere of cross-polytope monotone-path polytopes.

Run: python verify_signohedron.py
Uses only Python's standard library. Finite tests corroborate, but do not prove, the theorem.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random


def path_average(a, signs):
    """Average of the increasing piecewise-linear path -e_n -> signed e_i -> e_n.

    Integrate each affine segment by the trapezoid rule in projection height,
    dividing by the full projection interval length 2*a[-1].
    """
    n = len(a)
    selected = sorted([(s * a[i], i, s) for i, s in enumerate(signs) if s],
                      key=lambda record: record[0])
    if not selected:
        raise ValueError("A coherent vertex requires an intermediate root")
    previous = (-a[-1], n - 1, -1)
    stages = selected + [(a[-1], n - 1, +1)]
    x = [Q(0) for _ in range(n)]
    for stage in stages:
        dt = stage[0] - previous[0]
        assert dt > 0
        for (_, i, sign) in (previous, stage):
            x[i] += Q(sign) * dt / (4 * a[-1])
        previous = stage
    assert sum(a[i] * x[i] for i in range(n)) == 0
    return x


def validate_profile(a):
    a = tuple(map(Q, a))
    n = len(a)
    assert n >= 2 and 0 < a[0] and all(a[i] < a[i+1] for i in range(n-1))
    R2 = (1 + (a[-2] / a[-1]) ** 2) / 4
    contacts = []
    inspected = 0
    multi = 0
    for s in product((-1, 0, 1), repeat=n-1):
        if not any(s):
            continue
        x = path_average(a, s)
        d2 = sum(z*z for z in x)
        assert d2 <= R2, (a, s, d2, R2)
        if d2 == R2:
            contacts.append(s)
        if sum(q != 0 for q in s) >= 2:
            multi += 1
            assert R2 - d2 >= (a[-1] - a[-2])**2 / (8*a[-1]**2)
        inspected += 1
    expected = [tuple([0]*(n-2) + [-1]), tuple([0]*(n-2) + [1])]
    assert sorted(contacts) == expected, (a, contacts)
    return inspected, multi


def main():
    counts = profiles = multicount = 0
    for n in range(2, 9):
        for a in combinations(range(1, 10), n):
            x, y = validate_profile(a)
            profiles += 1
            counts += x
            multicount += y
    random = Random(201071)
    for n in range(2, 10):
        for _ in range(12):
            nums = sorted(random.sample(range(1, 201), n))
            denoms = sorted(random.sample(range(202, 401), n), reverse=True)
            a = [Q(x, y) for x,y in zip(nums,denoms)]
            # The construction gives strictly increasing rational weights.
            x,y = validate_profile(a)
            profiles += 1
            counts += x
            multicount += y
    print("PASS: profiles", profiles)
    print("PASS: exact coherent vertices", counts)
    print("PASS: multi-intermediate vertices and quantitative clearance", multicount)
    print("PASS: unique antipodal contact pair and zero projection for every vertex")

if __name__ == '__main__':
    main()
