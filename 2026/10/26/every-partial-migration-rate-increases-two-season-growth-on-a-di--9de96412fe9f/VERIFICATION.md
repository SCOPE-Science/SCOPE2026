---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With a=1−d, b=d and Q=M D⁻¹ M D, put u=x/y, v=y/z, w=z/x, so uvw=1. The trace is 3a² and the principal 2×2 minors sum to 3a⁴−ab³(u+v+w+uv+uw+vw). Also det Q=(det M)²=(a³+b³)². It follows that det(I−Q) differs from its homogeneous value by −ab³ times the ratio sum minus 6; the homogeneous value is zero because Q=M² is column-stochastic. This proves the asserted identity for all parameters. The defect is the sum of (D_ii−D_jj)²/(D_ii D_jj) over the three index pairs i<j, and is positive exactly for a nonconstant diagonal. The index-pair reading is needed at repeated values: the shorthand sum over pairs in the set {x,y,z} in the proof should not drop multiplicities, which are explicit in the Finding. A strictly negative monic characteristic polynomial at 1 has a real zero above 1, yielding the strict spectral-radius bound. At d=0 the normalized operator is I; at d=1 it is a weighted permutation on one 3-cycle with weight product one. The homogeneous case has radius one at every rate, and continuity ensures an interior global maximizer in the heterogeneous case. For a two-patch kernel with both off-diagonals positive, positive diagonal similarity gives a symmetric migration matrix N(d) without changing either growth diagonal. Conjugating the period operator by D₁^(1/2) then gives BᵀB for B=D₂^(1/2)N(d)D₁^(1/2); ||B||₂ is convex in d and maximized by at least one endpoint. A one-way or diagonal kernel is triangular, with each period diagonal term bounded by its no-migration value; one patch is immediate. The independent rational replay checked trace/minor/determinant expressions in 448 cases, 300 strict, and independently recovered the example polynomial and its value −1/2 at two. This corroborates the all-parameter algebra, not a sampling proof of it.

## originality

PASS

Schreiber–Li already show strict interior advantage for the same normalized two-season family at one directed-triangle parameter point. The overlapping witness and the reversible endpoint argument are not supported as distinct claims. The all-positive-profile, all-intermediate-rate if-and-only-if and its ratio discriminant are the distinct core: the known example fixes both D and d, and the general reversible results exclude one-way cycles. The frozen paper locator for the example should be the closing remark after Appendix B on PDF p. 20, not an Appendix A concluding remark.

## value

PASS

The all-parameter identity resolves whether a known failure of reversible dispersal intuition depends on a carefully chosen migration rate and growth triple. For the minimal directed cycle with equal isolated period multipliers, the strict advantage holds at every genuine partial rate under precisely heterogeneity, with both endpoints and the homogeneous equality case identified. This is a complete classification of a natural basic model rather than a new numerical example, and it does not presume a field or nonlinear consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
