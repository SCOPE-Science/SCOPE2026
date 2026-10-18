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

The source's \((-p)\)-mean uses an unnormalized spherical area integral divided by the ambient dimension; the proof and checker use exactly this convention. The proof separately checks the a.e. radial derivative of a nonsmooth Minkowski gauge, the uniform boundedness needed for dominated convergence, the area-measure Jacobian, and the vanishing total normal integral. Global Hausdorff convergence uses the exact ordinary-covariogram chord identity as a localization bound, not merely local uniform convergence. The polytope rate uses an explicit finite-facet maximum and spherical band-measure estimate, not a finite-dimensional guess.

Run the standalone standard-library checker with `python3 check_critical_polytope.py`. It uses 20,000 midpoint polar nodes on each of four rectangle/triangle displacement tests and independently verifies the area of each polygon, the finite-parameter deficits, the explicit limiting facet integral, and decreasing errors for \(p=40,80,160,320\). This is a numerical consistency check with discretization error and does not establish the infinite limiting claims. The theorem is not asserted for bodies with origin only on the boundary, nor are dimension-uniform or sharp rate constants claimed.
