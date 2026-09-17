#!/usr/bin/env python3
"""Reproducible checks for the SCOPE run 2026-09-17.

Main theorem audited in the accompanying report:
For every k>=2, the exact minimum-degree threshold within bipartite graphs
for strong 1/k-majority edge-colourability with k+1 colours is k^2+1.

This script performs:
  (1) exhaustive arithmetic checks of the ceiling inequality used in the upper bound;
  (2) algebraic checks of the one-colour extremal bound used for K_{k^2,k^2+1};
  (3) optional MILP maximization of a single colour class under the local strong-majority
      constraints, for small k, if SciPy is installed.

The proof itself is symbolic; these computations are supplementary checks, not substitutes.
"""

from __future__ import annotations
import argparse
import math


def M(k: int) -> int:
    return k**3 - k**2 + k


def check_upper_arithmetic(kmax: int = 100, extra: int = 500) -> None:
    for k in range(2, kmax + 1):
        d0 = k*k + 1
        for d in range(d0, d0 + extra + 1):
            lhs = math.ceil(d / (k + 1))
            rhs = (d - 1) / k
            assert lhs <= rhs + 1e-12, (k, d, lhs, rhs)
        # Check sharpness of the arithmetic threshold: d=k^2 fails.
        d = k*k
        assert math.ceil(d / (k + 1)) > (d - 1) / k
    print(f"Upper-bound arithmetic verified for 2<=k<={kmax} and {extra+1} degrees per k.")


def check_extremal_algebra(kmax: int = 1000) -> None:
    for k in range(2, kmax + 1):
        m = M(k)
        # Easy one-sided-high cases.
        assert k*k*(k-1) <= m
        assert (k*k+1)*(k-1) <= m
        # Both sides high, all high degrees exactly k: at most k high vertices on X.
        assert k*k*(k-1) + k == m
        # A degree-(k+1) high vertex on X.
        bx = (k+1)*k + (k*k-k)*(k-2)
        assert bx <= m
        # A degree-(k+1) high vertex on Y.
        by = (k+1)*k + (k*k-k-1)*(k-2)
        assert by <= m
        # Capacity contradiction with k+1 colours.
        total_capacity = (k+1)*m
        total_edges = k*k*(k*k+1)
        assert total_capacity < total_edges
    print(f"Extremal algebra verified for 2<=k<={kmax}.")


def milp_single_colour(k: int, time_limit: float = 10.0) -> None:
    try:
        import numpy as np
        from scipy.optimize import milp, LinearConstraint, Bounds
        from scipy.sparse import lil_matrix, csr_matrix
    except Exception as e:
        print("SciPy MILP unavailable:", e)
        return

    a = k*k
    b = k*k + 1
    n = a*b
    # x_xy=1 means edge xy belongs to one fixed colour class H.
    # For every edge xy of the ambient complete bipartite graph:
    #   d_H(x)+d_H(y)-2*x_xy <= 2k-1.
    A = lil_matrix((n, n), dtype=float)
    ub = np.full(n, 2*k-1.0)
    row = 0
    for x in range(a):
        for y in range(b):
            for yy in range(b):
                A[row, x*b + yy] += 1.0
            for xx in range(a):
                A[row, xx*b + y] += 1.0
            A[row, x*b + y] -= 2.0
            row += 1

    res = milp(
        -np.ones(n),
        integrality=np.ones(n),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(csr_matrix(A), -np.inf, ub),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )
    best = None if res.fun is None else -float(res.fun)
    print(f"k={k}: solver status={res.status}; best found={best}; theorem bound M(k)={M(k)}")
    if getattr(res, "mip_dual_bound", None) is not None:
        print(f"  MILP upper bound from solver={-float(res.mip_dual_bound)}; gap={getattr(res, 'mip_gap', None)}")
    if res.status == 0:
        assert round(best) == M(k), (best, M(k))
        print("  Solver independently certified the exact one-colour maximum.")
    else:
        print("  Time limit/nonoptimal status: this run is evidence only, not a certificate.")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--kmax", type=int, default=100)
    p.add_argument("--milp", type=int, default=None, help="optionally solve one-colour MILP for this k")
    p.add_argument("--time-limit", type=float, default=10.0)
    args = p.parse_args()
    check_upper_arithmetic(args.kmax)
    check_extremal_algebra(max(args.kmax, 100))
    if args.milp is not None:
        if args.milp < 2:
            raise SystemExit("--milp k requires k>=2")
        milp_single_colour(args.milp, args.time_limit)


if __name__ == "__main__":
    main()
