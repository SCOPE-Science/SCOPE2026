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

# Verification instructions

Execute `python3 verify_boundary.py` with Python 3.8 or later and no external packages. The program directly enumerates sample subsets, checks the derived product against direct block boundaries for every integer-partition block profile up to nine points at three rational sampling probabilities, checks inverse reconstruction from exact rational coefficients, and verifies the truncation examples.

The finite checker output for this review was:

`VERIFY_OK partition_bias_cases=291 direct_weighted_subsets=71865 n_up_to=9 p=1/2,1/3,2/5 full_inverse=PASS fixed_n_uniqueness=PASS prefix_sharpness=PASS`

This is evidence for the specified finite tests only. The general uniqueness proof is the nonzero leading-factor induction in `RESULT.md`; the other universal assertions follow by elementary block case analysis and symbolic identities. No external or independent verification has been performed.
