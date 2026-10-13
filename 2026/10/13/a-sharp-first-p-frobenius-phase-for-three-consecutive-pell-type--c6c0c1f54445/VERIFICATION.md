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

# Verification and limits

The theorem is proved by the canonical two-denomination parametrization and the exact formula for lifts to three-denomination representations in `RESULT.md`. No finite census can establish this infinite statement; the algebraic steps in the proof are essential.

Run `python3 verify.py` in the folder containing this file. The standalone checker uses unrestricted integer arithmetic. It performs independent dynamic-programming representation counts for 20 Pell parameter pairs; verifies 12,341 predicted residue crossings, 194 predicted global maxima, and 660 direct representations enumerations. The actual deterministic output is in `verification_output.txt`.

The checker does not inspect every integer parameter, and its success is not independent mathematical certification. Literature priority remains subject to unindexed sources.
