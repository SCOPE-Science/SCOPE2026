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

# Verification of the mathematical result

The executable `verify.py` reconstructs exact rational finite-dimensional cases, checks the matrix-variance identity against Frobenius projection, samples symmetric dense matrices and competing directions, and numerically solves the one-dimensional strongly convex dual for general affine quadratics. It also verifies that the displayed rank-two indefinite example has zero conditional variance while the leading active direction retains positive variance. The run uses deterministic seeds; `requirements.txt` lists required packages.

To reproduce: `python -m pip install -r requirements.txt` and `python verify.py`.

These checks test algebraic identities and representative instances. They are **not** exhaustive over real parameters or a substitute for the global proof. Global optimality is established by the spectral upper bound, maximal-eigenspace subgradient and matching equality construction in `RESULT.md`. Priority relative to all published optimization literature is not independently certified.
