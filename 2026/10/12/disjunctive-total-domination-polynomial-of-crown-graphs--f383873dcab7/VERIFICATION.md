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

The proof uses the exact crown-graph distance table to derive an analytic local criterion, so the theorem for all \(n\ge3\) does not depend on finite enumeration.

The accompanying `verify.py` constructs each crown graph directly, computes all-pairs distances by breadth-first search, tests the disjunctive-total-domination definition vertex by vertex, and exhaustively compares it with the claimed classification for every subset when \(3\le n\le9\). It also checks every polynomial coefficient and the minimum-set multiplicity. A replay of the packaged script produced:

`VERIFY_OK n_range=3..9 subset_checks=349504 dtd_sets=348419 criterion_checks=349504 distance_checks=840 coefficient_checks=91 minimum_checks=14 max_order=18`

The finite range is a verification boundary, not an unproved extrapolation. Literature searches and source comparisons are evidence for originality assessment rather than mathematical proof of uniqueness.
