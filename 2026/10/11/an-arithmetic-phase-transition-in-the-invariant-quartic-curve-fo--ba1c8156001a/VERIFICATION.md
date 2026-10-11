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

# Verification

The standalone `artifacts/verify.py` was executed successfully from the extracted science package using `python artifacts/verify.py`; it reported `VERIFY_OK fields=14 Gaussian_integer_fourth_moments=84 local_representation_profiles=14 quadratic_characters=PASS`. Prime fields and quadratic extensions are tested using explicit field arithmetic; all checks on weighted fourth moments use exact Gaussian-integer convolution.

A separate exact symbolic differentiation check confirmed both derivative identities and the constant-input first variation. The proof itself covers every finite field of characteristic greater than three through the standard nondegenerate quadratic-character identity, the distinct linear case in characteristic seven, and a complete one-variable maximization. The finite checks do not prove infinite-parameter coverage. Independent audit and validation have not been performed.
