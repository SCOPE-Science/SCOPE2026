---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python verification.py` with a Python 3 standard library. Actual result from the included code is:

`VERIFY_OK urns=1323 cases=9240 parity=49 phases=3`

The program uses exact fractions to define urn masses and 65-decimal-digit square roots and total-variation calculations. It checks all \(N\in\{2,\ldots,50\}\) and \(m\in\{0,\ldots,N\}\), tests the exact parity formulas and monotonicity, tests product and two-point-mixture competitors on rational parameter grids, and visits all three parameter regimes. Its tolerance is \(10^{-54}\) for the parity formula and \(10^{-55}\) for feasible competitors.

These 1,323 urn computations and 9,240 sample comparisons do not exhaust infinitely many parameters or infinitely many mixing measures. The analytic proof uses an \(L^2\) inequality with its equality condition, a convex quadratic projection, the finite-count urn extremal representation, and an elementary monotonicity argument; each is spelled out in `RESULT.md`. The theorem concerns total variation as \(\sup_E|P(E)-Q(E)|\), rather than the doubled convention used in some finite de Finetti literature. No machine-checked formal proof or independent audit is claimed.
