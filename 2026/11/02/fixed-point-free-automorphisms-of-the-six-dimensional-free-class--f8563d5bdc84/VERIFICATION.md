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

# Reproducibility and scientific limits

Run `python3 verify_fpf_free_two_step_rank3.py` in a directory containing the supplied code. The expected output is included in `fpf_rank3_check_output.txt`. The checker implements finite fields of orders \(2,3,5\) by modular arithmetic and the field of order \(4\) as a quadratic extension. It exhaustively enumerates \(q^9\) coordinate matrices in all four cases; for each invertible matrix, the checker independently evaluates the original determinant conditions. For a bounded sample of matrices, it additionally forms the induced exterior-square action and tests rank six of the explicit Lie-automorphism matrix minus the identity under three central shears. It verifies admissible quotient-action counts \(48,4860,98048,922000\).

The code tests finite cases, not the entire infinite family. The proof derives the general count through a complete rational-canonical partition and exact class-size formulas. Scientific limitations and priority uncertainties are given in RESULT.md and REVIEW.md. No independent audit has been performed.
