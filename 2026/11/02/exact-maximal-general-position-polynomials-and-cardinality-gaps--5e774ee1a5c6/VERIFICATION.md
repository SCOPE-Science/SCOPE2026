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
# Reproduction and boundaries

The standalone `verify.py` uses standard Python without external dependencies. Running `python3 verify.py` tests nine rook graphs directly from their adjacency relations. It constructs shortest-path distances by breadth-first search; each forbidden triple is checked against the three geodesic equalities. Exhaustive subset enumeration and inclusion-maximality are checked independently of the labelled-block counting recurrence in the same script. The independent finite-sum formula is asserted equal to the exhaustive counts for every tested size and every coefficient. The combined complete finite test consists of 1,152,848 vertex subsets, including a 20-vertex board with 1,048,576 subsets. All tested comparisons passed in the reviewed execution. The infinite claim is justified by the proof in `RESULT.md`, not by an extrapolation from these finite tests. Publication priority remains subject to differently formulated or unindexed sources.
