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

For a tetrahedron with original outward facet normals n_i, disjoint parallel-to-opposite-facet truncations of vertex subset S require t_i+t_j<1. Each retained original edge between facets F_i,F_j is a generic silhouette edge exactly for opposite signs s_i≠s_j; each new cut triangle normal is −n_i and meets three old facets, giving [s_i=s_j]. These are ALL edges because cuts are pairwise disjoint; summing yields N_S=Σ_(i<j)[s_i≠s_j]+Σ_(i∈S,j≠i)[s_i=s_j]. For each unordered pair, complement S^c contributes exactly two edges across the two polytopes irrespective of signs; N_S+N_Sc=12 for every generic viewing line and any shape/depths meeting hypotheses. For regular tetrahedron, sign patterns k=1,2,3 positive (14 total), all singleton chambers have total probability p=6 acos(1/3)/pi−2 by classical vertex-cone law, and balanced chamber probability 1−p. For r=|S|, balanced count 4+r and singleton-minority count 3+2(r−1_{m∈S}), giving stage laws r0 {3:p,4:1−p}; r1 {3:p/4,5:1−p/4}; r2 {5:p/2,6:1−p,7:p/2}; r3 {7:1−p/4,9:p/4}; r4 {8:1−p,9:p}. Independent exhaustive 224 subset-sign pattern combinatorial cases pass complement. The generic exception and disjoint cuts are essential.

## originality

PASS

Feldman–Klain (2008) establishes the already known triangular-shadow probability for an untruncated tetrahedron. Resultary previously published arbitrary tetrahedron area-weighted shadow moments, which do not determine new facets under truncation; Coxeter-plane truncated tetrahedron illustrations give selected projections but not the all-direction paired count. The all-shape same-direction complementary law and four new regular probability rows were not found as consequences of inspected sources. Unknown general polyhedral stereology may contain an equivalent sign-edge transfer and remains an explicit priority risk.

## value

PASS

A complete finite-stage natural classification for all subsets of tetrahedron vertex cuts, with a depth-robust pathwise conservation law and perfectly anticorrelated complementary shadows. Extends classical tetrahedron silhouette probabilities to all five truncation stages, predicts only 8/9-gonal generic full-cut shadows, and applies to every nondegenerate original tetrahedron for the complement law. This is a useful geometric structural identity rather than an arbitrary simulated viewing direction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
