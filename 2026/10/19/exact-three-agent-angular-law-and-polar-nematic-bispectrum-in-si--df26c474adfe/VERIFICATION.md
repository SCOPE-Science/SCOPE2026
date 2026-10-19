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

# Verification scope
The analytic proof and all assumptions are in RESULT.md. Execute `python verify.py` with installed `numpy` and `scipy`; the script constructs the finite-state transition generator independently from the formula it checks. The packaged script was executed and passed 400 comparisons, including direct stationary-generator observations for 4- and 8-root angular alphabets and exact rational symbolic-parameter identities.

These computations do not establish the continuous-circle theorem by exhaustive enumeration; that conclusion follows from the explicitly stated generator balance equations. Finite root calculations only test harmonics that do not alias modulo the alphabet size. The all-order, all-\(N\) theorem and first-public-source dating have not been independently audited.
