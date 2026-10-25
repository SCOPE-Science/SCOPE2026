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

# Reproducible exact verification

Run `python3 verify.py` from this same package with a standard Python 3 interpreter. The verifier has no external dependencies. It reconstructs the icosahedral graph, its rectification, graph distances, all relevant clique faces, two lexicographic acyclic Morse matchings and their complete directed Hasse graphs. It checks the exact signed differential \((1,-1)\), the full oriented 56-triangle surface cycle, all 330 and 3,150 three-simplex cocycle equations, the evaluations \(1\) and \(-1\), and the fifteen disjoint distance-five pairs. Every assertion is a finite integer equality or combinatorial condition.

The critical topology reasoning is: one critical zero-cell and one critical two-cell imply \(K_2\simeq S^2\); at scale three a primitive three-cell attaching vector \((1,-1)\) on \(S^2\vee S^2\) leaves \(S^2\); the integral cocycle pairings establish that the actual scale-two inclusion induces a unit map on integral degree-two homology and therefore is a homotopy equivalence. The scale-four complex is a join of fifteen two-point sets and has type \(S^{14}\). At scale one the independent triangular two-cell boundaries collapse to eleven circles.

This finite check does not cover other graph metrics, other Archimedean solids or all possible equivalent prior publications. No independent audit or independent validation was performed.
