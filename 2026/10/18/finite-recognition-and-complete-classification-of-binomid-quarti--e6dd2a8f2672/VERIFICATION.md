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

The source proof reduces all nonnegative integer root shifts to a finite rational enumeration via an inequality valid for every admissible branch. The `verify.py` program enumerates that tree with `fractions.Fraction`, independently solves the final shift by a linear rational equation and compares the two exact result sets. The established exhaustive candidate counts are 83 after \(f_1\mid f_2\), eight after \(f_1\mid f_3\), and five after \(f_1f_2\mid f_3f_4\). The three excluded fractions are printed exactly.

A supplementary calculation checks the first 80 complete generalized-coefficient rows of the five survivors. This calculation is not an infinite proof; unrestricted integrality follows from known binomidness of Pascal-column sequences and closure under termwise product.

To reproduce: `python3 verify.py`. Successful output is contained in `verification_output.txt`. Both files accompany this record. No independent audit or validation has been performed.
