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

# Verification and limitations

Run `python3 wheel_convexity_check.py` from a directory containing the included standard-library script. The checker first constructs wheels independently from their adjacency lists and performs graph-distance BFS; for each subset it tests that every interval between selected vertex pairs is contained in the subset. For rim sizes 5 through 11 it compares the complete brute-force convex class with the predicted cyclic-word normal form, then independently tests every query support for all traces. It compares all support counts and the VC dimension to the closed formulas. For rim sizes 12 through 20 it enumerates all cyclic rim supports and verifies polynomial coefficient extraction and the maximum-degree count formula. The final assertion prints `ALL_WHEEL_SHATTERING_CHECKS_PASS`.

The complete parameter-independent theorem is justified by the four-step proof in `RESULT.md`. These finite checks validate boundary behavior and implementation arithmetic only. The historical-priority comparison does not establish exhaustive uniqueness and no independent scientific audit has taken place.
