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

# Verification instructions

Run `python3 verify_split_octonion_zero_products.py` with a standard Python 3 interpreter. The checker requires no external packages. It implements the original Zorn multiplication, finite-field arithmetic, and elementary Gaussian elimination independently of the closed formula. It enumerates every possible first factor in \(\mathbb F_2\), \(\mathbb F_3\), and the nonprime field \(\mathbb F_4\), calculates the exact nullity of the combined left- and right-product map, checks each norm/trace stratum and sums all kernel sizes. The complete expected output is in `verification_output.txt`.

The exhaustive finite tests validate those particular fields only; the argument over arbitrary fields, the four-component classification, and the motivic identity depend on the complete proof in `RESULT.md`. No independent human or external certification has been performed. The analyzed object is the reduced variety of ordered pairs satisfying both multiplication orders, not the original possibly nonreduced equation scheme.
