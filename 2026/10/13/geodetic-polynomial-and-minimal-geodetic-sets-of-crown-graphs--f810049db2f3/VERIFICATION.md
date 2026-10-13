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

The symbolic proof is checked independently by `verify.py`. For each \(3\le n\le8\), the program constructs the crown graph, computes all-pairs shortest-path distances, and tests every vertex subset directly against the definition that each vertex must lie on a shortest path between selected endpoints. It then compares the result with the structural criterion, compares every polynomial coefficient with the closed formula, and checks inclusion-minimality by deleting each selected vertex.

Replay command:

`python verify.py`

Observed output:

`VERIFY_OK n_range=3..8 subset_checks=87360 geodetic_sets=79076 minimal_sets=765 coefficient_checks=72 minimal_checks=79076 max_order=16`

The finite checks verify instances through order \(16\). They do not replace the general proof. The originality comparison is literature-based and remains subject to the partial-access risks described in `REVIEW.md`.
