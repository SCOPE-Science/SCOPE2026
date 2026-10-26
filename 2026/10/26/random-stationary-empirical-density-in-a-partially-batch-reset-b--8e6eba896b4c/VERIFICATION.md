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
# Reproducibility and verification

Run `python3 verify.py` using Python 3 with its standard library. The script uses fixed random seed `20261020` for reproducibility and returns 80 completed assertions on symbolic/numerical consequences. Checks include finite-\(N\) exact covariance versus independently evaluated source expressions, comparison with the thermodynamic covariance, first five cumulants across three reset fractions, the geometric Laplace-renewal identity, seeded sample estimates of mean and variance, the logarithmic Laplace asymptotic, and small-fraction cumulant scaling.

The mathematical results on conditional empirical measures, \(L^2\) energy convergence, the central limit theorem and the infinite-series small-deviation probability are established by the proof in `RESULT.md`. No finite test is presented as an exhaustive or infinite verification. The calculations require no external files, credentials or network access. No independent audit has been performed.
