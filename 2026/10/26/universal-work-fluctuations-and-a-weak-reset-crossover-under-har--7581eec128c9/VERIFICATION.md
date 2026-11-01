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

Let q=a^2 and stationary Y_j=aY_{j-1}+xi_j with E xi^2=2Dm and cum4(xi)=12D^2 v. Bilateral moving average gives EY^2=2Dm/(1-q), cum4(Y)=12D²v/(1-q²). Conditional quadratic regression yields Cov(Y_j²,Y_{j+h}²)=q^h Var(Y²); exact geometric covariance summation gives the claimed finite-n work variance and long-run CLT variance. A square-integrable martingale difference decomposition gives the fixed-a CLT. Under n(1-q)->ell>0, normalized stationary AR1 interpolation converges to dZ=-Z/2 dt+dB with stationary normal start; normalized reward is a Riemann integral of Z². Wick covariance integral proves variance 4(ell-1+exp(-ell))/ell² and non-Gaussianity. Independent symbolic algebra checked each variance identity and OU covariance integral. Conditions exclude a=1, infinite second moments and physical-time work counts.

## originality

PASS

Olsen and Gupta (2024) introduced the partial-reset harmonic-work model and derived a-independent mean cost, one-time stationary moments and numerical work plots, while explicitly proposing work fluctuations as a future problem. The exact finite-reset correlated-work variance and path-level joint weak-reset crossover are not in its inspected results. Complete resetting work-fluctuation papers use iid renewal blocks; continuous-time refractory/erasure models have different reset protocols. The AR(1) covariance and OU invariance machinery themselves are classical, not new.

## value

PASS

A physically meaningful work-reliability quantity is quantified beyond the previously established mean-only law. The exact variance separates reset persistence from exploration-time randomness, shows singular loss of self-averaging as a->1, and identifies a non-Gaussian critical distribution despite Gaussian one-time position limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
