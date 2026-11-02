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

# Reproducible exact verification

Running `python3 verify_flex.py` from this package prints `KLEIN_FLEX_MOD7_21_AT_SINGULARITY_PLUS_3_SIMPLE_OK` on success. It recomputes the Hessian determinant, finite-field resultant, support gcd and transversality, and singular-point gradient. The resultant is an exact polynomial identity, not a finite-point sample. Degree-24 intersection, local length 21 and arithmetic flatness additionally invoke explicit proofs using Bézout and the local criterion for flatness in RESULT.md. No independent external validation has been performed.
