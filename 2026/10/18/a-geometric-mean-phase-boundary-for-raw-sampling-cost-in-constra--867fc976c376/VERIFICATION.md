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
# Verification notes

Run `python3 checker.py` using Python 3 standard library. The program checks the exact coupon-collection dynamic-programming recurrence against the closed-form two-coupon expectation, reconstructs short histories by exhaustive enumeration, checks diagonal-coordinate updates, scans exact rational triples across both sides and at the geometric-mean boundary, and verifies the higher-dimensional Frobenius and raw-draw bounds.

The program reports `PASS: exact-arithmetic checks = 2475` on completion. This verifies the listed finite test cases in exact arithmetic. The analytical proof in `RESULT.md` establishes the infinite families, arbitrary positive singular values, and unbounded asymptotic separation; the program is not an exhaustive verification of those infinite assertions.

Scientific model: independent fixed squared-row-norm raw probes, no floating-point rounding error, and zero-residual draws discarded but counted. No statement is made about total hardware sampling cost, adaptive resampling, or nonorthogonal matrices.
