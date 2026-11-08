---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The stationary law is a geometrically aged beta-binomial urn: regenerate at rate r, conditional variance k/[4(n+1)(n+k)], conditional martingale identity gives covariance (1-r)^h Var(X). The de Finetti representation supplies the Gaussian weak- and intermediate-reset regimes; for nr→∞, jumps of scaled martingales are ≤sqrt(r), predictable bracket →t/4, Bernoulli reset epochs converge to unit-rate Poisson, giving the stationary J1 Brownian-reset process with generator f''/8+f(0)-f. Ages scaled by r converge to Exp(1) and its Gaussian variance mixture is Laplace of characteristic function (1+s²/8)^−1. Even n, balanced deterministic resets, r→0 and compact finite horizons are essential. Independently recalculated conditional beta-binomial second moments; fixed-n tests do not establish functional convergence.

## originality

PASS

Best-knowledge PASS: Classical Pólya/Eggenberger urn without resets is conditionally beta-binomial; Evans–Majumdar Brownian motion with resetting has a stationary Laplace density. Neither is the exact independent full-reset finite-urn chain or its crossover. Dean proves growing-composition functional urn CLTs without independent state resets; they supply an ingredient for the Gaussian limit, but do not determine the regenerative stationary three-regime theorem.

## value

PASS

The exact stationary reinforcement-reset law and its three sharply separated Gaussian, normal-mixture and Laplace regimes are a natural nontrivial scaling classification. The process-level limit identifies a physical Brownian-reset mechanism, beyond the already known Brownian Laplace marginal; exact temporal covariance is additionally useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
