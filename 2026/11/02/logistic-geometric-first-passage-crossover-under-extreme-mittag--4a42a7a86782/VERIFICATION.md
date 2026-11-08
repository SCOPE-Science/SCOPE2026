---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The source uses the correct rate law E[e^{-s lambda}]=1/(1+s^alpha). Rescaled log rate W_alpha=alpha log lambda has limiting survival 1/(1+exp(z)), derived by dominated convergence from the stated first-type Mittag-Leffler integral. An independent scipy quadrature of that integral at alpha=.20,.10,.05 and z=-.6,0,.6 converged numerically toward the logistic tail, with errors decreasing in alpha. For finitely many slow blocks the integrated jump clock divided by x_alpha^2 is exponentially tiny, and Doob maximal inequality prohibits reaching zero or moving a macroscopic fraction of x_alpha. A fast block has exponentially huge jump clock, and a half-line heat-kernel survival bound forces absorption within eta*tau_alpha. The intermediate log-rate band is negligible by logistic continuity; independent blocks then yield a geometric first-fast-block time. Weak convergence at all noninteger continuity points and bounded-transform convergence follow. No expectation convergence or uniformity in kappa is inferred.

## originality

PASS

Closest paper by Levit and Reuveni establishes the same rate-reset walk, spectral survival and mean transition but the accessible text discusses fixed-distance mean and survival tails, not an exponentially scaled distance/interval joint weak limit. Existing doubly stochastic random-walk work develops fixed distributions and interval exits. Best-of-knowledge PASS with high risk because supplementary full text was not accessible after arXiv/OA attempts and authorized institutional VPN disconnection.

## value

PASS

The exact logistic-to-geometric crossover identifies a natural singular scale x^2/tau ~ exp(kappa/alpha), demonstrating that a first-passage time collapses into the first exceedingly fast refresh interval; this is a genuine distributional scaling law relevant to fluctuating-rate transport rather than a renamed mean asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
