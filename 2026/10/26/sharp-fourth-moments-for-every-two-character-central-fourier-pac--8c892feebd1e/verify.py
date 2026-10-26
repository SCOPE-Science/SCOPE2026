"""Exact fusion checks and reproducibility tests for two SU(2) characters.

Requires only the Python standard library. Finite tests corroborate the proof.
"""
from collections import defaultdict
import math


def fusion(a, b):
    return range(abs(a - b), a + b + 1, 2)


def direct_fourth(n, m, a, b):
    # Product decomposition is built independently of the proposed fourth-moment formula.
    squared = defaultdict(complex)
    for r, s, coefficient in [(n, n, a * a), (n, m, 2 * a * b), (m, m, b * b)]:
        for degree in fusion(r, s):
            squared[degree] += coefficient
    return sum(abs(coefficient) ** 2 for coefficient in squared.values())


def closed_fourth(n, m, a, b):
    A, B, k = n + 1, m + 1, m - n
    H = max(0, A - k // 2) if k % 2 == 0 else 0
    J = A if k % 2 == 0 else 0
    cross = (a * b.conjugate()).real
    return (A * abs(a) ** 4 + B * abs(b) ** 4
            + 2 * A * abs(a * b) ** 2 + 4 * A * cross ** 2
            + 4 * H * abs(a) ** 2 * cross + 4 * J * abs(b) ** 2 * cross)


def multiply(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return result


def poly_value(coefficients, t):
    answer = 0.0
    for c in reversed(coefficients):
        answer = answer * t + c
    return answer


count = 0
for n in range(12):
    for m in range(n + 1, 21):
        for r, s, u, v in [(-1, 1, 2, -2), (2, 0, 0, 1), (1, 2, 3, 1),
                           (3, -1, 4, -2), (0, 1, 2, 3), (2, 2, -1, 1), (-3, -2, -2, -1)]:
            a, b = complex(r, s), complex(u, v)
            direct, formula = direct_fourth(n, m, a, b), closed_fourth(n, m, a, b)
            assert abs(direct - formula) < 1e-7 * max(1, abs(direct))
            count += 1

# Verify the rational derivative identity by exact integer polynomial arithmetic
# for independently selected A, B, H (including H=0 and H=A).
for A in range(1, 19):
    for B in range(A + 1, 35):
        for H in range(A + 1):
            N = [B, 4 * A, 6 * A, 4 * H, A]
            Nprime = [(i + 1) * N[i + 1] for i in range(4)]
            D, Dprime = [1, 0, 2, 0, 1], [0, 4, 0, 4]
            left = multiply(Nprime, D)
            right = multiply(N, Dprime)
            left += [0] * (len(right) - len(left))
            identity_lhs = [x - y for x, y in zip(left, right)]
            p = [A, 3 * A - B, 3 * (H - A), -2 * A, -H]
            identity_rhs = [4 * v for v in multiply(p, [1, 0, 1])]
            identity_lhs += [0] * (len(identity_rhs) - len(identity_lhs))
            identity_rhs += [0] * (len(identity_lhs) - len(identity_rhs))
            assert identity_lhs == identity_rhs
            count += 1

for n in range(12):
    for m in range(n + 1, 31):
        A, B, k = n + 1, m + 1, m - n
        if k % 2:
            if B < 3 * A:
                u = (3 * A - B) / (5 * A - B)
                optimum = B + (3 * A - B) ** 2 / (5 * A - B)
                assert 0 < u < 1
                actual = closed_fourth(n, m, complex(math.sqrt(u)), complex(math.sqrt(1 - u)))
                assert abs(actual - optimum) < 1e-8 * (optimum + 1)
            else:
                optimum = B
            for j in range(1001):
                u = j / 1000
                val = A * u * u + B * (1 - u) ** 2 + 6 * A * u * (1 - u)
                assert val <= optimum + 1e-8
                count += 1
        else:
            H = max(0, A - k // 2)
            assert 0 <= H <= A
            p = [A, 3 * A - B, 3 * (H - A), -2 * A, -H]
            lo, hi = 0.0, 1.0
            while poly_value(p, hi) >= 0:
                hi *= 2
            for _ in range(120):
                midpoint = (lo + hi) / 2
                if poly_value(p, midpoint) > 0:
                    lo = midpoint
                else:
                    hi = midpoint
            root = (lo + hi) / 2
            def F(t):
                return (A * t**4 + 4 * H * t**3 + 6 * A * t**2
                        + 4 * A * t + B) / (1 + t*t)**2
            optimum = F(root)
            assert optimum > B
            for val in [j / 100 for j in range(1000)] + [float(100 + j * 100) for j in range(200)]:
                assert F(val) <= optimum + 1e-8
                count += 1

assert abs(closed_fourth(0, 2, complex(1 / math.sqrt(5)), complex(2 / math.sqrt(5))) - 21/5) < 1e-12
print('PASS: independent Clebsch-Gordan contractions, exact polynomial derivative, both parity optimizers')
print('PASS assertion groups:', count)
print('PASS examples: (n,m)=(0,1) K=7/3; (0,2) K=21/5; (0,3) K=4')
