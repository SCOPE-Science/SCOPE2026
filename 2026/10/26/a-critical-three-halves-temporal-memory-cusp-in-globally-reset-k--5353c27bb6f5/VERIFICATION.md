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

From the frozen RESULT.md: the exact conditional-on-reset split gives C(t)=e^(-lambda t)Cov(f(A),f(A+t)), not just the one-point renewal law. Verify explicitly the Riccati/logistic solutions f= rho0 e^(-k t)/sqrt[1+K rho0²(1-e^(-2kt))/(2k)] subcritical, f=q/sqrt[1+(q²/rho0²-1)e^(-(K-2sigma)t)] supercritical, f=h(t+c)^(-1/2) critical. Expanding bounded denominator terms uniformly over A>=0 gives the stated pure exponential rates and strictly positive prefactors (same/opposite monotonicity compensated by b_+ sign). At the critical point the age-independent h t^-1/2 term cancels; -h(A+c)t^-3/2/2 survives, with integrable Taylor remainder O((A+c)^2 t^-5/2) since A exponential. Direct gamma integration gives B_c and positivity by strictly negative Cov(f(A),A). Constant branch rho0=q is handled exactly; K=0, rho0=1 and small positive rho0 are within stated quantifiers. Independent 9-parameter numerical checks include 27 ODE derivative residuals, positive prefactors, two incomplete-gamma-vs-integral comparisons, the equilibrium-constant case and asymptotic ratios; these are corroboration, not infinity proofs. Reconstructed seven-blob Git tree matches exact assigned source-tree SHA-1.

## originality

PASS

Best-of-knowledge: the exact reset-age identity is standard regenerative machinery and the cubic OA flow is already known; however, in materially read original and broader primary literature, the theorem's precise centered stationary TWO-time cross-covariance, its sharp switch from off-critical pure exponentials to e^{-lambda t}t^{-3/2} exactly at K=2sigma, positivity and incomplete-gamma prefactor are not stated. The physical and mathematical observable is not equivalent to the equal-time C(t) in Acharya et al. This PASS is qualified by possible implicit general regenerative-theorem coverage and incomplete inspection of Das–Gupta 2018.

## value

PASS

The long-lag autocovariance of collective coherence is a natural dynamic observable, not determined by an instantaneous stationary order-parameter distribution. It has a mathematically sharp critical signature at the classical OA threshold K=2sigma: exp(-lambda t)t^-3/2 rather than an off-critical pure exponential or uncentered t^-1/2 response. The positive exact incomplete-gamma coefficient and explicit exceptional zero path make the classification usable in temporal inference and comparison with reset-ensemble simulations. Although the covariance reduction itself is standard, quantifying the critical cancellation and all regimes is a motivated exact invariant, not an arbitrary parameter slice, mere normalization, or a known table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
