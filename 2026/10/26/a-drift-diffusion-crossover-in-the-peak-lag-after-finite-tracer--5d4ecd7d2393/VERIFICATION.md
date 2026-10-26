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

The self-contained `check_peak.py` script uses only Python's standard library. Run `python3 check_peak.py` from the same directory. The computation tests 2,000 seeded parameter points against shifted log-density equality, expected crossing direction, mode position and positive peak-time sensitivity. Separate 300-pair checks cover strict lag decrease with increased drift and 300 duration comparisons cover simultaneous decrease of lag and increase of peak time. It prints long-release asymptotic residuals and crossover ratios and checks an explicit two-parameter example.

These floating-point checks are finite consistency tests, not an exhaustive proof of uniqueness or of limits over infinitely many parameter values. The proof in `RESULT.md` uses an exact one-positive-zero quadratic derivative, strict unimodality, an implicit-function argument and controlled root-equation asymptotics. No independent audit or external certification has been performed.
