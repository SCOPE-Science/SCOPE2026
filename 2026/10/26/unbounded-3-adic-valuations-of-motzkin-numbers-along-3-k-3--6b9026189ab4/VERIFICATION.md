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
# Checks and reproducibility

The proof uses an exact generating-function coefficient, integral Catalan coefficients, Kummer's ternary-carry formula, and a Lucas-theorem unit computation. Each normalization step is stated explicitly in `RESULT.md`.

Running `python3 verify_motzkin.py` reproduces the Motzkin recurrence for \(2\le k\le7\), the residues \(M_{3^k-3}\equiv-3^{k-1}\pmod{3^k}\), the exact valuations, and the necessary Catalan carry inequalities through \(k=8\); successful output is `VERIFY_OK`. These are finite checks only. The general proof is self-contained in the result file.

Independent mathematical validation has not been performed. The result does not address \(3\)-regularity of the full valuation sequence.
