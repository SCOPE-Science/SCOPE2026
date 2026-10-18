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

The frozen result uses log-odds h(f(t))−h(t)=a(t−b), hence a two-cycle satisfies x+y=2b. Parameterizing x=b−u, y=b+u gives increasing A_b(u)=2/u[artanh(u/b)+artanh(u/(1−b))] with endpoint 2/[b(1−b)] and ∞, so unique period-two orbit for a above flip threshold. The derivative identity f'(t)=q(f(t))/q(t)(1−a q(t)) gives Λ=(1−a q(x))(1−a q(y)). Convexity g(t)=1/q(t) and trapezoid inequality show a<g(x)+g(y), hence Λ<1. For b=1/2−δ, uniformly small δ, x≤e^{-a/10} at a≥A; compact/smaller parameter intervals have Λ>-1 by symmetry continuity and nonnegative correction. On a≥1/(2δ), x≤δ and |dx/da|≤x; deriving Λ=1−2aδ(1−2δ)+O((a+a²δ)x) and ∂_aΛ=−2δ(1−2δ)+O((1+a+a²δ)x) gives unique transverse -1 crossing (1/(2δ),2/δ). Evaluating yields a*=1/[δ(1−2δ)]+O(δ^-2 e^{-1/(20δ)}). Symmetric b=1/2 has Λ=(1−a q(x))²∈[0,1). Independent high-precision numerical roots for δ=.1,.05,.02,.01 corroborated scale, not uniqueness in continuum. Scope only small |b−1/2|, local linear stability.

## originality

PASS

PASS for unique near-symmetry transverse multiplier threshold with exponentially accurate singular law; accepted known exact cycle existence, flip onset and exactly symmetric stability as background. Relevant full primary mathematical analyses and bifurcation plots do not themselves establish this complete ray-wise uniqueness and asymptotic; residual possible reparametrized prior threshold is recorded.

## value

PASS

The extreme separation between stable symmetric behavior and an asymmetric loss at a~1/δ gives a natural, sharp singular perturbation boundary in a model where the two-cycle is central. Proving uniqueness/transversality and scale is substantive beyond plotting a bifurcation, while deliberately not claiming a full attractor classification or period-four bifurcation direction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
