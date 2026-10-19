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

# Verification details

`verify.py` was executed after its complete source was prepared. It produced:

`22 diagnostic assertions passed; no claim of computer-assisted exhaustive proof`

The executable checks exact symbolic derivatives of the total concentration and projective coordinate, exact conservation of the stated first integral, the balanced-coordinate derivative, numerical convergence of the two-term peak-time expansion, finite-parameter time-reflection identities, and convergence of the normalized profile for representative positive rates and scales. All checks use source contained in this package; the script requires `sympy` and `mpmath`.

The complete homoclinic statement, two-sided Riccati limit, and uniform compact-scale profile are established analytically in `RESULT.md`. The finite checks are neither exhaustive over parameters nor a replacement for the strict endpoint Laplace argument. No independent audit was performed; priority comparisons remain subject to older-literature access limitations.
