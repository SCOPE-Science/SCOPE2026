"""Exact finite checks for the sharp parity-mode theorem.

Run: python verify_modal.py
All coefficients remain unnormalized integers; scaling does not change modes.
These checks are supplementary to the proof for arbitrary real probabilities.
"""
from itertools import product
from random import Random


def coefficients(triples):
    a = [1]
    for L, T, W in triples:
        b = [0] * (len(a) + 2)
        for j, val in enumerate(a):
            b[j] += L * val
            b[j + 1] += T * val
            b[j + 2] += W * val
        a = b
    return a


def check_modes(a, strict=True):
    p = a[::2]
    q = a[1::2]
    if not any(p) or not any(q):
        return False
    ip = [i for i, v in enumerate(p) if v == max(p)]
    iq = [i for i, v in enumerate(q) if v == max(q)]
    if strict:
        assert all(i-j in (0, 1) for i in ip for j in iq), (a, ip, iq)
    else:
        assert all(abs(i-j-0.5) <= 1.5 for i in ip for j in iq), (a, ip, iq)
    return max(abs(i-j-0.5) for i in ip for j in iq)


def check_ratio(a, strict=True):
    p = a[::2]
    q = a[1::2]
    n = len(q)
    for k in range(n-1):
        # Strict interlacing of successive coefficient ratios.
        if strict:
            assert p[k+1] * q[k] > q[k+1] * p[k], (a,k,'left')
            assert q[k+1] * p[k+1] > p[k+2] * q[k], (a,k,'right')
        else:
            assert p[k+1] * q[k] >= q[k+1] * p[k], (a,k,'left')
            assert q[k+1] * p[k+1] >= p[k+2] * q[k], (a,k,'right')


def main():
    strict_tests = 0
    for n in range(1, 7):
        choices = [(L, T, 5-L-T)
                   for L in range(1, 4) for T in range(1, 4)
                   if 5-L-T >= 1]
        for triples in product(choices, repeat=n):
            a = coefficients(triples)
            assert check_modes(a) == 0.5
            check_ratio(a)
            strict_tests += 1
    rng = Random(20261014)
    for _ in range(5000):
        n = rng.randint(1, 14)
        triples = [(rng.randint(1, 20), rng.randint(1, 20), rng.randint(1, 20))
                   for j in range(n)]
        a = coefficients(triples)
        assert check_modes(a) == 0.5
        check_ratio(a)
        strict_tests += 1
    boundary_tests = 0
    boundary_max = 0.0
    choices = [(L, T, 4-L-T)
               for L in range(5) for T in range(5-L)]
    for n in range(1, 5):
        for triples in product(choices, repeat=n):
            a = coefficients(triples)
            if not any(a[::2]) or not any(a[1::2]):
                continue
            distance = check_modes(a, strict=False)
            check_ratio(a, strict=False)
            if distance is not False:
                boundary_tests += 1
                boundary_max = max(boundary_max, distance)
    witness = coefficients([(0, 1, 3), (2, 0, 2)])
    assert witness == [0, 2, 6, 2, 6]
    assert check_modes(witness, strict=False) == 1.5
    print(f'PASS: {strict_tests} strictly-positive exact coefficient tests, '
          f'{boundary_tests} boundary exploratory mode tests '
          f'(maximum observed distance {boundary_max}); '
          'all exact integer arithmetic')


if __name__ == '__main__':
    main()
