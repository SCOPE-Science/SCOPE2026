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

`verify.py` is a standalone Python 3 standard-library checker. Execute `python3 verify.py` from the extracted package directory. It reports `PASS exact rational angle parameterizations: 2485` and ends in `VERIFICATION_OK` after checking the angle-dependent GMRES normal equation, exact squared-error and residual ratios, strict inequalities, and determinant of the first two Krylov vectors for rational Pythagorean parameterizations. It also checks the algebraic maximizing parameter and 9,999 numerical grid points. No external dependency, network access, or other artifact is required.

The exact matrix identities, rational-function differentiation and sign analysis, rather than finite enumeration, prove the continuum statement for all admissible angles. Full two-step GMRES termination and strict failure of finite-iteration alternating-projection termination follow from an explicit nonzero determinant and a closed form for powers of the projection product. The checker is corroborative only. No independent audit or external certification was performed.
