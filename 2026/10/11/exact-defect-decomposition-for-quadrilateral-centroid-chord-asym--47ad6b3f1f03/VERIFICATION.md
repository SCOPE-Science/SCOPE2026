---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Affine normal form from intersecting diagonals, positive x>=y>=1 and 0<=v<=u<1 covers all nondegenerate convex quadrilaterals up to affine/dihedral relabeling. Area centroid G=((x-1)/3,(1-y)/3) follows by triangle area weighting. Solving the linear endpoint equations for all six edge pairs shows only three distinct valid bisected chords: (1,2),(1,3), plus (0,2) when v<=u/(u+2) or (2,3) when v>=u/(u+2); at the interface the latter two represent the same vertex chord. The other two edge pairs have parameters outside [0,1]. Directed shoelace areas yield a12,a13,a02,a23 as displayed; difference factors and domain signs give a12<=all<=a13. Independent exact-rational geometry checks: 127 configurations including v=0, v=u, chamber boundary and u=3/7,v=0; exact chord count 3 and exact area-ratio agreement in every case. Independent SymPy simplification proves the displayed rho formula and two-term defect identity. Delta>0 and B>0 on 0<=v<=u<1, so equality iff u=3/7,v=0; parallelogram endpoint rho=1. Additionally d(rho)/dv=v(1-u)P/[(1+u)Delta²]>0 for 0<v<=u, by explicit polynomial coefficient bounds. The rational finite checks supplement the algebraic proof, rather than proving it by sampling.

## originality

PASS

Best-of-knowledge novelty attaches ONLY to the full affine two-modulus pointwise rho-profile, exact positive two-term defect identity, and fixed-u reduction. The sharp scalar 24/25 lower bound and affine equality class were already in Chevallier–Fruchard–Vîlcu (2015) and are not credited as new. The materially read Section 8.9 reports the known extremum using Maple, but does not state the general rho(u,v) formula or the positive v² defect. No stronger implication identified in separate alias, formula, or semantic-index searches. Published self-match excluded from priority.

## value

PASS

The quotient is a natural affine asymmetry invariant explicitly introduced in the original centroidal-section literature; arbitrary nondegenerate quadrilaterals form a complete two-parameter affine moduli chamber. The known scalar extremum 24/25 does not evaluate the quotient at other quadrilaterals. The exact full-moduli profile and positive separated defects identify the contribution of each diagonal imbalance and a unique fixed-u minimizer, providing a reusable analytic stability description and potential starting point for other polygons or convex bodies. This is a motivated exact structural classification, not a renaming or recomputation of a known table entry. No higher-dimensional or general-body theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
