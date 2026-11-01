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

For any finite simple F with n≥1, each pendant leaf ℓ_v forces every dominating set to meet the disjoint pair {v,ℓ_v}; selecting all originals dominates B(F), hence γ(B(F))=n. Equality chooses exactly one per pair and excludes every subdivision vertex. A subdivider w_uv is dominated precisely when at least one endpoint u,v rather than its leaf is chosen: therefore selected-leaf indices form an independent set I, and every I yields exactly D(I). Consequently the marked polynomial is I_F(t). Any size-preserving swap between min sets must flip the same pair v↔ℓ_v, an actual edge, giving identical token-slide and unrestricted exchange reconfiguration graphs, the simplex graph S(complement F). Removing I\J then adding J\I gives exact Hamming metric; the majority of three independent sets is independent, giving medianity. Every k-dimensional induced cube in the ambient coordinate hypercube is a coordinate face with a unique maximum independent set I and k freely toggled positions: c_k=Σ_I binom(|I|,k), so C(q)=I_F(1+q). Direct degrees, subdivision cycles, leaf attachments establish size 2n+|E|, bipartiteness, girth at least six, maximum degree max{Δ+1,2}, planarity and connectivity claims. Cubic independent-set #P-hardness transfers parsimoniously to the specified degree-four bipartite high-girth family; no unproved general #P-membership claim. Inspected source verifier tests 1,369,076 subsets across 81 graphs, and independently developed checker additionally exhausts 78 graphs including all n≤4, compares real minimum-set adjacencies, BFS distances and cube counts. These finite tests substantiate but do not replace unrestricted combinatorial proof. Edge cases n=1, isolated vertices, empty E and disconnected F are included.

## originality

PASS

Best-of-knowledge PASS for the new minimum-domination bijection and restricted bipartite realization of the already-known subdivision-vertex corona, and for the resulting token-slide/jump solution-graph identification. PRIOR: Lu–Miao (2013) defined exactly B(F) as F ⊙ K1; DeVos et al. (2020) proved unconstrained family gamma-realizability; Xie–Xu (2025) covers simplex graphs/medianity; Xie–Feng–Xu (2024) ALREADY proves the shifted clique/cube polynomial identity for simplex graphs. None of those inspected full texts gives the specific B(F) min-domination correspondence with 2n+|E| vertices, girth≥6 and degree four for cubic F. New value/novelty is NOT claimed for the graph operation itself, the cube identity alone, generic gamma realizability, medianity, or independent-set #P-hardness. Search absence does not certify priority; a missing specialized subdivision-vertex corona domination classification remains a material risk.

## value

PASS

The all-source, explicit restricted realization transfers complete minimum dominating-set families, marked solution-size polynomial, exact token-slide/jump metric, and a parsimonious cubic-input counting reduction into a sparse bipartite host of girth≥6. These constraints matter for domination reconfiguration and counting and are not implied by unconstrained family realization. Although private-pair arguments and the cube identity once the simplex graph is identified are elementary/previously known, the uniform solution-family representation across arbitrary source graphs is a motivated structural result rather than arbitrary unmotivated sampling. Value is limited to this specified known graph operation; it does not extend to all bipartite graphs and does not make old median/cube facts new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
