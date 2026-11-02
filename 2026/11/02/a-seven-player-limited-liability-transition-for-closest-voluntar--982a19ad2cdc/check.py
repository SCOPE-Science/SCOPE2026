"""Exact-rational checks for symmetric pair-synergy coalition-entry payment flows.

The mathematical proof, including the symbolic one-parameter certificate,
is in RESULT.md. This checker uses only the Python standard library.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations


def rvec(q, n):
    # Normalized pair-synergy game: v(S) = choose(|S|, 2).
    qq = [F(0)] + list(q)
    return [F(k) - k * qq[k] + sum(qq[k + 1:], F(0)) for k in range(n)]


def consent_g(r):
    n = len(r)
    return [r[k] - sum(r[k + 1:], F(0)) / (n - k - 1)
            for k in range(n - 1)]


def matvec(A, x):
    return [sum((aa * xx for aa, xx in zip(row, x)), F(0)) for row in A]


def setup(n):
    m = n - 1
    zero = [F(0)] * m
    c = consent_g(rvec(zero, n))
    basis = []
    for j in range(m):
        e = zero.copy(); e[j] = F(1)
        basis.append([z - y for z, y in zip(consent_g(rvec(e, n)), c)])
    A = [[basis[j][i] for j in range(m)] for i in range(m)]
    w = [F(comb(n, k) * (n - k) * k * (k + 1)) for k in range(1, n)]
    return A, c, w


# A nonnegative multiplier on each binding consent inequality proves global
# optimality of a feasible candidate for the strictly convex quadratic.
EXACT = {
    2: ([F(1, 2)], [0], [F(1)]),
    3: ([F(1, 2), F(1, 2)], [0, 1], [F(9, 2), F(3, 4)]),
    4: ([F(1, 2), F(2, 5), F(3, 5)], [0, 1], [F(66, 5), F(28, 5)]),
    5: ([F(1, 2), F(30, 71), F(45, 142), F(54, 71)],
        [0, 1], [F(2330, 71), F(2985, 142)]),
    6: ([F(1, 2), F(20, 41), F(10, 41), F(12, 41), F(40, 41)],
        [0, 1], [F(3015, 41), F(2388, 41)]),
    7: ([F(1, 2), F(1, 2), F(210, 929), F(168, 929),
         F(280, 929), F(1200, 929)],
        [0, 1, 2], [F(270963, 1858), F(476175, 3716), F(16044, 929)]),
}


def prove_stationarity(A, w, q, active, dual, upper_dual=F(0)):
    n = len(q)
    for j in range(n):
        rhs = sum((dual[i] * A[active[i]][j] for i in range(len(active))), F(0))
        if j == n - 1:
            rhs -= upper_dual
        assert w[j] * q[j] == rhs, (j, w[j] * q[j], rhs)


def direct_dynamic_consent(q, a):
    """Independently replay full-coalition-state uniform-entry Bellman recursion."""
    n = len(q) + 1
    mall = (1 << n) - 1
    u = [[F(0)] * (1 << n) for _ in range(n)]
    checks = 0
    for k in range(n-1, -1, -1):
        for mask in range(1 << n):
            if mask.bit_count() != k:
                continue
            outside = [j for j in range(n) if not (mask >> j) & 1]
            if not outside:
                continue
            for i in range(n):
                outcomes = []
                for j in outside:
                    pay = (a + k * (1 - q[k-1])) if i == j and k else (a if i == j else F(0))
                    if i != j and (mask >> i) & 1:
                        pay = q[k-1]
                    outcomes.append(pay + u[i][mask | (1 << j)])
                u[i][mask] = sum(outcomes, F(0)) / len(outcomes)
                if i in outside and len(outside) >= 2:
                    now = outcomes[outside.index(i)]
                    later = (sum(outcomes, F(0)) - now) / (len(outside)-1)
                    assert now >= later, (mask, i, now, later)
                    checks += 1
    assert all(v == a + F(n-1, 2) for v in (u[i][0] for i in range(n)))
    return checks


def verify_all():
    cases = 0
    inequalities = 0
    for n in range(2, 8):
        A, c, w = setup(n)
        q, active, dual = EXACT[n]
        slacks = [v + cc for v, cc in zip(matvec(A, q), c)]
        assert all(x >= 0 for x in slacks)
        assert all(x == 0 for x in (slacks[i] for i in active))
        assert all(x >= 0 for x in dual)
        prove_stationarity(A, w, q, active, dual)
        assert all(x >= 0 for x in q)
        payments = [F(k) * (1 - q[k - 1]) for k in range(1, n)]
        if n <= 6:
            assert all(x >= 0 for x in payments)
        else:
            assert payments[-1] == -F(1626, 929)
            assert all(x >= 0 for x in payments[:-1])
        inequalities += len(slacks)
        cases += 1

    A, c, w = setup(7)
    for L in [F(1), F(13, 12), F(6, 5), F(5, 4), F(1200, 929)]:
        assert F(1) <= L <= F(1200, 929)
        q = [F(1, 2), F(1, 2), -15*(L-2)/47,
             -12*(L-2)/47, -20*(L-2)/47, L]
        dual = [-3*(3200*L - 8703)/94,
                -175*(128*L - 303)/188,
                -84*(80*L - 113)/47]
        upper_dual = -42*(929*L-1200)/47
        slacks = [v + cc for v, cc in zip(matvec(A, q), c)]
        assert slacks[:3] == [0, 0, 0]
        assert all(x >= 0 for x in slacks + dual + [upper_dual])
        prove_stationarity(A, w, q, [0, 1, 2], dual, upper_dual)
        a = 6*(L-1)
        for k, x in enumerate(q, 1):
            assert F(0) <= x <= 1 + a/k
        D = sum((ww*x*x for ww, x in zip(w, q)), F(0)) / 2
        Dstar = F(1742853, 3716)
        assert D - Dstar == 21*(929*L-1200)**2/F(43663)
        inequalities += len(slacks) + len(q)*2
        cases += 1

    # Independent direct coalition-path check. A full path is a permutation
    # of agents. Under permutation-invariant budget balance, each agent's
    # mean terminal payoff must equal the Shapley value.
    for q, a in [(EXACT[7][0], F(0)),
                 ([F(1, 2), F(1, 2), F(15, 47), F(12, 47), F(20, 47), F(1)], F(0)),
                 (EXACT[7][0], F(2))]:
        n = 7
        result = [F(0)]*n
        for path in permutations(range(n)):
            payoff = [F(0)]*n
            seen = []
            for k, entering in enumerate(path):
                pk = a if k == 0 else a + F(k) * (1-q[k-1])
                payoff[entering] += pk
                if k:
                    for old in seen:
                        payoff[old] += q[k-1]
                seen.append(entering)
            assert sum(payoff) == a*n + F(n*(n-1), 2)
            result = [t + p for t, p in zip(result, payoff)]
        expected = a + F(n-1, 2)
        assert all(x == factorial(n)*expected for x in result)
        cases += 1
    checks = 0
    for n in range(2, 8):
        checks += direct_dynamic_consent(EXACT[n][0], F(0))
    for a, q in [(F(0), [F(1,2), F(1,2), F(15,47), F(12,47), F(20,47), F(1)]),
                 (F(1), [F(1,2), F(1,2), F(55,188), F(11,47), F(55,141), F(7,6)])]:
        # The second vector is rebuilt from its exact L parameter.
        L = 1 + a/F(6)
        q = [F(1,2), F(1,2), 15*(2-L)/47, 12*(2-L)/47, 20*(2-L)/47, L]
        checks += direct_dynamic_consent(q, a)
    print(f'VERIFY_OK cases={cases} exact_inequalities={inequalities} enumerated_paths={3*factorial(7)} direct_consent_states={checks}')

if __name__ == '__main__':
    verify_all()
