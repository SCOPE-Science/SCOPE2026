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

The analytical proof is in `RESULT.md`. The separate executable `check.py` uses the Python standard library and 180 decimal digits of arithmetic precision. It checks finite critical-point brackets, projective sign comparisons and maximum tests on a 401-point grid, plus displacement and exponential-factor consistency at three fixed skew parameters and five exponents. An actual execution returned `PASS: 12120 deterministic high-precision assertions`.

The calculations are numerical cross-checks only, not an exhaustive proof of uniqueness, an infinite-dimensional certificate, or independent mathematical review. The proof establishes exact global quantifiers and eventual threshold conditions. The row-Hölder expression is a **lower** bound for the matrix norm; the limit is pointwise in a fixed skew parameter. Publication priority remains unverified independently.
