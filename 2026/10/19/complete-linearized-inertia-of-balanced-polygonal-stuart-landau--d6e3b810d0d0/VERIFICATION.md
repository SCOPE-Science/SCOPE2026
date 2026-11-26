---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The complete-graph coupling is c times the sum minus Mc times the local coordinate. After rotation and use of the equilibrium radii, the quadratic form is c|Tv|²−2κ|Uv|², with Tv=Σv_j and (Uv)_j=w_j·v_j. When the polygon is noncollinear, U is onto and T maps ker U onto the plane, so (T,U) is onto. In a basis lifting its image and completing with its kernel, the form is congruent to diag(cI₂,−2κI_M,0_{M−2}). The derivative of polygon closure on the fixed-radius product has rank two because the rotated w_j span the plane. Thus the kernel is the tangent space of the equilibrium manifold. Continuity and the separated nonzero spectrum give local normal hyperbolicity, not a uniform bound up to the collinear set. At collinearity signs of the w_j drop out: the transverse block is c11ᵀ, and the longitudinal block is −2D+c11ᵀ with D=diag(β_j−Mc)>0. Congruence by D^(−1/2) gives M−1 negative directions and the sign of 2(τ−1) for the last longitudinal direction. The transverse block adds one positive and M−1 zeros, so the critical equality and both strict inequalities give exactly the displayed cases; each is unstable. I read the rational checker but did not run it; the argument is exact for arbitrary permitted lengths.

## originality

PASS

The rotating-frame gradient system and closed-polygon zero-mean family, with its generic dimension, are prior work. In the primary passages inspected, I found no prior determination of all the indices for arbitrary all-active fixed-length shapes under positive real coupling, or of the exact singular collinear threshold. Two later catalogue records cover the same theorem, one as a special case of a wider classification. Their later dates do not support earlier priority; the overlap is substantive and does not make these three different mathematical results on the common regime.

## value

PASS

The result replaces shape-by-shape stability analysis in the real-coupled regime by complete indices for every allowed size and heterogeneity. The two normally expanding directions at regular polygons and the sharp loss or gain of one longitudinal direction at collinearity separate degeneracies that the common-phase neutral mode alone would not reveal. This is a useful exact benchmark for these equilibria, without implying a nonlinear bifurcation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
