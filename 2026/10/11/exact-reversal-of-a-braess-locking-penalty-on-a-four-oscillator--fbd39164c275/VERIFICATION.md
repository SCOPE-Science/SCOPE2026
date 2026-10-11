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

The theorem follows from the equilibrium sine-flux identities, explicit Hessian witnesses for every non-cohesive branch, and maximization of a cubic polynomial. These prove the exact threshold for all real edge weights \(a\geq0\), without numerical extrapolation.

Run `python3 verify.py` with the Python standard library to check finite examples and algebraic normalizations. The supplied script passed 526 finite assertions. Finite grid searches cannot certify a global supremum; the monotonicity and explicit critical-point argument in the proof provide that certification. The uncoupled path at threshold is multiply marginal, so no nondegenerate one-dimensional fold theorem is invoked. The numerical crossing is approximate, while its defining polynomial and uniqueness are proved analytically. Independent scientific verification has not been conducted.
