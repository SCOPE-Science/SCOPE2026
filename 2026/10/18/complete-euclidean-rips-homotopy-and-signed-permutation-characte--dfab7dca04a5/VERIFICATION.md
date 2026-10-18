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

# Verification methods and limitations

The accompanying `verifier.py` and `collapse_pairs.json` reconstruct the fourteen stated Euclidean integer-coordinate points and compute all \(91\) squared pair distances. It additionally enumerates and solves all triples of the twelve defining halfspaces using exact rational arithmetic, verifying that the resulting convex polytope has exactly the fourteen required vertices and twelve four-vertex facets. The program enumerates complete flag faces at squared thresholds \(3,4,8,11,12,16\), checks the exact convex-boundary triangulation, and replays all \(80\) elementary free-face deletions **in order**. Each pair is checked against the then-current complex, with exactly one codimension-one coface, and the final surviving faces are compared exactly to the full cube-vertex crosspolytope boundary. It then verifies crosspolytope and join structure and compares the signed Lefschetz traces of the four stages to the expected symmetry characters for **all \(48\)** signed-coordinate permutations.

The finite checks are exact, use only standard Python, and do not infer infinite statements from experiments. The proof supplies a general relative acyclic-matching argument independent of the chosen \(80\)-pair elimination order. The assertion concerns only this finite point configuration, so exhaustive enumeration is logically sufficient for the computational parts.

To replay after extracting all embedded files to one directory: run `python verifier.py`; expected marker `VERIFY_OK`. The checked results include \(38,74,240,2186,6911,16383\) nonempty faces at the successive squared thresholds and the complete list of six squared pair-distance shells. The externally independent scientific audit has **not** been performed, and these checks do not rule out an equivalent result in unindexed literature.
