"""Exact finite-state checks for random-mapping fixed/cyclic-point laws.

Standard-library only. Run: python verify.py
The asymptotic assertion is proved analytically in RESULT.md; no finite
computation is used as a substitute for that proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, e, factorial


def derangement(m):
    if m == 0:
        return 1
    if m == 1:
        return 0
    a, b = 1, 0
    for r in range(2, m + 1):
        a, b = b, (r - 1) * (a + b)
    return b


def cyclic_count(mapping):
    count = 0
    for start in range(len(mapping)):
        seen = set()
        v = start
        while v not in seen:
            seen.add(v)
            v = mapping[v]
        if v == start:
            count += 1
    return count


def exact_joint_formula(n):
    out = {}
    for k in range(1, n + 1):
        falling = factorial(n) // factorial(n - k)
        q = Fraction(k * falling, n ** (k + 1))
        for j in range(k + 1):
            r = Fraction(comb(k, j) * derangement(k - j), factorial(k))
            out[k, j] = q * r
    return out


def exact_joint_direct(n):
    counts = {}
    for mapping in product(range(n), repeat=n):
        k = cyclic_count(mapping)
        j = sum(mapping[i] == i for i in range(n))
        counts[k, j] = counts.get((k, j), 0) + 1
    return {key: Fraction(value, n**n) for key, value in counts.items()}


def tv_joint_product(joint, n):
    mk = {k: sum(joint.get((k, j), 0) for j in range(n + 1))
          for k in range(1, n + 1)}
    mf = {j: sum(joint.get((k, j), 0) for k in range(1, n + 1))
          for j in range(n + 1)}
    distance = sum(abs(joint.get((k, j), 0) - mk[k] * mf[j])
                   for k in range(1, n + 1) for j in range(n + 1)) / 2
    return distance, mk, mf


def check():
    assertions = 0
    expected_tv = {
        1: Fraction(0),
        2: Fraction(1, 2),
        3: Fraction(109, 243),
        4: Fraction(3235, 8192),
        5: Fraction(686076, 1953125),
        6: Fraction(1194697, 3779136),
    }
    for n in range(1, 7):
        formula = exact_joint_formula(n)
        direct = exact_joint_direct(n)
        for k in range(1, n + 1):
            for j in range(n + 1):
                assert formula.get((k, j), 0) == direct.get((k, j), 0)
                assertions += 1
        distance, mk, mf = tv_joint_product(formula, n)
        assert distance == expected_tv[n]
        assertions += 1
        assert sum(mk.values()) == 1
        assertions += 1
        assert sum(mf.values()) == 1
        assertions += 1
        for j in range(n + 1):
            assert mf[j] == Fraction(comb(n, j) * (n-1)**(n-j), n**n)
            assertions += 1
        for k in range(1, n + 1):
            assert mk[k] == Fraction(k * factorial(n) // factorial(n-k), n**(k+1))
            assertions += 1
        mean_f = sum(j * mf[j] for j in range(n + 1))
        mean_k = sum(k * mk[k] for k in range(1, n + 1))
        mean_fk = sum(k * j * formula.get((k, j), 0)
                      for k in range(1, n + 1) for j in range(n + 1))
        assert mean_f == 1
        assert mean_fk == mean_f * mean_k
        assertions += 2

    for k in range(1, 21):
        # The rencontres law has unit mean and total mass one.
        probs = [Fraction(comb(k, j) * derangement(k-j), factorial(k))
                 for j in range(k+1)]
        assert sum(probs) == 1
        assert sum(j * probs[j] for j in range(k+1)) == 1
        assertions += 2

    # A numerical consistency check of the limiting analytic constant.
    # The finite partial sum uses rencontres masses, not simulated maps.
    import math
    partial = 0.0
    for k in range(1, 25):
        probs = [comb(k, j) * derangement(k-j)/factorial(k)
                 for j in range(k+1)]
        pp = [math.exp(-1)/factorial(j) for j in range(k+60)]
        delta = sum(abs((probs[j] if j <= k else 0)-pp[j])
                    for j in range(k+60))/2
        partial += k*delta
    sharp_sum = (3*e**2+1)/8
    assert abs(partial-sharp_sum) < 1e-7
    assertions += 1
    print(f"PASS: {assertions} exact/finite checks and one numerical asymptotic-constant consistency check")

if __name__ == '__main__':
    check()
