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

The standalone `verify.py` computes exact symbolic affine edge-cut flows for all 16 labeled spanning trees of the four-point complete graph. For each tree it produces a permutation of its three cut magnitudes whose coordinatewise differences from `(t,1-t,1)` are nonnegative affine functions on the whole interval `[0,1]`; both endpoint checks use exact integer arithmetic. A matching tree attains the candidate triple. The independent analytic argument in RESULT.md proves strict monotonicity of the derivative and the all-parameter cusp. Five numerical root evaluations illustrate the theorem but do not prove it.

Run: `python3 verify.py`. Successful replay prints `EXACT_SYMBOLIC_TREE_CERTIFICATE_OK 16 trees` followed by `ALL_CHECKS_OK`.
