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

# Verification record

The complete proof, exact definitions, limit regimes, and limitations are contained in `RESULT.md`. The standalone `CHECK.py` requires only Python 3 and its standard library: `python3 CHECK.py`.

The test performed 1,955 successful assertions: exact rational Markov-state transition and normalization checks for batch sizes one through six, round counts through nine; exact comparison of means, variances, and covariances with a separately implemented recurrence; limiting covariance checks; and finite Poisson-coupling bound checks. The Gaussian convergence and total-variation asymptotics are proved through martingale and coupling estimates, rather than relying on test coverage. Independent audit has not been performed.
