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

# Verification

The mathematical result is proved directly in `RESULT.md`. Reproduction requires Python 3 with the packages listed in `requirements.txt`; run `python check.py` in the extracted directory. The checker reports `PASS: 145 independent analytical/numerical cross-check assertions` and exits normally.

The checks cover exact zero-lag covariances, the physical-parameter normalization for three triples, positivity and decreasing covariance, long- and short-lag limiting coefficients, direct nested Gaussian-integration evaluation of the central all-time formula, and independently integrated Poisson shot-noise Laplace/cumulant identities. The computational paths and parameter values are contained entirely in `check.py`.

The analytically necessary ingredients are the stationary reset renewal density, two-time no-reset identity, the Gaussian-Laplace integral reductions, conditional ergodic theorem for the infinite independent-resetting product, Poisson Laplace functional, and generalized Dickman first-point factorization. Tests alone cannot certify these infinite-domain statements or determine literature priority. Independent audit has not been performed.
