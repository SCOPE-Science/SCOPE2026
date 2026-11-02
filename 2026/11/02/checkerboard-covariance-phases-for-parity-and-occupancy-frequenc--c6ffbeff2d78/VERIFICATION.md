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

# Reproducibility and limitations

Run `python3 verify.py` in a standard Python 3 environment. The file has no third-party dependencies and returns `VERIFY_OK 144293` when all assertions succeed.

It directly enumerates uniform allocations for three through five boxes and two through seven balls, comparing exact empirical joint moments with the closed covariance expression. It separately evaluates 41 box sizes, occupancy frequencies through 17 and sample sizes up to 149 using rational arithmetic, checking even-frequency negativity, singleton positivity and single-switch signs. It compares the exact finite covariance per box against the stated Poisson-density limit at four positive intensities and two large box sizes for seven frequencies.

These checks are finite corroboration of the explicit theorem and do not prove a general statement by enumeration. The proof's exact conditional mean, unimodality and asymptotic expansion establish the infinite ranges. No independent external audit has occurred. The source comparison is a limited historical-priority assessment, not a guarantee that no earlier equivalent result exists.
