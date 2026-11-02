---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Verified the actual RESULT.md for all k≥2, n_i≥2 over Q. In the clique complex X of the Hamming graph, a ≥2-vertex clique belongs to precisely one coordinate-line simplex; these contractible line simplices meet at at most one vertex. The surjection ⊕_L C_*(Δ_L)→C_*(X) is an isomorphism in all positive degrees and has precisely the vertex-direction redundancy in degree zero, inducing H_1(X)=ker[Q[V×[k]]→Q[V]⊕Q[L]]. Decomposing Q[V] as ⊕_{S⊂[k]}⊗_{i∈S} U_i (normalized constant factors elsewhere), each direction i has one copy of W_S in incidences, the line incidence kills the term exactly if i∈S, and vertex incidence enforces Σ_{i∈S}c_i=0. Thus the kernel is E_S⊗W_S for |S|≥2, with no higher H_j and no H̃_0. This is canonical and equivariant under independent alphabet permutations and swaps of equal-size axes. The combinatorial Alexander dual T=X* then has only H̃_{N−4}, with the orientation character sgn_V and rational self-duality via invariant inner products. Finally [H_1(X)]=[Q[V×[k]]]−[Q[V]]−[Q[L]]+[1] proves χ(g)=sgn_V(g)(1−ℓ(g)+(d(g)−1)v(g)); χ(1) gives (k−1)N+1−ΣN/n_i. All normalizations and the boundary k=2,n_i=2 (degree zero) check out. Independently computed direct total-two-cut faces, rational signed traces and mod-2 boundary ranks on five finite Hamming shapes (188 group elements in all); all match. The finite computations corroborate, but the uniform theorem follows from the exact incidence/duality proof, not test counts.

## originality

PASS

Best-of-knowledge PASS for the new all-parameter rational Γ-module and full character, not for the already published Hamming homotopy type or identity-character rank. The primary Carnero Bravo Theorem 41 dominates the nonequivariant rank and wedge statement; the observed finite/parameter special cases and generic cut-complex techniques do not imply the tensor-augmentation constituents or the nonidentity character without additional equivariant incidence calculations. The exact top semantic-search match is the same current record, not independent priority evidence. The comparison is substantive and residual unindexed-equivalence risk is retained.

## value

PASS

The already known complete all-parameter Hamming total-two-cut wedge count does not determine the natural automorphism representation. The explicit full coordinate-group module and signed character refine a natural topological invariant uniformly in arbitrary alphabet sizes and coordinate number, isolate higher-order coordinate-interaction constituents and their multiplicities, and detect equal-axis interchanges. This is a motivated structural classification across an infinite family, beyond merely recalculating a known Betti number, although it is not an integral-module or equivariant homotopy classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
