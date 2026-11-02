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
# Reproduction

Run `python3 verify.py` using Python 3's standard library in the same directory as this document. The script directly forms all factorial-ratio coefficients and independently computes each polynomial discriminant using the fraction-free Bareiss determinant of its Sylvester matrix. Tested cases: \((3,1,2)\), \((3,2,2)\), \((5,1,2)\), \((5,1,3)\), \((5,1,4)\), \((7,1,2)\), \((7,1,3)\), \((7,1,4)\).

Actual completed command output:

`VERIFY_OK cases=8 exact_resultant_discriminants=8 coefficient_checks=56 derivative_competitor_checks=40`

For each case the script checks the strict Newton-polygon inequalities, derivative-term valuation dominance, exact discriminant valuation and integral-index identity. The code requires no third-party packages, downloads, or external input. The mathematical proof, not these eight cases, establishes the stated universal claim. No other-prime discriminants, global Galois groups, or independent external audit are certified.
