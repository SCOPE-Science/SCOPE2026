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

# Reproduction

Run `python3 verify_cycle_burning.py` with Python 3 (standard library only). The program uses a direct graph-distance definition of legal ignition and burning to enumerate all labeled length-\(k\) tuples at \(k=2,3,4\), independently of the formula-generating arc constructions. It checks both cycle orders \(k^2\) and \(k^2-1\) at these parameters. It separately generates all \(k^2-1\) optimal candidates via labeled cyclic arcs for \(2\le k\le7\), calculates exchange adjacencies by deleting each time coordinate, and computes component sizes with a disjoint-set union. Counts and degree histograms are asserted against closed formulas, and generated sequences through \(k=5\) are checked by the direct distance conditions.

Expected near-square `(k, states, edges, components)` values are `(2,6,6,1)`, `(3,48,80,1)`, `(4,360,720,2)`, `(5,2880,6336,6)`, `(6,25200,58800,24)`, `(7,241920,587520,120)`. At square order for \(k=2,3,4\) the counts are \(4,18,96\) respectively, all isolated. A successful run concludes with `VERIFY_OK`.

The generated checks are finite. The proof for all integers \(k\ge2\) is the interval tiling, defect and adjacency argument in RESULT.md. No validation by an independent party has been performed.
