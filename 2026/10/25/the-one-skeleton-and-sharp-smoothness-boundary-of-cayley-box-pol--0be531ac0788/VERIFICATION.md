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

Run `python3 verify.py` using Python 3 and the standard library. No downloads, environment variables, optimization solvers, or input data files are required.

Expected output:

`EXACT_OK matrices=1686 graph_edge_count_simplicity_smoothness=verified sparse_family_d=2..50`

For each input matrix the script independently enumerates cube-layer vertices, computes active linear constraints directly from the coordinate inequalities, and tests every pair using exact rational matrix rank. It checks the predicted graph, both contributions to the edge count, per-layer degrees, simplicity by vertex degree, and smoothness by determinants of primitive incident edge directions. Exhaustive matrices have entries in \(\{0,1,2\}\) and dimensions \((n,d)=(1,1),(1,2),(2,1),(2,2),(3,1)\); 400 additional cases use fixed-seed random matrices in larger dimensions. The special sparse-support degree formulas are also checked symbolically for \(2\leq d\leq50\).

The calculations are exact finite corroboration. The proof in `RESULT.md` establishes the complete graph and two equivalence criteria for every permissible matrix and all dimensions; no computation is asserted to certify infinitely many cases by extrapolation. No external independent audit has been performed.
