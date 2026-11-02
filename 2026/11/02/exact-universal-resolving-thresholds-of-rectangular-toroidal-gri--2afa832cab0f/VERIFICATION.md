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

# Reproducibility and verification

The complete theorem and its domain appear in `RESULT.md`. The standalone script `verify_toroidal_threshold.py` uses only the Python standard library and does not depend on an external graph library.

Run `python3 verify_toroidal_threshold.py` from the directory containing the extracted artifact. The program reconstructs every cycle-distance-difference histogram and tests every nonzero translation displacement for all \(3\le m,n\le40\), 1,444 graph parameters. A distinct verification builds explicit four-neighbor graph adjacency, runs independent breadth-first searches from every vertex, computes every vertex-pair bisector and checks the result for all \(3\le m,n\le10\), 64 graph parameters. The complete run returned:

`VERIFY_OK 1444 full offset-pair histogram cases; 64 independent BFS all-vertex-pair cases`

These are exact integer checks, with no numerical tolerance or random sampling, but cover only the displayed finite parameter ranges. The general proof depends on exact one-cycle histogram counts, majorization, rearrangement, the zero-coordinate case, and elementary inequalities. These steps are proved in the accompanying manuscript, not asserted on the basis of the checker alone. No independent mathematical audit or certification has been performed.
