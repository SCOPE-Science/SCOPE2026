---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At a complete reset cycle of length L, conditional Brownian area is centered Gaussian with variance 2DL^3/3. The exact Laplace transform E exp[-(D/3)k²L³] has small-k exponent Γ(1-α/3)(D/3)^(α/3)|k|^(2α/3) for 2<α<3; the renewal strong law N_T/T→(α-1)/α turns complete-cycle partial-sum limits into the stated physical-time stable constant. At α=3 the borderline transform 1-φ(k)~(D/3)k² log(1/[(D/3)k²]) yields variance 4D/9 in the sqrt(T log T) weak Gaussian limit. For α>3, E L³=α/(α-3) produces the finite-variance CLT. Stationary equilibrium-age/residual integration gives Cov(X_0,X_h)=D/μ E[(L-h)_+²], evaluating to the asserted h≤1 polynomial and h≥1 power tail. Integrating 2∫_0^T(T-h)Cov dh independently yields 4D/3 at α=3, hence a real factor-three nonuniform-integrability anomaly. Initial and terminal partial excursions have tight stationary area laws and vanish after diverging scaling. Independent direct renewal quadrature tested 15 cases; it is not an infinite proof.

## originality

PASS

The evaluated signed-area stable index, exact characteristic-function constant, borderline weak-vs-moment factor three and specific Pareto covariance do not appear in the materially read reset-Brownian and general resetting-reward source statements. Classical renewal-reward stable/CLT machinery is prior, as is the finite-variance branch; the claimed novelty is the explicit joint specialisation and critical contrast. Best-of-knowledge PASS, not a claim of independently new general stable-limit theory.

## value

PASS

The signed time-averaged displacement is a canonical transport observable, and the exact stable-to-critical Gaussian boundary at α=3 together with the factor-three failure of second-moment convergence distinguishes typical fluctuations from rare long reset gaps. The stationary covariance power law supplies a separate physical-memory interpretation. This is more than a routine application of finite-variance CLT; it identifies a nonuniform-integrability boundary with explicit constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
