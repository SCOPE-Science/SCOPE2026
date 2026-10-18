---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The theorem is proved analytically in RESULT.md. The accompanying `verify.py` is a standard-library-only reproducibility check. It enumerates finite environmental histories, compares direct matrix multiplication against the exact parity factorization, computes exact rational finite-chain covariances, verifies the variance minimizer and tests finite-horizon moment convergence numerically.

In the executed verification run, 4,092 direct-multiplication identities, 12 exact covariance cases, the optimizer checks, and three independently simulated finite-horizon moment comparisons all passed. The executable checks are finite and do not establish the asymptotic limit; the latter follows from the explicitly constructed bounded martingale-difference array, its limiting diagonal quadratic variation, and the fourth-moment uniform-integrability bound.

The model assumes strictly positive biomass in both initial age stages, fixed switching probability strictly between zero and one, and a binary stationary symmetric Markov environment. No independent audit or external validation has been performed.
