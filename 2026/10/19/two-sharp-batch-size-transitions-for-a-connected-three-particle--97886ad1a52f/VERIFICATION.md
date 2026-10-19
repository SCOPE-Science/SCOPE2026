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

The exact stationary generator yields the moments and the rational normalized third connected cumulant; the proof in RESULT.md supplies an explicit all-size positivity certificate, an exact endpoint comparison and a finite exhaustive small-population calculation. The accompanying `verify.py` reconstructs these identities with symbolic polynomial arithmetic, compares exact displayed coefficients, and checks exact rational values for 3 <= N <= 150. Run `python verify.py` after installing the versioned dependency listed in `requirements.txt`.

All displayed factorization and coefficient assertions were run and passed. The finite N check is ancillary; infinite-population generality comes solely from the symbolic identities and coefficient-positive expansion for all nonnegative integer substitution parameters. The source comparison remains subject to the stated residual literature risks. Independent audit and validation have not been performed.
