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

# Mathematical verification and scope

The general statement is proved analytically in RESULT.md. The exact three-node determinant comes from the full Gaussian–Fock Gram matrix, not from an approximation, and the interpolation extremum follows from a strict derivative sign argument valid for every positive anchor spacing. The collision expansion is for fixed interior fractional position and is not asserted to be uniform at the boundary fractions.

Reproduce the supplementary test using `python verify.py` after installing the single dependency from `requirements.txt`. Its run completed 431 finite, high-precision geometry, Schur-complement and eigenvalue comparisons, as recorded in `verification_output.txt`. This does not independently certify the all-parameter theorem. No independent scientific audit has been performed.
