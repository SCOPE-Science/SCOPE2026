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

Run `python3 verify_honeycomb.py` with no third-party dependencies. The program independently constructs all perfect-matching facets using the stated plane-partition formulas, checks that the edge map is a facet-preserving involution, checks the minimal nonface, tests the two-pivot matching and separation of all paired faces from the invariant boundary, and verifies signed simplicial Lefschetz numbers. It then removes the outside faces by actual elementary-collapse sequences.

Observed complete finite cases: \(n=2,3,4\). Facet totals: \(6,10,15\). Face totals including the empty face: \(1347,17487,206127\). Outside elementary-collapse counts: \(670,8736,103048\). Reduced Lefschetz numbers: \(1,1,-1\), corresponding to half-turn degrees \(-1,+1,+1\). The ending program markers are `HONEYCOMB_RELATIVE_COLLAPSE_HALF_TURN_FINITE_CHECKS_OK` and `HONEYCOMB_ACTUAL_ELEMENTARY_COLLAPSE_REPLAY_OK`.

The infinite-family conclusion relies on the universal proof in `RESULT.md`. The finite replay is not a substitute for proving acyclicity, for proving the relative matching valid for every \(n\), or for external expert verification. No independent audit has been performed.
