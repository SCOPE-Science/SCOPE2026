---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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
# Verification and scope

Run `python3 verify.py` in the package directory (standard Python 3.8 or later, no external dependencies). It checks 4096 directed four-vertex pure-triadic edge patterns and computes every Boolean fixed support of each pattern. It compares their union with the iterated core and tests the half-density subsolution inequalities at unit weights and recoveries and common multiplier 4. These are integer tests after clearing the positive denominators. They test Boolean supports and subsolutions, not equilibria computed independently of the proof.

For the five-vertex empty-core example, the checker includes the initial set but not a duplicate final empty layer. It numerically checks each layer's bound at each time from 0 through 100. These examples do not certify a universal theorem; the proof in `RESULT.md` supplies the support and extinction implications.
