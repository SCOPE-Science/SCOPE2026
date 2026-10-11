#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import linprog, minimize_scalar

for n in range(2, 41):
    rootn = math.sqrt(n)
    for r in range(1, n):
        # Closed inradius formula.
        low_inner = 2*r <= n + rootn + 1e-12
        if low_inner:
            cin = r/(n + rootn)
            rin = cin
        else:
            cin = 0.5
            rin = 0.5

        # Full inradius LP in variables c_1,...,c_n,rho.
        obj = np.r_[np.zeros(n), -1.0]
        A = []
        b = []

        # x_i >= rho.
        for i in range(n):
            row = np.zeros(n+1)
            row[i] = -1.0
            row[-1] = 1.0
            A.append(row)
            b.append(0.0)

        # x_i <= 1-rho are genuine facets exactly when r >= 2.
        if r >= 2:
            for i in range(n):
                row = np.zeros(n+1)
                row[i] = 1.0
                row[-1] = 1.0
                A.append(row)
                b.append(1.0)

        # Rank-facet clearance: sum c_i + sqrt(n) rho <= r.
        row = np.zeros(n+1)
        row[:n] = 1.0
        row[-1] = rootn
        A.append(row)
        b.append(float(r))

        lp = linprog(
            obj,
            A_ub=np.array(A),
            b_ub=np.array(b),
            bounds=[(None,None)]*n + [(0.0,None)],
            method="highs",
        )
        assert lp.success, (n, r, lp.message)
        assert abs(lp.x[-1]-rin) < 2e-9, (n, r, lp.x[-1], rin)
        assert np.max(np.abs(lp.x[:n]-cin)) < 2e-8, (n, r, lp.x[:n], cin)

        # Tangency phase.
        lower = cin
        rank_clearance = (r - n*cin)/rootn
        assert abs(min(lower, rank_clearance, (1-cin if r >= 2 else 1e9)) - rin) < 2e-12
        if 2*r < n + rootn - 1e-12:
            assert abs(lower-rin) < 2e-12
            assert abs(rank_clearance-rin) < 2e-12
            if r >= 2:
                assert 1-cin > rin
        elif 2*r > n + rootn + 1e-12:
            assert r >= 2
            assert abs(lower-rin) < 2e-12
            assert abs((1-cin)-rin) < 2e-12
            assert rank_clearance > rin
        else:
            assert r >= 2
            assert abs(lower-rin) < 2e-12
            assert abs((1-cin)-rin) < 2e-12
            assert abs(rank_clearance-rin) < 2e-12

        # Closed minimum-enclosing formula.
        if 2*r < n:
            cout = r/n
            Rout2 = r*(n-r)/n
        else:
            cout = 0.5
            Rout2 = n/4

        # Evaluate all vertex layers exactly at the claimed center.
        vals = [n*cout*cout + k*(1-2*cout) for k in range(r+1)]
        assert abs(max(vals)-Rout2) < 2e-12
        if 2*r < n:
            assert vals[-1] == max(vals)
            assert all(vals[k] < vals[-1] for k in range(r))
        else:
            assert max(vals)-min(vals) < 2e-12

        # Independent scalar minimization of the exact outer objective.
        def outer_obj(t):
            vals = [n*t*t + k*(1-2*t) for k in range(r+1)]
            return max(vals)

        num = minimize_scalar(
            outer_obj,
            bounds=(-0.25, 1.25),
            method="bounded",
            options={"xatol": 1e-13},
        )
        assert abs(num.fun-Rout2) < 1e-6*max(1.0,Rout2), (n, r, num.fun, Rout2)
        assert abs(num.x-cout) < 1e-5, (n, r, num.x, cout)

print("VERIFY_OK uniform-independence-radii n=2..40 all-ranks=yes full_inradius_lp=yes outer_minimax=yes")
