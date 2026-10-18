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

The executable `check_a5.py` is the complete stand-alone exact-arithmetic finite certificate. It takes no input files and uses only Python 3's standard library. Run `python3 check_a5.py`. Its asserted result is `PASS: all 1,711 normalized supports checked over Q; 13 types; 34,220 total.` The checker was actually run successfully.

The checker constructs 60 even permutations of five letters, the full multiplication and inverse tables, the twelve-element five-cycle conjugacy class and inverse test, and all normalized three-element supports. For each support it computes generated subgroup order, pairwise quotient orders, the additional conjugacy-class flag where necessary, tests all three anchor normalizations, builds the exact 60-by-60 integer regular convolution matrix, and performs rational Gaussian elimination. It verifies each of the thirteen classification entries, its support count, and the nullity census after accounting for support translations.

These checks are an exhaustive finite mathematical verification within the stated support domain; they do not provide an independent external audit, a general theorem for other groups, or an original-publication priority certificate. The same review applies only to the single claim recorded in the result, not to any broader spectral or weighted-convolution statement.
