---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Diagonalizing the SPD quadratic H, the expected inner position recurrence is y_j=q_h y_(j−1)+eta′ gamma x_h with q_h=1−eta′(h+gamma); its unique explicit solution and exponential average mu_K yield phi_K(h)=gamma h/(h+gamma) S_K(eta′(h+gamma)). Completing the Gaussian square gives the ideal gamma h/(h+gamma). Under eta′(M+gamma)<=1, S_K(z) strictly increases, while S_K(z)/z strictly decreases for K>=2 (each polynomial geometric sum decreases, with a genuinely j>=2 term). Thus kappa∞<kappa_K<kappa=M/mu for K>=2. K=1 gives alpha gamma eta′ H and exact raw condition number; exponential averaging forgets the initialization as K→∞, and small-eta Taylor gives kappa_K→kappa at fixed K. Independent 1,000 random recurrence/filter checks with strict comparisons passed; these are finite guards only.

## originality

PASS

The founding Entropy-SGD article defines the exact Gibbs-mean gradient, its finite SGLD inner algorithm and ideal Hessian smoothing, but does not identify this finite-K spectral filter or the sharp K=1/no-improvement and K>=2 interpolation for SPD quadratics. Dziugaite–Roy 2018 addresses PAC-Bayes generalization, not finite estimator conditioning. Similar polynomial filters are standard numerical analysis, so an unindexed prior equivalent derivation remains possible.

## value

PASS

The practical Entropy-SGD procedure estimates its intended smoothing with finitely many stochastic inner steps. Its actual expected conditioning on Gaussian quadratics, as a function of computational inner budget and stepsize, is a natural algorithmic invariant. Exact strict interpolation and the K=1 boundary quantify when ideal-objective smoothing has not materialized; value is limited to expected SPD quadratics and nonoscillatory steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
