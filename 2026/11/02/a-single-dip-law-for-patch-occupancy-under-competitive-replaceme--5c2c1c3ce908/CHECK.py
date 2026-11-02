"""Exact rational checks for the reversible-patch invasion threshold theorem.

Uses only the Python standard library. The algebraic proof, not this finite
set of test cases, establishes the arbitrary finite-state result.
"""
from fractions import Fraction as F
import random


def invert(a):
    n = len(a)
    x = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if x[i][j])
        x[j], x[k] = x[k], x[j]
        piv = x[j][j]
        x[j] = [z / piv for z in x[j]]
        for i in range(n):
            if i != j:
                m = x[i][j]
                x[i] = [x[i][k] - m * x[j][k] for k in range(2*n)]
    return [row[n:] for row in x]


def multiply(a, b):
    n, m, p = len(a), len(b), len(b[0])
    return [[sum((a[i][k]*b[k][j] for k in range(m)), F(0))
             for j in range(p)] for i in range(n)]


def stationary(q):
    n = len(q)
    a = [[q[j][i] for j in range(n)] for i in range(n)]
    a[-1] = [F(1)]*n
    z = invert(a)
    return [z[i][-1] for i in range(n)]


def example_chain(rng, n):
    masses = [F(rng.randint(1, 7)) for _ in range(n)]
    conductance = [[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        i = rng.randrange(j)
        conductance[i][j] = conductance[j][i] = F(rng.randint(1, 8))
    for i in range(n):
        for j in range(i+1, n):
            if conductance[i][j] == 0 and rng.random() < 0.35:
                conductance[i][j] = conductance[j][i] = F(rng.randint(1, 5))
    q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                q[i][j] = conductance[i][j]/masses[i]
        q[i][i] = -sum(q[i], F(0))
    pi = [m/sum(masses) for m in masses]
    assert stationary(q) == pi
    assert all(pi[i]*q[i][j] == pi[j]*q[j][i]
               for i in range(n) for j in range(n))
    return q, pi


def checks(q, pi, b, v):
    n = len(q)
    a = [[(b if i == j else F(0)) - q[i][j]
          for j in range(n)] for i in range(n)]
    r = invert(a)
    r2 = multiply(r, r)
    r3 = multiply(r2, r)
    h = b*r[0][0]
    h1 = r[0][0] - b*r2[0][0]
    h2 = -2*r2[0][0] + 2*b*r3[0][0]
    assert 0 < h < 1 and h1 > 0 and h2 < 0
    vacancy = v*h/(v+b)
    aug = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            aug[i][j] = q[i][j] - (b if i == j else F(0))
        aug[i][n] = b
    aug[n][0] = v
    aug[n][n] = -v
    stat = stationary(aug)
    assert stat[0] == vacancy
    assert stat[n] == b/(v+b)
    return h, h1, h2, vacancy


def run():
    rng = random.Random(382017)
    count = 0
    for n in range(2, 7):
        for _ in range(12):
            q, pi = example_chain(rng, n)
            bigpi = [[pi[j] for j in range(n)] for i in range(n)]
            a = [[bigpi[i][j]-q[i][j] for j in range(n)] for i in range(n)]
            tau = invert(a)[0][0] - pi[0]
            assert tau > 0
            for v in [F(1, 2), F(3), F(11)]:
                previous = None
                for b in [F(1, 5), F(2, 3), F(1), F(4), F(9)]:
                    h, h1, h2, vac = checks(q, pi, b, v)
                    factor = (b+v)*h1-h
                    if previous is not None:
                        assert factor < previous
                    previous = factor
                    count += 1
                # The exact threshold for initial decrease in occupancy.
                initial_slope_sign = v*tau-pi[0]
                assert (initial_slope_sign > 0) == (v > pi[0]/tau)
    # Exact, nontrivial two-resident-state example: 0->1 = 1, 1->0 = 1.
    q = [[F(-1), F(1)], [F(1), F(-1)]]
    pi = [F(1, 2), F(1, 2)]
    v = F(10)
    assert v*F(1, 4)-pi[0] > 0
    assert checks(q, pi, F(2), v)[-1] == F(5, 8)
    assert checks(q, pi, F(1), v)[-1] < F(5, 8)
    assert checks(q, pi, F(3), v)[-1] < F(5, 8)
    assert F(1)-F(5, 8) == F(3, 8)
    # Algebraic threshold root for arbitrary a,u,v in two-resident model.
    for a, u, v in [(F(1),F(1),F(10)), (F(2),F(3),F(20)),
                    (F(3),F(4),F(1))]:
        # Stationary formula directly from the three-state balance equations.
        for b in [F(1, 7), F(1), F(5)]:
            q = [[-a, a], [u, -u]]
            pi = [u/(a+u), a/(a+u)]
            assert checks(q, pi, b, v)[-1] == v*(u+b)/((v+b)*(a+u+b))
            count += 1
    print('PASS: %d exact rational joint-stationary/resolvent/strict-concavity comparisons' % count)
    print('PASS: two-state sharp minimum b=2, vacancy=5/8, occupancy=3/8')
    print('PASS: analytic proof in RESULT.md covers every finite reversible background')


if __name__ == '__main__':
    run()
