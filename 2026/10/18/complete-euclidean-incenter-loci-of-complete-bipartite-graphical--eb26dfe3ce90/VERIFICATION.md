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

The analytic argument reduces Euclidean inball containment to all cut inequalities via the exact graphical-zonotope support function, applies the complete-bipartite Laplacian spectrum to classify equality cases, and derives all center restrictions by preserving both orientations of each tangent cut hyperplane. The exceptional \(K_{2,2}\) case is treated separately.

Reproduce: `python3 checker.py` with the Python standard library. The script checks 36 entire cut collections through 14 vertices using exact integer comparisons and rational ranks; it additionally checks both explicit \(K_{2,q}\) endpoint families through \(q=11\) with 75-digit decimal arithmetic. Those latter floating-decimal computations are corroborative only. The formulas for all dimensions and binomial endpoint multiplicities are proved algebraically in RESULT.md rather than extrapolated from experiments.

Known radius coverage: the general weighted-graph cut-expansion formula supplies the scalar radius, so the new statement concerns only full incenter loci, their dimensions and facet-contact transitions. No independent audit or validation has been performed.
