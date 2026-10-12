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

# Reproducible checks and limits

Run `python3 check_pareto_records.py` using Python 3 standard library. The script enumerates all coordinate rank permutations for sample sizes two through seven and compares observed exact mixed moments with a separate hypergeometric fixed-threshold-count formula (199 exact cells). It additionally verifies binomial averaging for three rational threshold probabilities and the strict sign and exponential bound for every sample size from two to 34 at nine interior parameter pairs. The test examples produce \(-1/16\) and \(-15/128\) for sample sizes two and three when both exceedance probabilities equal one half.

The unrestricted theorem is established by the analytic record-indicator covariance calculation and telescoping bound in `RESULT.md`. Finite rational tests are regression checks, not exhaustive evidence for arbitrarily large samples. No verification for dependent coordinates, moving thresholds, or more than two dimensions is asserted.
