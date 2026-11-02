---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

All parameters 0<alpha<1, eta>0, m>=1, real deterministic observation times, two-sided stationarity and distinction from the preceding Galton–Watson explosion limit are explicit. Original Theorem 2.3 supplies CSBP u_r(theta), immigration PPP rate alpha/(1-alpha), independent Gamma(1-alpha,1) masses and stationary Gamma(alpha,1) law. By PASTA and independent future Poisson increments, the pre-last-arrival Gamma(alpha,1) plus independent new Gamma(1-alpha,1) is exactly Gamma(1,1), giving (3) and conditional mean exp(-a/alpha). Upper log tail follows Markov bound exp(-eta/alpha). For the lower log tail the latest immigrant C_r has Laplace (5), is positive, and exponential-Markov at theta=exp((a+eta)/alpha) yields exp(1+a+eta-eta/alpha); integrating exp(a) against backward age Exp(1/(1-alpha)) gives exactly 1/alpha. The rate-1 plus rate-alpha/(1-alpha) decomposition couples ages with mismatch probability alpha at each time; union bound yields (1) and all finite-dimensional limits. The no-arrival/last-arrival split establishes kernel (2) and generator Gf=f' + f(0)-f on smooth tests. This proves fixed-time laws, not a path-space theorem; 4 independently chosen alpha quadratures and a native-Git tree reconstruction corroborate premises only.

## originality

PASS

Best-of-knowledge distinct parameter-singular finite-dimensional law and explicit all-alpha coupling for the fixed model of Harris–Johnston–Pardo. The fixed-alpha paper supplies the model but not the alpha-to-zero multi-time assertion; large-tail immigration and fixed-mechanism long-time theorems are not direct covers. Primary 2022 full text remains an identified access-related priority risk, not evidence that the claim is covered.

## value

PASS

The exact small-shape Gamma marginal would only show Exp(1) at one time, but the stationary family evolves over a singular 1/alpha scale. The full jointly coupled age-reset Markov limit, explicit transition kernel and uniform exponential-in-1/alpha tracking estimate provide a natural, reproducible structural description of rare immigration bursts in the fixed branching model. This is a nontrivial process-level asymptotic and useful benchmark for rare-arrival limits, not merely a normalizing substitution or a small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
