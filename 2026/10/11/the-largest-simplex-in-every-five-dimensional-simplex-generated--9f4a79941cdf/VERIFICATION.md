---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For six centered generators with their unique dependence, the 62 distinct nonempty proper subset sums are exactly the exposed zonotope vertices. Choosing a1..a5 as basis gives volume(Z)=6D, where D=|det(a1,...,a5)|. Independently implemented exact integer Bareiss enumeration of all 3*C(61,5)=17,847,441 orbit-representative 5-completions (each size class 1,2,3) reproduced sharp determinants 14,17,18; the 20-subset middle layer has exactly 30 determinant-18 six-tuples, all distinct five-subset deletions (180), agreeing with the 15 pairings and two 3-pair cycles of the manuscript. A multilinear determinant convex-combination argument reduces arbitrary contained simplices to vertex tuples; the no-common-five-winners fact excludes nonvertex maximizers. Hence optimal ratio (18D/120)/(6D)=1/40 and exactly 30 rigid maximizers. Finite enumeration covers this 62-vertex finite model only, not all convex bodies.

## originality

PASS

The original Živaljević paper establishes the Δ-zonotope construction and cubulation, not the contained 5-simplex optimum. The known maximum 6x6 binary determinant 9 already covers the middle-layer numerical determinant 18, which is credited rather than claimed new. The new statement requires comparing all 42 off-middle vertices, proving rigid global maximizers against nonvertex points, and classifying all 30 by pair cycles. Hudelson–Klee–Larman (1996) optimizes simplices in unprojected cubes; projecting a simplex can change volume and feasible sets, and the accessible abstract provides no specific projection result. Full 1996 text was unavailable and is a residual coverage risk, not automatic rejection.

## value

PASS

The maximum contained simplex and complete equality set are natural affine invariants of a canonical nontrivial Δ-zonotope family. The dimension-five sharp ratio and cycle-indexed 30-solution classification identify a meaningful extremal-geometric benchmark at the boundary of 0-1 determinant phenomena. The all-point rigidity conclusion is not mechanically supplied by knowing the central-layer determinant value alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
