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

The exact argument in `RESULT.md` is a universal proof for each characteristic greater than three. Execute `python3 verify.py` from the directory containing the two files to reproduce exhaustive projective-point enumerations for 11 prime fields and 3 quadratic extension fields. The verifier uses only the Python standard library and independent polynomial evaluation, not the claimed formula to generate points. Expected output: `VERIFY_OK: 11 prime-field and 3 quadratic-extension sextic/divisor censuses`.

The finite computations do not prove the formula for all primes or extensions: that conclusion uses the birational conic normalization, explicit singular points and branch Frobenius, and inclusion-exclusion. The original curve's characteristic-zero freeness and singularities are established in cited literature rather than independently re-certified here. Independent audit has not been performed.
