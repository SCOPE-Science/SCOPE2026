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

# Reproducibility and limits

Run `python3 verify_folded_geodesics.py` with a standard Python 3 interpreter. It constructs the full antipodal quotient as a simple graph and calculates shortest-path distances from the zero class by breadth-first search. For every distance and every target class in each dimension \(3\le n\le10\), it enumerates **all** shortest vertex paths by monotonically increasing BFS distance, then defines adjacency by differing in exactly one vertex position. It asserts the predicted number and sizes of connected components, all edges and degrees. For the first target of every distance class it independently calculates every rerouting eccentricity, testing the predicted common radius and diameter. Its exact recorded output is `verify_folded_geodesics.out`, terminating with `VERIFY_OK`.

The finite test is exhaustive for the stated dimensions, not for infinitely many dimensions. The general theorem follows instead from the group-kernel, two-generator displacement, and small-dimensional arguments in `RESULT.md`. There is no independent external audit. Source comparisons and residual originality risk are described in `REVIEW.md` and `AUDIT.json`.
