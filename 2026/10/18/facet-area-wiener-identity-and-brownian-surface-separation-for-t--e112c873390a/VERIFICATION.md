---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

With d=n−1 tree edges, oriented incidence B has full rank and all n maximal minors ±1, whence det(BᵀB)=n. Each of the 2^d signed crosspolytope facets is a d−1 simplex and its pyramid with origin has intrinsic volume sqrt(n)/d!. Its supporting normal h_s satisfies Bᵀh_s=s and lies in 1⊥, so the facet area is sqrt(n)||h_s||/(d−1)!. Centered path potentials realize h_s, and ||h_s||²=(1/n)Σ_{u<v}(φ(u)−φ(v))². Rademacher independence gives E||h_s||²=W(T)/n and the claimed average squared area. Expanding E||Σ_e s_e q_e||⁴=a²+4Σ_{e<f}<q_e,q_f>²≤3a² and Hölder/Jensen proves sqrt(a/3)≤E||h||≤sqrt(a). On stars, ||h||²=n−1−Y²/n with Y a sum of n−1 signs, so ||h||/sqrt(n)→1 in probability and mean. On paths, a centered random walk scaled by sqrt(n) converges in C[0,1] to centered Brownian motion; the discrete L2 norm satisfies ||h||/n⇒sqrt(Q). Since E(||h||/n)²=(1−n⁻²)/6, uniform integrability gives expectation convergence. The mean-zero Neumann Green operator has eigenvalues 1/(π²k²), yielding Q=Σ Z_k²/(π²k²), and its Laplace product gives c=sqrt(2/π) ∫(1−sqrt(u/sinh u))/u²du. Independent direct incidence/facet Gram determinants for 16 tree cases (n=3..8, 744 signed facets) reproduce gram=n||h||² and exact Wiener means. Independent 60-digit quadrature gives c=0.3781319637260636570, as stated. Finite checks corroborate algebra only; analytic arguments establish arbitrary n and the limit.

## originality

PASS

The published tree crosspolytope equivalence and facet-labeling results, as well as closely matching geometric Resultary findings, are distinguished statement by statement. Lattice equivalence preserves face structure and normalized volume, not intrinsic Euclidean facet measures; prior inradius max-norm, zonotope spherical width and balanced-simplex Wiener energy are different invariants. A broad search found no primary result asserting the full mean squared facet area for all canonical trees, the Brownian path facet-area limit, or the explicit first-order path-to-star surface-area ratio. Standard Brownian and incidence-matrix ingredients are duly acknowledged. This is best-of-knowledge originality and retains risk of an alias/Kirchhoff-index treatment.

## value

PASS

Every canonical n-vertex tree root polytope has the same combinatorial crosspolytope face lattice and intrinsic volume 2^(n−1)sqrt(n)/(n−1)!, making Euclidean boundary geometry a well-motivated invariant invisible to lattice equivalence. The exact squared-area moment converts its geometry into the Wiener index for every tree, not an arbitrary finite parameter slice. The path/star comparison exhibits qualitatively distinct typical facet areas (Brownian random profile versus deterministic concentration) and gives a nontrivial sharp sqrt(n) first-order surface ratio with an explicit universal constant. This is a useful complete structural identity plus an asymptotic classification of two canonical extremal tree families, without asserting unproved global extremality or an optimal universal lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
