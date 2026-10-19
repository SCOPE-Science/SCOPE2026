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

# Reproducibility checks

Run `python3 verify.py` with Python 3 standard library only. The program constructs coefficients from the exact displayed numerator and denominator using an integer recurrence. It independently counts complete directed-pair profiles by enumerating all ternary words of lengths \(1\) to \(11\); it also independently enumerates all nine-entry nonnegative integer matrices with totals from \(0\) through \(12\), applying the Euler-trail degree and connectivity tests. The three computations agree for the common ranges.

The infinite-length theorem depends on the mathematical decomposition of connected balanced and open Euler trails into arc-pair differences, not on the finite tests. The code does not prove originality, code uniqueness, efficient encoding, error correction, or general-alphabet extensions. This is a self-reviewed mathematical result; no independent audit has been performed.
