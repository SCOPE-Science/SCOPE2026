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

Run `python3 verify.py` with Python 3 standard library. It enumerates each labeled tournament exactly for sizes 2 through 6, computes the outdegree-count histogram on every orientation, accumulates exact rational means and second moments, and checks every covariance entry against the theorem. It also verifies each binomial marginal and exact expected Pearson statistic. The program stops on any failed assertion and prints `VERIFY_OK` only after all checks.

The analytic proof, not bounded enumeration, establishes the results for every integer size. No distributional chi-square claim or independent audit is made.
