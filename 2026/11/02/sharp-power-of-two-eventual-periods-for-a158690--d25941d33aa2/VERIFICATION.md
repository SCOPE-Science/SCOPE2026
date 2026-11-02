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

# Reproducible verification

Run `python3 verify.py` with the Python standard library. It checks the modulo-32 coefficients and eight residue classes, plus exact integer evaluations of the half-period difference for exponent levels 5 through 10. The independent arithmetic checks are finite; all-exponent validity follows from the proved binomial congruence and Stirling truncation in `RESULT.md`.

The finite exact certificate is the modulo-32 coefficient vector `(1,1,2,7,1,5,11,30)`, the inclusion-exclusion weights `(4,23,16,19,19,25,25,30)`, and the residue cycle `(31,17,31,1,31,17,31,1)` on indices 5 through 12. The OEIS initial sequence values provide a separate normalization check. The verifier must print `VERIFY_OK` and terminate without assertion errors. No independent mathematical audit has been performed.
