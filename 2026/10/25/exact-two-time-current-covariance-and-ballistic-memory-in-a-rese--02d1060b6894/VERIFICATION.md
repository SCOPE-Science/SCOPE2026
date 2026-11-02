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

I reconstructed the stationary velocity-resolved telegraph densities A_sigma=(lambda+sigma*r/v)/4 on x>0, Poisson (0,1) mark thinning, and the no-reset/last-reset renewal decomposition. The conditional velocity free telegraph resolvent integrates to the claimed transform in q=s+r. The zero-lag covariance rho/(2lambda), right slope -rho*(v*lambda+r)/(4lambda), nonzero plateau rho/(8lambda), and branch-point coefficient were checked algebraically, including cancellation of the apparent pole at s=-r. Independent high-precision de Hoog inversion at rho=1.4,r=0.7,gamma=1.3,v=2 gave C(0.2)=0.7524873679115 and C(2)=0.3143533762853, agreeing with recorded simulation-scale values. The bivariate Poisson generating function follows from independent marked anchors, not from assuming independent Q(0),Q(t). The branch asymptotic is fixed-parameter for gamma,r>0.

## originality

PASS

Di Bello et al. 2023 treat this independently reset particle model and one-time annealed/quenched current distributions, but not the evaluated stationary two-time telegraph covariance transform; their initial displacement condition also differs. Jose, Rosso and Ramola treat non-resetting RTP current fluctuations. A Brownian resetting analogue does not imply the finite-velocity gamma-dependent branch coefficient.

## value

PASS

The exact temporal correlation provides a nontrivial explicit diagnostic for hidden anchor disorder: single-time Poisson stationarity coexists with positive long-lag memory. The ballistic slope and t^{-1/2} exponential approach can distinguish reset and tumble mechanisms, rather than repackaging one-time marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
