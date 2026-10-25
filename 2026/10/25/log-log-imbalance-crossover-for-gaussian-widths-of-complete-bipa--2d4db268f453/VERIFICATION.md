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

The reproducible standalone file `check_width.py` computes all subset-support widths and both sides of the identity (1) for dimensions 2--8 and verifies them on 520 deterministic sampled vectors. It independently evaluates the limiting mean and variance from convergent gamma-log formulas and compares those values with 60,000 random truncated exponential-series samples (38 terms). A successful run prints `EXACT_SUPPORT_PASS` and `POISSON_MOMENT_PASS`. These finite calculations and random diagnostics are auxiliary; the analytical Gaussian extreme-point-process and infinite-weight-tail arguments establish the limit. No independent audit has been performed.
