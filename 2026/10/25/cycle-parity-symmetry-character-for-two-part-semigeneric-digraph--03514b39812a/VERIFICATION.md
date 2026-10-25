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
# Verification record

The accompanying `verify.py` brute-forces every bit assignment on each tested bipartite edge set, retains only those obeying even parity on all rectangles, and directly tests permutation invariance. It checks every side-preserving permutation pair and every side-swapping permutation pair for balanced shapes, then independently checks Burnside averages and orbit formulas.

Seven shapes were checked: (1,1), (1,2), (2,2), (2,3), (3,3), (2,4), (3,4), for 288 group-character comparisons. Expected final verifier line: `ALL_TESTS_PASS 288`.

All-parameter correctness follows from the stated algebraic proof. No external review or proof-assistant certification is claimed.
