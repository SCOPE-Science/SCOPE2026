#!/usr/bin/env python3
"""Finite arithmetic and deterministic quantile checks for the stated Cantor theorem.

Only the standard library is required. The universal statements have analytic proofs
in RESULT.md; these computations do not establish them independently.
"""
from fractions import Fraction as Q
from math import isclose


def exact_values(r):
    assert Q(0) < r < Q(1, 2)
    g = 1 - 2*r
    iid = g / 4
    projected = g*g / (4*(1-2*r*r))
    ratio = iid / projected
    assert ratio == (1-2*r*r) / g
    assert iid-projected == r*(1-r)*g/(2*(1-2*r*r))
    assert iid > projected > 0
    for p in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
        # Exact calculation of the dual test function's expectation.
        expected_phi = Q(1, 2) - 2*r*p*(1-p)
        dual = expected_phi-Q(1, 4)
        assert dual == iid + 2*r*(p-Q(1, 2))**2
        assert dual >= iid and (dual == iid) == (p == Q(1, 2))
    # Sum of mass at two endpoints of each gap up to generation K-1.
    for K in (1, 4, 8):
        total_mass = sum((2**k)*g*r**k for k in range(K))
        assert total_mass == 1-(2*r)**K
        total_gap_cost = sum((2**k)*(g*r**k)**2/4 for k in range(K))
        assert projected-total_gap_cost == g*g*(2*r*r)**K/(4*(1-2*r*r))
    return iid, projected, ratio


def fair_cantor_quantile(index, depth, r):
    # Binary dyadic midpoint has precisely 'depth' digits followed by 1, 0,...
    # Their contribution after depth is <= r**depth; using the prefix is enough.
    result = 0.0
    for j in range(depth):
        bit = (index >> (depth-1-j)) & 1
        result += (1-r)*bit*(r**j)
    return result


def quantile_mesh_check(r, depth=14):
    m = 2**depth
    cost = 0.0
    bad_lower = bad_upper = 0
    for k in range(m):
        u = (k + 0.5)/m
        x = fair_cantor_quantile(k, depth, r)
        cost += abs(x-u)/m
        if k < m//2 and x>u+1e-13:
            bad_lower += 1
        if k >= m//2 and x<u-1e-13:
            bad_upper += 1
    # Quantile truncation <= r**depth, midpoint sum error <= 2/m
    tolerance = r**depth + 3/m
    assert abs(cost - (1-2*r)/4) <= tolerance
    assert bad_lower == bad_upper == 0
    return cost, tolerance


def main():
    for r in (Q(1, 10), Q(1, 3), Q(9, 20)):
        iid, support, ratio = exact_values(r)
        cost, tol = quantile_mesh_check(float(r))
        print(f"r={r} iid={iid} support={support} ratio={ratio} "
              f"quantile_mesh={cost:.12f} tolerance={tol:.8g}")
    assert exact_values(Q(1, 3)) == (Q(1, 12), Q(1, 28), Q(7, 3))
    print("PASS: rational identities, gap-cost tails, and finite quantile checks")


if __name__ == '__main__':
    main()
