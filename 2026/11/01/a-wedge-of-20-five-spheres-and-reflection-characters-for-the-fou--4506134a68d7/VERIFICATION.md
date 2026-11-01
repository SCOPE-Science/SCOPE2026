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

Execute `python3 verify.py` using Python 3.9 or later; no external dependencies are required. The checker builds the exact \(3\times4\) grid, enumerates every one of its \(4095\) nonempty vertex subsets, computes all independent four-subsets, verifies each prospective face from a second direct four-subset test, and enumerates the full codimension-one Hasse incidence set.

The specified vertex-toggle matching yields \(697\) disjoint pairs and exactly one critical zero-cell plus twenty critical five-cells. The complete directed incidence graph has \(1415\) vertices and \(6160\) edges; a topological sort removes all \(1415\) vertices. The check is exhaustive for the finite complex, not a sampling or a timeout-based inference.

For the four rectangular symmetries, signed chain traces and the alternating Lefschetz identity give degree-five homology traces \((20,0,-4,0)\). The character projections give multiplicities \((4,4,6,6)\). The checker prints `VERIFY_OK` only after all checks pass and prints a digest of the complete matching-pair list.

The discrete-Morse homotopy conclusion rests on the standard theorem for acyclic face-poset matchings: a matching with one critical zero-cell and only critical five-cells gives a point with twenty five-cells attached, hence a wedge of spheres. The character calculation is rational and does not certify integral representation splitting. The result is not independently audited.
