"""Supplementary finite integer tests for a monomial composition-adjoint model.

Run: python verify.py
"""
import math


def successor(j, m, n):
    return m * (j // n) if j % n == 0 else None


def predecessor(j, m, n):
    return n * (j // m) if j % m == 0 else None


def test_incomparable():
    count = 0
    for m, n in [(2, 3), (6, 10), (8, 15), (10, 14), (12, 18)]:
        d = math.gcd(m, n)
        p, q = m // d, n // d
        if p <= 1 or q <= 1:
            continue
        for N in range(0, 12):
            for r in range(1, 50):
                if math.gcd(r, p * q) != 1:
                    continue
                chain = [d * p**a * q**(N-a) * r for a in range(N+1)]
                assert len(chain) == len(set(chain))
                assert predecessor(chain[0], m, n) is None
                assert successor(chain[-1], m, n) is None
                for a in range(N):
                    assert successor(chain[a], m, n) == chain[a+1]
                    assert predecessor(chain[a+1], m, n) == chain[a]
                count += 1
    return count


def test_divisibility():
    count = 0
    for m, n in [(4, 2), (12, 3), (12, 2), (2, 4), (3, 12), (2, 12)]:
        if m % n == 0:
            for r in range(1, 50):
                if r % (m // n) == 0:
                    continue
                j = n * r
                assert predecessor(j, m, n) is None
                for _ in range(10):
                    j = successor(j, m, n)
                    assert j is not None
                    count += 1
        elif n % m == 0:
            for r in range(1, 50):
                if r % (n // m) == 0:
                    continue
                j = m * r
                assert successor(j, m, n) is None
                for _ in range(10):
                    j = predecessor(j, m, n)
                    assert j is not None
                    count += 1
    return count

if __name__ == '__main__':
    x, y = test_incomparable(), test_divisibility()
    print(f'PASS: {x} finite Jordan paths; {y} unilateral path steps.')
