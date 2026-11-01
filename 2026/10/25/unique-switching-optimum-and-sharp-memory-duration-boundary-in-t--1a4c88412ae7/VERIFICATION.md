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

Reconstructed the exact OU hazard h_tau(t)=D(1-exp(-t/tau)), strictly increasing from 0 to D, and F(gamma)=beta_s/2*(gamma+c)M0. Integration by parts gives F_prime=(beta_s/2)*int t*(h_tau(t)-c)*exp(-gamma*t)*G_tau(t) dt. For 0<c<D this integrand has exactly one t sign change. Splitting negative early and positive late contributions, their positive ratio N_gamma/P_gamma has strictly negative log derivative since its positive-part time mean exceeds t0 and its negative-part time mean falls below t0; this ratio tends to 0 as gamma grows. Thus F_prime crosses 0 at most once and, when c<c_*=M0/M1, crosses from positive to negative exactly once. For c>=D F_prime is strictly negative. Since K=1/F the optimizer classification and strict monotonicity follow. For tau increasing, G_tau2/G_tau1 is a strict likelihood-ratio increasing function of t, making M1/M0 strictly increase and c_* decrease. The limits follow by dominated convergence at tau->0 and Gaussian t=sqrt(tau) scaling at tau->infinity. At gamma=b/tau and tau->0 the derivative sign reduces to (1-kappa)/b^2-1/(b+1)^2, whose unique zero is b0=sqrt(1-kappa)/(1-sqrt(1-kappa)); bracketing plus previously proved uniqueness yields the optimizer scaling. Independent SciPy quadrature reproduced strictly descending c_* at five tau values, unique positive gamma*=0.2273477 at (D,c,tau)=(1,0.5,3), and tau cutoff 4.22146244017. Numerical cases only corroborate these universal analytic steps.

## originality

PASS

Best-of-knowledge comparison of the complete asserted mathematical implication against actual primary material read and documented searches. The original same-object source reports a sufficient condition in its accessible abstract; no prior necessary-and-sufficient global optimization theorem was established, but its full text was inaccessible and is explicitly a residual risk.

## value

PASS

The source OU linear-response model motivates the competition between switching amplification and memory suppression but provides only an existence criterion and examples in accessible primary abstract. The exact necessary-and-sufficient all-parameter classification, monotone unique correlation-duration threshold and sharp singular 1/tau optimizer scale answer a natural model-specific timescale question; no nonlinear stability claim is smuggled in.

The dated certificate retains the supplied scientific assessment, sources and limitations.
