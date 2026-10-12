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

The included `verify.py` uses only Python 3.9+ standard library. Running `python3 verify.py` rebuilt the eighteen-vertex, twenty-seven-edge incidence graph from \(\mathbb F_3\), independently checked the shortest-path matrix and coordinate distances, and exhaustively examined all \(262144\) vertex subsets by both distinguishing-mask and distance-signature conditions. It confirmed the full resolving polynomial, the criterion for every one of the \(3060\) four-vertex candidates, and the two \(108\)-element orbits under \(216\) incidence automorphisms.

The exact computation covers the entire finite domain of the stated Pappus graph, but does not establish a general theorem for arbitrary biaffine order and does not provide independent external validation. Literature-priority checks are described separately in `REVIEW.md` and `AUDIT.json`.
