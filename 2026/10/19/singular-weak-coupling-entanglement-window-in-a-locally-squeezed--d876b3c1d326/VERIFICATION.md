---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The exact square identity in `RESULT.md` proves the bound, its unique equality condition for finite positive squeezing, and the strict finite-squeezing entanglement criterion. The stationary model, covariance convention, and eigenvalue formula follow from the cited phase-locked squeezed-bath solution.

The retained checker `python verify.py`, with dependencies in `requirements.txt`, includes finite numerical checks of the stationary covariance, its partial-transpose symplectic eigenvalues and the optimal value at selected squeezing levels, as well as auxiliary checks outside the statement in `RESULT.md`. The checker is not a proof of parameter-uniform inequalities.
