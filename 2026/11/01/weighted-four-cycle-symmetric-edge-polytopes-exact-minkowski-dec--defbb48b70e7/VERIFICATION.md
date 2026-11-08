---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The normalized centrally symmetric circuit has vertices ±e_1,±e_2,±e_3,±(a,b,c), a,b,c>0. A generating antipodal pair drops exactly when one of four strict convex-hull triangle-inequality chambers fails, producing a 3D crosspolytope and hence an indecomposable six-vertex case. In the eight-vertex region a facet has at most one point from each antipodal pair, and a four-vertex facet forces one of the three signed equalities a+b−c=1, a−b+c=1, −a+b+c=1. With zero or one equalities, connected triangular facets touch all facets, so McMullen’s criterion yields indecomposability. Two equalities reduce, up to permutation, to a=1,b=c=t≠1: the formula Q_t + [−m h,m h], m=min(1,t), h=(0,1/2,1/2), gives an exact Minkowski decomposition with crosspolytope Q_t. The four triangular facets in two components and parallel cross-edges force every summand deformation, modulo translations, into a two-dimensional cone. Its two independent indecomposable factors therefore supply precisely the two extremal rays. All three equalities give a three-segment parallelotope. Returning to original positive edge weights, exactly two equal pairs characterize the decomposable locus. Independently enumerated rational supporting facets and solved exact edge-parallel deformation linear systems corroborate the 1-, 2-, and 3-dimensional nontranslation deformation cones. Finite rational tests are corroboration, not the universal proof.

## originality

PASS

The unweighted K_{2,2}=C4 result is explicitly prior and not newly asserted; the all-positive-edge-weight equality-stratum criterion and the exact summand cone are different assertions. Checked both exact graph terminology and the affinely normalized antipodal eight-vertex circuit, conditional decomposability and deformation cone aliases. The closest full-text primary work provides tools or broader combinatorial context, not an implication of the quantitative weight equality classification. This is best-of-knowledge originality with historical-priority risks.

## value

PASS

This is a sharp, motivated classification for the smallest graph C4 whose unweighted symmetric edge polytope is decomposable. It identifies exactly how anisotropic edge weights destroy the Minkowski factorization, distinguishes quadrilateral-facet changes from genuine decomposability, and classifies the complete summand cone on the two-equality strata. A future deformation or rigidity study of edge-weighted circuits can need the precise equality loci, not just the unweighted special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
