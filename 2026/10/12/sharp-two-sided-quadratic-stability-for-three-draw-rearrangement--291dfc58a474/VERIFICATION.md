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

# Verification record

The accompanying standard-library script `verify.py` was executed from its actual packaged directory with `python verify.py`. It returned `VERIFY_OK exact_simplex_cases=12854 independent_expectation_cases=251`.

The script checks both exact deficit/certificate identities, nonnegative rational-grid certificates, uniform and nonuniform extremizers, and independently enumerates three-draw words on smaller alphabets. Rational grids are neither continuum-exhaustive nor a substitute for proof. The algebraic pair identity, cubic Schur identity, positivity, equality classification, and sharpness of coefficients were also reconstructed by direct symbolic expansion in the proof. Independent audit was not performed.
