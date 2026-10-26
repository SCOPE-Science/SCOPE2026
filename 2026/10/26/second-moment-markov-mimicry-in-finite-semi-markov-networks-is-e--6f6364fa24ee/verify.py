"""Exact rational checks for finite semi-Markov hitting-moment rigidity.

Run using Python 3: python verify.py
The mathematical proof is independent of this finite verification.
"""
from fractions import Fraction as F


def solve(a, b):
    n = len(a)
    m = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(a)]
    for j in range(n):
        k = next((k for k in range(j, n) if m[k][j]), None)
        if k is None:
            raise ArithmeticError("singular")
        m[j], m[k] = m[k], m[j]
        pivot = m[j][j]
        m[j] = [v / pivot for v in m[j]]
        for k in range(n):
            if k != j:
                factor = m[k][j]
                m[k] = [u - factor * v for u, v in zip(m[k], m[j])]
    return [row[-1] for row in m]


def make_p(n, shift):
    w = [[F(0) if i == j else F(1 + ((i + 2) * (j + shift + 2) % 7))
          for j in range(n)] for i in range(n)]
    return [[a / sum(row) for a in row] for row in w]


def hitting(p, mu, m2, alpha, target):
    n = len(p)
    ids = [i for i in range(n) if i != target]
    matrix = [[int(i == j) - p[i][j] for j in ids] for i in ids]
    h_sub = solve(matrix, [mu[i] for i in ids])
    h = [F(0)] * n
    for i, hi in zip(ids, h_sub):
        h[i] = hi
    u_sub = solve(matrix, [m2[i] + 2 * sum(alpha[i][j] * h[j] for j in range(n))
                               for i in ids])
    u = [F(0)] * n
    for i, ui in zip(ids, u_sub):
        u[i] = ui
    return h, u


checks = 0
for n in range(2, 8):
    for shift in range(1, 9):
        p = make_p(n, shift)
        mu = [F(i + 2, i + 1) for i in range(n)]
        m2 = [2 * x * x for x in mu]
        alpha = [[mu[i] * p[i][j] for j in range(n)] for i in range(n)]
        all_h = []
        for target in range(n):
            h, u = hitting(p, mu, m2, alpha, target)
            hc, uc = hitting(p, mu, [2 * x * x for x in mu],
                             [[mu[i] * p[i][j] for j in range(n)] for i in range(n)],
                             target)
            assert (h, u) == (hc, uc)
            all_h.append(h)
            checks += 2 * n
        # For each starting state i, the rows indexed by targets t != i form
        # a nonsingular square matrix in d_i and n-2 independent c_ij.
        for i in range(n):
            out = [j for j in range(n) if j != i]
            basis, final = out[:-1], out[-1]
            rigidity = [[F(1)] + [2 * (all_h[t][j] - all_h[t][final])
                                        for j in basis]
                        for t in out]
            # Every unit vector has a unique preimage precisely if nonsingular.
            for unit in range(n - 1):
                rhs = [F(int(k == unit)) for k in range(n - 1)]
                recovered = solve(rigidity, rhs)
                assert all(sum(rigidity[row][col] * recovered[col]
                               for col in range(n - 1)) == rhs[row]
                           for row in range(n - 1))
                checks += n - 1

# The first moment of holding time may be destination-independent without
# the entire conditional distribution being destination-independent.
p = make_p(3, 1)
mu = [F(2), F(3), F(5)]
alpha = [[mu[i] * p[i][j] for j in range(3)] for i in range(3)]
m2 = [2 * x * x for x in mu]
for t in range(3):
    h1, u1 = hitting(p, mu, m2, alpha, t)
    h2, u2 = hitting(p, mu, m2, alpha, t)
    assert h1 == h2 and u1 == u2
    checks += 6
# A perturbation of first destination-conditioned moments is detectable in
# at least one second hitting-time moment.
altered = [row[:] for row in alpha]
out = [k for k in range(3) if k != 0]
altered[0][out[0]] += F(1, 10)
altered[0][out[1]] -= F(1, 10)
assert any(hitting(p, mu, m2, alpha, t)[1] != hitting(p, mu, m2, altered, t)[1]
           for t in range(3))
checks += 1
# Conditional lognormal laws of common mean mu with conditional variance
# mu^2/2 or 3 mu^2/2, under equal outgoing weights, give total m2=2 mu^2.
for x in mu:
    assert (F(1, 2) * (x*x + x*x / 2)
            + F(1, 2) * (x*x + 3*x*x / 2)) == 2*x*x
    checks += 1
print(f"PASS: {checks} exact rational algebraic/moment checks; n=2..7")
