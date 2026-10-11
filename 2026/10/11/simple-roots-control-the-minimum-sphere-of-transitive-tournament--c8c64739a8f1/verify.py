#!/usr/bin/env python3
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize

def exact_case(n):
    S = Fraction(n * (n*n - 1), 6)
    lam = [Fraction(i*(n-i), 1) / S for i in range(1, n)]
    assert sum(lam, Fraction(0)) == 1
    assert all(x > 0 for x in lam)

    c = [Fraction(n+1-2*k, 1) / S for k in range(1, n+1)]
    assert sum(c, Fraction(0)) == 0

    recon = [Fraction(0) for _ in range(n)]
    for i, w in enumerate(lam):
        recon[i] += w
        recon[i+1] -= w
    assert recon == c

    norm2 = sum(x*x for x in c)
    assert norm2 == Fraction(2, 1) / S

    R2 = Fraction(2, 1) - Fraction(2, 1) / S
    shells = {}
    for i in range(n):
        for j in range(i+1, n):
            d = j-i
            dot = c[i]-c[j]
            dist2 = Fraction(2, 1) + norm2 - 2*dot
            expected = Fraction(2, 1) - Fraction(4*d-2, 1) / S
            assert dist2 == expected
            shells.setdefault(d, []).append(dist2)

    assert set(shells) == set(range(1, n))
    for d, vals in shells.items():
        assert len(vals) == n-d
        assert len(set(vals)) == 1
    for d in range(1, n-1):
        assert shells[d][0] > shells[d+1][0]
    assert shells[1][0] == R2
    return S, c, R2

for n in range(3, 101):
    exact_case(n)

for n in range(3, 10):
    S, c_exact, R2_exact = exact_case(n)
    V = []
    for i in range(n):
        for j in range(i+1, n):
            v = np.zeros(n)
            v[i] = 1.0
            v[j] = -1.0
            V.append(v)
    V = np.array(V)

    c0 = np.array([float(x) for x in c_exact])
    R20 = float(R2_exact)
    x0 = np.r_[c0, R20 * 1.01 + 1e-6]

    def objective(w):
        return w[-1]

    constraints = [{
        "type": "eq",
        "fun": lambda w: np.sum(w[:-1])
    }]
    for v in V:
        constraints.append({
            "type": "ineq",
            "fun": lambda w, v=v: w[-1] - np.sum((v-w[:-1])**2)
        })

    res = minimize(
        objective,
        x0,
        method="SLSQP",
        constraints=constraints,
        options={"ftol": 1e-12, "maxiter": 5000}
    )
    assert res.success, (n, res.message)
    assert abs(res.fun - R20) < 5e-8, (n, res.fun, R20)
    assert np.max(np.abs(res.x[:-1] - c0)) < 5e-6, (n, res.x[:-1], c0)

print("VERIFY_OK transitive-tournament-MEB n=3..100 exact_shells=yes n=3..9 full_epigraph=yes")
