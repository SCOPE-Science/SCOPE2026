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

The supplied `verify.py` is a reproducible exact-arithmetic cross-check. It independently forms the full weighted Gram matrix of the affine basis, computes its inverse, and compares every absolute row sum with the two analytic formulas on 46 rational parameter profiles covering dimensions 3 through 9 (1,061 row instances). Separate SymPy simplifications check the symbolic derivatives, equality at the proposed optimum, and the determinant stationary identity.

To execute: `python verify.py` with Python 3 and SymPy installed. The analytic argument in RESULT.md proves the all-dimension theorem; finite checks are not a substitute. Independent scientific audit has not been performed.
