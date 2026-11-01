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

Exact proof: an attached subtree's two-step boundary-count tensor splits as \(A_h(p_0,s_1)A_h(p_1,s_0)\); the strict three-neighbor majority and the two-neighbor root tie rule give the nonlinear recurrence and root closure. Primitive two-cycles are obtained by subtracting the known fixed states and dividing nonfixed returning configurations into temporal pairs. The root fraction and entropy follow from the ratio recurrence and a geometrically bounded logarithmic series.

Actual reproducible checks: run `python3 verify_majority_tree.py` alongside the embedded verifier. The captured output `verify_majority_tree.output.txt` confirms independent sixteen-entry pair dynamic programming and a separate fixed-state recursion for heights 1 through 8, plus exhaustive synchronous microscopic one-step/two-step simulation for all 32,904 binary labelled states of heights 1 through 3. The final line is `BINARY_TREE_MAJORITY_VERIFY_OK 8 independent_DP_heights_and_3_exhaustive_heights`.

Scope: no claim of exhaustive microscopic simulation at unbounded height, no proof from finite experiments, no basin census, and no independent external audit. The exact general-height theorem is proved by algebraic induction. Earlier general tree periodicity and fixed-point counting are credited rather than represented as new.
