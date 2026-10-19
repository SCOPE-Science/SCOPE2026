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

The proof uses a pathwise logarithmic comparison against one geometric Brownian envelope, an absorbing Brownian first-passage formula, and total-variation support separation. The numerical checker in `verify.py` independently integrates the first-passage density for four parameter sets and compares against the two-normal closed form. All displayed examples are illustrative only; their agreement does not certify the universal quantifiers in the theorem.

The terminal probability lower bound is attained by full transmission suppression with maximal treatment in the specified persistent-noise model. It is not claimed for a model whose noise disappears when transmission is suppressed, nor for a finite-count epidemic. No independent audit was performed.
