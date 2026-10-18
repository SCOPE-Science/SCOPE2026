"""Independent finite-dimensional checks of uniform periodic hat-spline slope gain.

Uses standard-library exact rational matrices, not a symbolic algebra dependency.
Finite tests do not replace the analytic asymptotic proof.
"""
from fractions import Fraction
from math import sqrt

Q = 2 - sqrt(3)
LIMIT = (9 - sqrt(3)) / 2
count = 0

def require(condition, message):
    global count
    if not condition:
        raise AssertionError(message)
    count += 1

def invert(matrix):
    n = len(matrix)
    augmented = [[Fraction(matrix[i][j]) for j in range(n)]
                 + [Fraction(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        diagonal = augmented[col][col]
        require(diagonal != 0, f"singular pivot at {n}:{col}")
        augmented[col] = [x / diagonal for x in augmented[col]]
        for row in range(n):
            if row != col:
                multiplier = augmented[row][col]
                if multiplier:
                    augmented[row] = [x - multiplier * y for x, y in
                                      zip(augmented[row], augmented[col])]
    return [row[n:] for row in augmented]

def integrate_abs_affine(left, right):
    if left * right >= 0:
        return (abs(left) + abs(right)) / 2
    return (left * left + right * right) / (2 * (abs(left) + abs(right)))

def exact_gain(n):
    matrix = [[4 if col == row else
               1 if col == (row + 1) % n or col == (row - 1) % n else 0
               for col in range(n)] for row in range(n)]
    inverse = invert(matrix)
    for i in range(n):
        for j in range(n):
            require(sum(Fraction(matrix[i][k]) * inverse[k][j]
                        for k in range(n)) == Fraction(i == j),
                    f"inverse failure {n}:{i}:{j}")
    nodal_slopes = [6 * (inverse[1][j] - inverse[0][j]) for j in range(n)]
    require(sum(nodal_slopes) == 0, f"constant input not annihilated: {n}")
    gain = sum((integrate_abs_affine(nodal_slopes[j],
                                       nodal_slopes[(j + 1) % n])
                for j in range(n)), Fraction(0))
    return nodal_slopes, gain

def cyclic_green_formula(n):
    t = -Q
    return [sqrt(3) * (1 + Q) * (t ** (j - 1) - t ** (n - j)) /
            (1 - t ** n) for j in range(1, n + 1)]

for n in range(3, 22):
    slopes, gain = exact_gain(n)
    calculated = cyclic_green_formula(n)
    for j in range(1, n + 1):
        require(abs(float(slopes[j % n]) - calculated[j - 1]) < 3e-10,
                f"periodic Green inverse disagrees {n}:{j}")
    magnitudes = [abs(float(slope)) for slope in slopes]
    for j in range(n):
        require(slopes[j] * slopes[(j + 1) % n] <= 0,
                f"adjacent slopes should have opposing signs {n}:{j}")
    finite_formula = sum((magnitudes[j] ** 2 + magnitudes[(j + 1) % n] ** 2)
                         / (2 * (magnitudes[j] + magnitudes[(j + 1) % n]))
                         for j in range(n))
    require(abs(float(gain) - finite_formula) < 1e-9,
            f"finite gain formula disagrees {n}")
    require(0 < float(gain) < LIMIT, f"sharp infinite bound failed {n}")
    if n >= 10:
        require(LIMIT - float(gain) < 7 * Q ** (n // 2),
                f"sampled exponential bound failed {n}")
    if n <= 5:
        print(f"n={n}, C_n={gain}, decimal={float(gain):.12f}")

require(exact_gain(3)[1] == Fraction(3), "C3")
require(exact_gain(4)[1] == Fraction(27, 8), "C4")
require(exact_gain(5)[1] == Fraction(192, 55), "C5")
require(abs(LIMIT - 3.6339745962155616) < 1e-12, "limit")
print(f"PASS: {count} finite deterministic assertions; limiting constant {LIMIT:.15f}")
