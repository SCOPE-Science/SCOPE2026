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

# Reproducibility

Run `python3 verify.py` with SymPy installed. This reconstructs the stationary and corrector identities, integrates the stationary mean correction and variance brackets, and compares the centered and raw coefficients with the expression printed in Eq. (26) of arXiv:2406.07142v2. The script also checks the Taylor expansion and centered coefficient for the one-way renewal limit. These are exact algebraic checks, not a verification of the stochastic or ergodic limit theorems; those steps are given in the proof.
