---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Eliminating z gives the shared endemic state. The Jacobian has trace −(A+κB), determinant κ(τ−1), and scaled discriminant (1−r)²−4rg for r=κ/κ₀; the nonzero off-diagonal entry rules out a scalar matrix at the two discriminant roots. Differentiating κ/(A+κB)² gives the unique damping-ratio optimizer. For the spectral rate, put S=A+κB, T=τ−1 and X=BS−2T; on the node branches X²−B²D=4TC>0, with X negative on the lower branch and positive on the upper branch. Thus the rate increases through the lower node and focus intervals and decreases on the upper one. For the nonlinear claim, at κ₀ the map e^(−Jt) applied to the state deviation is the initial deviation plus a convergent integral of the quadratic remainder. Indeed the normalized integrand is O(ε² exp(−(A−2δ)t)) for any fixed 0<δ<A/2 using local exponential stability with rate A−δ. This directly gives an ε+O(ε²) cosine coefficient. At fixed κ_b>κ₀, the eigenvalues are strictly left of −A (for real roots use the characteristic polynomial's value κ_b C>0 at −A and the sum of roots less than −2A). The faster local solution is o(exp(−At)), also at its Jordan point. Alternating signs at successive sufficiently late cosine extrema prove the exact nonlinear same-initial-state comparison. The RK4 and finite rational checks are supplementary only.

## originality

PASS

Credit the model, endemic state, Jacobian, attraction and qualitative spiral to the primary article. A distinct Resultary record already displays the same phase interval and spectral-rate optimizer and proves nonlinear endemic-level crossings; those are not treated here as distinct on their own. The supported distinction is the two-objective tuning comparison and, in particular, the quantified nonlinear comparison of two trajectories with the same initial state and equilibrium, for every fixed faster κ_b, using a strict tail-rate separation and a nonvanishing slow leading term.

## value

PASS

Holding equilibrium burden fixed separates transient behavior from limiting prevalence. The spectral and damping-ratio optima show that two well-defined transient objectives prefer different speeds, and the nonlinear result rules out an eventual permanent prevalence ordering for the specified paired perturbations. Infinitely late but vanishing reversals are more informative here than a plotted spiral or equal endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
