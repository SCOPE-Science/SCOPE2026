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

## Reproducibility
Run `python3 verify.py` with Python standard library. The checker reconstructs 306 algebraic inverse identities and 12 high-precision radical-limit comparisons for the three exact rational parameters 5/4, 3/2 and 7/4, and emits `VERIFY_OK parameters=3 inverse_checks=306 branch_limit_checks=12 total_checks= 318`.

## Scope of checks
Finite evaluations test the displayed radical formula, location and asymptotic coefficient only. They do not verify the infinite-dimensional compactness argument, positivity for all real parameters, or historical novelty. These are addressed mathematically in RESULT.md, with literature-comparison limitations documented in REVIEW.md and AUDIT.json. Independent verification has not been performed.
