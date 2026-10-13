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

The proof is analytical. The package's standalone `checker.py` verifies probability normalization, mean matching, the two monotonicity chains, strict stop-loss comparisons at each interior integer threshold, and the positive second-moment gap using exact rational arithmetic. Run with `python checker.py`; expected output is `PASS: 11020 exact-rational checks across 551 parameter pairs`. The script covers only the stated finite parameter grid and does not certify any universal claim. The main proof establishes real-parameter, real-threshold inequalities without relying on numerical extrapolation. Independent scientific assessment has not been performed.
