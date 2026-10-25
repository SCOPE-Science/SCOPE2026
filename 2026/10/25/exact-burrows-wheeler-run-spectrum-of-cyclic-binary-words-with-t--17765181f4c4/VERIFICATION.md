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

# Reproducibility

Run `python3 verify.py` using Python 3 with only its standard library. The script independently enumerates every three-gap cyclic equivalence class at each length from 4 to 53, constructs actual circular binary words, sorts rotations, computes runs and compares with the structural adjacency rule and the exact class-size formulas. It produces a final PASS line on success. The finite checker does not establish the infinite statement; that follows from the explicit rotation ordering, gap adjacency and Burnside counting arguments in RESULT.md. No independent mathematical audit has been performed.
