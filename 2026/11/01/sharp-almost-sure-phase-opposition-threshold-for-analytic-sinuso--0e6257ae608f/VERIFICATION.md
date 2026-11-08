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

For F_h(z)=z+hKA sin z modulo 2π, u=A sin z, w=Ku, q=u^TKu, Taylor integral identity separates V(z)−V(F_hz) into h(1−hΛ/2)q + (h²/2)(Λq−w^TAw) + h²Σ_i a_i w_i²∫(1−t)(1+cos(z_i+thw_i))dt, all nonnegative when h≤2/Λ and strictly positive whenever sin z≠0 (K invertible and nonconstant cosine segment). Compactness and vanishing increments force every orbit to converge to one of finitely many binary equilibria, even at equality. All other binary equilibria have expanding derivative direction by symmetric congruence. Analytic nonzero Jacobian determinant at zero makes all preimages of null sets null; an endomorphism center-stable theorem gives null basin of each unstable fixed point despite singular derivatives. For h>2/Λ p* derivative has eigenvalue <−1, so same N^-1 argument makes its basin null. Direct independent numerical integration at critical parameter for nontrivial points verified Taylor equality to high precision; analysis does not infer measure theory from numerics.

## originality

PASS

The directly relevant 2026 Buescu–D’Aniello–Oliveira source proves descent only for 0<h<2/Λ, and full measure only for the diffeomorphic interval h<1/Λ; a supercritical local sink-loss result alone does not imply basin measure zero. Muşat–Boumal 2026 provides general noninvertible center-stable and Luzin N^-1 tools, which are credited, but no source supplied the cosine strict-remainder identity at the critical h and complete global phase-family threshold. Published neighboring oscillator records concern different coupling or critical-relaxation regimes.

## value

PASS

The inclusive threshold 2/Λ for almost-everywhere attraction of a prescribed phase-opposition state is a natural stability boundary for positive-weight tree phase networks. Exact endpoint descent persists when the usual quadratic descent coefficient vanishes; noninvertibility occurs at smaller steps than loss of almost-global attraction. Closing this measure-theoretic gap is meaningful beyond a local multiplier check and does not purport to classify supercritical attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
