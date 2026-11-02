---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For each existing nontrivial S(2,k,n), pair counting gives r(k-1)=n-1, bk=nr and r>=k, so n>=k(k-1)+1>2k and n>=7. The complement of each k-point block has >k points, hence a noncollinear basis triple and zero minimum of x(B); a basis with two points in the block and one outside gives maximum 2. Coordinate minima/maxima are 0,1. The rank-three matroid basis-exchange proof is valid, and Edmonds rank inequalities reduce the complete polytope to x(E)=3, 0<=x_i<=1, x(B)<=2. For reflected inclusion y=((s+1)c-x)/s, coordinate extrema force 1/(s+1)<=c_i<=s/(s+1). Block maximum y(B) from min x(B)=0 forces c(B)<=2s/(s+1). The lower c(B)>=2/(s+1) in the source is redundant but valid, following from the coordinate lower bounds because k>=3; it is not an independent necessary block-facet constraint. Summing coordinate and block constraints over the regular design yields four lower bounds (n-3)/3, 3/(n-3), 3k/(2n-3k), (2n-3k)/(3k). At the uniform center c=3*1/n all constraints hold for s equal to their maximum, so optimization over arbitrary centers is exact. For k=3, n=7 gives 9/5, and n>=9 gives (n-3)/3; for k>=4, n>=3k+1 implies (n-3)(2n-3k)>=9k. Thus the only exception is Fano. Non-Fano optimality saturates all coordinate lower bounds, forcing c_i=3/n; Fano optimality saturates all seven block upper bounds and A^T A=2I+J is invertible, again forcing c=3*1/n. Independent exact tests checked PG(2,2), AG(2,3), PG(2,3) with 28,72,234 bases and rational reflected containment, as well as 39,200 pairs (n,k) in a finite parameter box for the bound comparison. These finite checks are corroboration only; universal claim follows from algebra and matroid polytope characterization.

## originality

PASS

Best-of-knowledge distinct from general matroid-base Minkowski-center LP, rank-two base-polytope formula, polymatroid independence-polytope density theorem and same-object Steiner-design Ehrhart/face-volume results. The new content is closed exact reflection-dilation factor for all existing nontrivial S(2,k,n), unique uniform center, and sharp Fano exception. Source-level comparison is about implication, not titles or numerical coincidences. Priority not absolute; possible unindexed general base-polytope theorem remains.

## value

PASS

The rank-three base polytopes of Steiner systems are a natural, broad design-theoretic class including projective and affine planes and nonisomorphic Steiner triple systems. Their affine-invariant reflection asymmetry and minimizing-center locus are intrinsic geometric invariants not determined by the published Ehrhart/face-vector data. This exact all-design classification shows a stable hypersimplex benchmark despite loss of permutation automorphism symmetry and isolates the seven-point Fano plane as a genuine exceptional boundary. Rigidity of the uniform center is nontrivial when automorphisms need not be transitive. The exact factor and unique center are useful standalone geometry, not merely a known-table value or one-off finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
