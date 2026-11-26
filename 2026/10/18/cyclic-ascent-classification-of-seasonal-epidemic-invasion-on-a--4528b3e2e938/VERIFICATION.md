---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With one update per coordinate, write x for initial and y for final coordinates of the undamped sweep. Then y=x+Ly+Ux, where L records inputs from already updated coordinates and U records the rest. In recipient-update order L is strictly lower triangular; thus Q=(I−L)⁻¹(I+U) and det(zI−Q)=det((z−1)I−zL−U). Only the diagonal term and the full directed cycle enter the latter determinant, with signs giving (z−1)^n−Pz^k. This verifies multiplicities directly, even at repeated roots and at n=2. Each undamped shear has a nonnegative matrix, and the product dominates the identity plus the weighted directed cycle, so it is primitive and its spectral radius is simple. The positive root above one is unique since the logarithmic derivative of (z−1)^n/z^k is ((n−k)z+k)/(z(z−1))>0 there. Its strict order in k follows by comparing consecutive exponents. The common scalar damping multiplies the whole propagator, so comparison with the unit circle verifies the strict linear stability tests and the simple critical multiplier; it does not decide nonlinear critical behavior. The order-sensitive counterexample to the average passes the stated exact inequalities and the analytic log bound. Fresh exact arithmetic for all 152 orders in dimensions 2–5 supported the polynomial; the original replay was inspected and not run.

## originality

PASS

The distinct supported contribution is the weighted real cyclic-shear spectral reduction and its application to a one-cycle switched system. General ordered-propagator thresholds already exist. The closest exact algebraic statement gives the same statistic for an unweighted binary update and has a closely related determinant argument, but its characteristic-two theorem does not imply the weighted real spectrum. The cyclic Gauss–Seidel sources checked concern different iteration matrices or order restrictions.

## value

PASS

The main exact structural reduction replaces a factorially large schedule family by a single cyclic statistic for the full spectrum in each dimension. The abstract switched-system witness shows why stable snapshots and a stable average are insufficient evidence of period stability. The latter is a useful limitation for preventive modeling, not an empirical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
