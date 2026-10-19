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

The included `verify_squarezero.py` uses only the Python standard library and enumerates all rank-one square-zero matrices over fields of sizes 2, 3, 4, and 5 by their image lines and annihilating covectors. For every ordered pair, it computes the actual difference of matrix products and tabulates the complete target fiber dictionary. It then verifies the zero, nonzero nilpotent, and rank-two formulas, total numbers of targets, and weighted total pair counts. The output is `ALL_EXACT_CHECKS_PASSED 4`. Computation is finite; arbitrary-field validity rests on the written proof, and no independent audit was performed.
