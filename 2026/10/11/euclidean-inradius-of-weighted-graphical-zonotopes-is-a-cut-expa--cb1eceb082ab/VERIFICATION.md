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

The theorem is proved for every finite connected simple graph with strictly positive edge weights. The logical chain is: translate to the symmetry center; compute the zonotope support function as one half of weighted edge total variation; use central symmetry to reduce to a centered inscribed ball; express each mean-zero vector by centered superlevel-set indicators; apply discrete coarea and the Euclidean triangle inequality; and obtain equality from a minimizing centered cut indicator.

The accompanying `verify.py` uses exact rational arithmetic. It enumerates all 771 connected labeled simple graphs on 2 through 5 vertices, applies two positive integer weightings to each graph, verifies all 44,796 nontrivial cut comparisons, and checks 74,220 nonzero mean-zero vectors with coordinates in {-1,0,1}. Replay output:

`VERIFY_OK graphical-zonotope-inradius connected_graphs=771 weightings=1542 cut_checks=44796 vector_checks=74220 n=2..5`

This finite replay is corroborative only. It is not an exhaustive proof for arbitrary graph size or arbitrary real weights, and the general claim does not depend on it. The unresolved literature risk is possible alternative graph-Sobolev terminology for the variational quotient; no independent audit has been performed.
