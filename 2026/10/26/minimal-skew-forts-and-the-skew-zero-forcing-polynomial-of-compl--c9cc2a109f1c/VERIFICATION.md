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

# Verification scope

The executable `verification/verify_skew_prism.py` uses Python 3 standard-library integers, bitwise masks, and combinatorial coefficients. It constructs the complete prism directly from clique and matching adjacency, simulates **the original skew rule** (both blue and white acting vertices), enumerates all initial white subsets for \(n\in\{3,4,5,6,7,8\}\), identifies all nonempty stalled white sets and exact inclusion-minimal stalled sets, and compares every cardinality coefficient against the displayed formula. The second independent check compares successful forcing against avoidance of all minimal skew forts. The final program execution reported `VERIFY_OK subset_rule_and_obstruction_checks=174720` (two checks per subset). At each order, the minimum-set multiplicity and smallest fort size were also confirmed. The finite test is not a proof for arbitrary order; the result uses the symbolic neighborhood-count argument and exact case-based enumeration in `RESULT.md`.

No independent external mathematical audit or certification has been performed.
