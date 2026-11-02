"""Exact, self-contained finite checks of binary second-order hitting-time identities.

Run: python verify.py
Uses only Python's standard library. Finite tests supplement the general proof.
"""
from fractions import Fraction as F
from itertools import product
import random

STATES = tuple(product((0, 1), repeat=2))


def solve(matrix, rhs):
    """Independent exact Gauss-Jordan solve for a nonsingular linear system."""
    n = len(rhs)
    aug = [[F(x) for x in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((j for j in range(col, n) if aug[j][col]), None)
        assert pivot is not None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for j in range(n):
            if j != col:
                scale = aug[j][col]
                aug[j] = [x - scale * y for x, y in zip(aug[j], aug[col])]
    return [row[-1] for row in aug]


def check(u, v, w, z):
    qs = {(0, 0): u, (0, 1): v, (1, 0): w, (1, 1): z}
    pmat = [[F(0) for _ in STATES] for _ in STATES]
    for i, (a, b) in enumerate(STATES):
        for x in (0, 1):
            j = STATES.index((x, a))
            pmat[i][j] += qs[a, b] if x == 1 else (1 - qs[a, b])
    n = len(STATES)
    # Stationary probabilities, solved independently from the closed formula.
    mat = [[pmat[j][i] - (F(1) if i == j else F(0)) for j in range(n)]
           for i in range(n)]
    mat[-1] = [F(1)] * n
    stationary = solve(mat, [F(0)] * (n - 1) + [F(1)])
    assert all(x > 0 for x in stationary)
    assert sum(stationary) == 1
    marg1 = sum(stationary[i] for i, (a, _) in enumerate(STATES) if a == 1)
    marg0 = 1 - marg1
    # Two hitting-time systems solve the first-step recurrences.
    hitting = {}
    for target in (0, 1):
        hm = [[(F(1) if i == j else F(0)) -
               (pmat[i][j] if STATES[j][0] != target else F(0))
               for j in range(n)] for i in range(n)]
        hitting[target] = solve(hm, [F(1)] * n)
    theta = {(a, b): marg0 * hitting[0][i] + marg1 * hitting[1][i]
             for i, (a, b) in enumerate(STATES)}
    # Entirely separate closed expression from the claimed theorem.
    A = 1 + (1 - v) / u
    B = 1 + w / (1 - z)
    pi1 = B / (A + B)
    pi0 = A / (A + B)
    assert marg1 == pi1 and marg0 == pi0
    h1 = {(0, 0): 1 / u, (0, 1): A,
          (1, 0): 1 + (1 - w) * A, (1, 1): 1 + (1 - z) * A}
    h0 = {(1, 1): 1 / (1 - z), (1, 0): B,
          (0, 0): 1 + u * B, (0, 1): 1 + v * B}
    for i, ab in enumerate(STATES):
        assert hitting[0][i] == h0[ab]
        assert hitting[1][i] == h1[ab]
        assert theta[ab] == pi0 * h0[ab] + pi1 * h1[ab]
    assert theta[0, 0] - theta[0, 1] == pi1 * (u - v)**2 / u
    assert theta[1, 1] - theta[1, 0] == pi0 * (w - z)**2 / (1-z)
    const = len(set(theta.values())) == 1
    assert const == (u == v and w == z)
    if const:
        assert next(iter(theta.values())) == 1 + 1 / (u + 1 - w)
    return 1


def main():
    vals = [F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5)]
    assertions = 0
    for params in product(vals, repeat=4):
        assertions += check(*params)
    rng = random.Random(2026)
    for _ in range(400):
        params = [F(rng.randint(1, 19), 20) for _ in range(4)]
        assertions += check(*params)
    print(f"PASS: {assertions} exact-rational parameter tuples; ")
    print("  stationary four-state solve, two independent hitting-system solves, ")
    print("  all hitting formulas, both signed-square defects and rigidity checked.")


if __name__ == '__main__':
    main()
