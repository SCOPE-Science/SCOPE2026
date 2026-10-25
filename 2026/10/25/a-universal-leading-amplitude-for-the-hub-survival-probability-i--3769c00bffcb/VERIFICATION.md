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

# Reproducible scientific checks

Run `python verify_wheel.py` with Python 3; the program uses only the standard library. The algorithm independently enumerates occupied-vertex masks and available-edge transition rates, calculating exact rational absorption probabilities on rims of lengths 3 through 10 at spoke-rate ratios 1/2, 1, and 2. It compares the 24 finite graph results with the analytic positive-rate path recurrence. Separately, 108 exact-rational coefficient comparisons confirm the hypergeometric generating-function ratio through order 35. Coefficient signs and high-precision dominant-root/asymptotic checks yield 138 successful assertions. The finite enumerations, numerical root approximations, and test logs do not prove claims for arbitrary graph size or arbitrary real rates; the mathematical proof in RESULT.md addresses those quantifiers.

The positive-rate assumption is essential. No probabilistic claim about the zero-rate boundary is included. The cited foundational general graph paper was not inspected in full, leaving the bibliographic coverage limitation described in REVIEW.md. Self-review passed; independent audit has not been performed.
