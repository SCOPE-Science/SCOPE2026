---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

With common positive stationary π, every layer report has leverage α_ℓπ_i. Positive quadratic costs make each agent best response unique, and first-order conditions give y*=(barθ+Σ_iK_i θ_i)/(1+Σ_iK_i), K_i=Σ_ℓπ_i²α_ℓ²/c_iℓ. The displacement coefficient v_i=K_i−π_iΣK_j has zero sum, so maximizing |v⋅θ| over the opinion hypercube gives ||v||_1/2 exactly. The bijection z_ℓ=α_ℓ²/Σα² makes denominator G(z)=(Σ√z)^2+Σs_ℓz_ℓ, strictly positive and concave. Every sublevel ||Az||_1≤2τG(z) is convex, and rotated geometric-mean second-order cones yield equivalent feasibility, including boundary τ=0. Neutrality is Az=0, giving convex hull of n-dimensional zero-sum columns, and Carathéodory bounds support by n. For n distinct positive cyclic-shift layers, total variation from uniform and Cauchy–Schwarz bound prove sharp δ(1−m/n)/(n+δ+m), attained by m uniform active layers. Independent checks compared full 2^n opinion-vertex maximum and both formulas in heterogeneous examples n=2..5 to 7e−18, and confirmed the exact constructed frontier for 16 (n,m) cases.

## originality

PASS

The motivating Ebrahimi–Franceschetti preprint establishes equilibrium, centrality tilt and optimization for a fixed known opinion profile. The assessed claim instead minimizes worst-case displacement simultaneously across all bounded unknown opinions, proves exact quasiconvex/SOCP feasibility and a sharp layer-budget frontier in a distinct-layer family. The full original preprint could not be obtained via arXiv/OA; authorized Oxford institutional access returned VPN disconnected. That strongest primary comparison is a material explicit priority risk; the public abstract and indexed descriptions do not establish a dominating universal-minimax theorem.

## value

PASS

Opinion-blind robust design and universal no-distortion feasibility are natural platform questions distinct from optimizing one known profile. The exact conic feasibility test gives computationally actionable characterization, while the sharp n-layer necessity example shows a meaningful boundary despite all primitive layer matrices being distinct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
