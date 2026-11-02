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

Run `python verify.py` using Python 3.10+ and `sympy>=1.10`. The script independently computes all eight cyclic coefficients of the rational matrix map modulo the cycle equation, verifies every exact numerator and the positive denominator, checks the Descartes sign-variation and rational isolation needed for the global proof, and uses direct rational matrix inversions at ten test timesteps to check row sums and signs.

The analytical argument in `RESULT.md` establishes the all-real-positive-step necessity and sufficiency. The ten finite matrix tests do not establish a continuum theorem and are not claimed as exhaustive. The script computes with exact rationals; reported decimal endpoints are descriptive approximations, not the certificates. No independent mathematical audit has been performed.
