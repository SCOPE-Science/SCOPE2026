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
Run `python3 verify.py` using Python 3 and no third-party libraries. It constructs explicit color arrays, checks that every edge has one assigned color different from both endpoint colors, and runs union-find cycle detection separately on every monochromatic vertex-induced graph and monochromatic edge graph. It checks the counting lower bound against the prescribed color number for every width \(1\), \(2\), \(3\) and all second-part lengths up to \(200\), and checks each of the four saturated spanning-tree capacities on the exceptional graph.

Observed check: `CHECKS_PASSED instances=597 all_graph_edges=182077 special_K_1_3_5=23 saturation=YES`.

The proof in RESULT.md establishes the unbounded range; these finite tests are only consistency checks. There has been no independent audit.
