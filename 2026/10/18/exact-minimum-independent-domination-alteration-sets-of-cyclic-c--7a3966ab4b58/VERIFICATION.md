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

# Reproducibility and verification limits

Run `python3 verify.py` from the unpacked finding directory. It uses only the standard library and prints `VERIFY_OK` after the following reproducible checks:

1. Enumerate all subsets of sizes below or equal to the asserted threshold in every cycle of order \(3\le n\le30\), calculate the surviving path-gap ceiling sum and compare the complete directional count and structural conditions.
2. Independently enumerate all independent dominating vertex subsets for the necessary cycle deletions at \(3\le n\le11\).
3. Independently check all labeled base graphs of orders one through four, with two-vertex clique substitutions, under **every** vertex deletion pattern (16,932 base-graph/deletion combinations).
4. Enumerate deletion patterns directly in six clique-expanded cycles: \((n,q)=(3,2),(4,2),(5,2),(6,2),(3,3),(4,3)\).

All checks passed on the packaged source version. These computations corroborate small instances only and do not prove the infinite theorem; the full proof is in RESULT.md. The counts refer to labeled deletion sets. No independent audit or external scientific validation has been performed.
