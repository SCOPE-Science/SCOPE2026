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

# Reproducibility and limits

Run `python verification/ratchet_counting.py` with NumPy and SciPy available. All three joint-transform crosschecks compare the exact exponential-resolvent/geometric expression with an independent integral over Brownian Gaussian tails conditional on a waiting time. Additional checks differentiate the numerical SCGF root to reproduce exact renewal-reward mean and variance for three nontrivial finite parameter sets. Four edge-window counting fields, at two increasingly large rates each, converge to the limiting implicit SCGF. The analytic third edge cumulant is compared with a finite-difference derivative at three distinct apex scales. All checks passed.

The mathematical proof is in `RESULT.md`. Computations substantiate the algebra, but finite checks cannot prove the large-deviation principle or uniqueness for all real fields. The earlier first/second cumulants are treated solely as independent crosschecks and are not new claims. No independent external audit has been performed.
