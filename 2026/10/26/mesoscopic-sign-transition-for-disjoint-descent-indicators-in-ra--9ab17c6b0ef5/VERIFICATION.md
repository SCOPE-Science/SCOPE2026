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

The included `check.py` (Python 3 standard library only) was executed successfully. It exhaustively generated every involution of sizes 4 through 11 (48,920 objects), verifying conditional one-point and all two-point descent probabilities for all admissible fixed-point counts. The same script checked coefficient/covariance identities for every admissible fixed-point count for sizes 4 through 100. Total: 3,743 exact rational and integer comparisons.

The unrestricted theorem rests on the Robinson--Schensted/Littlewood identity, Burnside counting, algebraic covariance reduction, strict monotonicity of the cubic, and a rescaling limit. Finite enumeration does not prove statements for untested sizes or originality. The exact covariance statement excludes overlapping comparisons. Scientific priority and independent review remain open.
