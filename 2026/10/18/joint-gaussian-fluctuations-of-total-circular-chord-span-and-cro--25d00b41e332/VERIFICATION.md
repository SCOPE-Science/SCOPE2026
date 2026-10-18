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

# Reproducible checks and limitations

Execute `python verify.py` with a Python 3 standard-library interpreter. The script constructs all perfect matchings of cyclically ordered \(2n\) points for \(2\le n\le7\), 146,598 matchings in total. Using `fractions.Fraction`, it compares all five exact moments for each size with the formulas in `RESULT.md`. It also exactly integrates the first-order Hoeffding projection polynomials, checks determinant \(1/8640\), and checks linear-regression residual variance \(1/720\). Successful completion prints `VERIFY_OK`.

The script is self-contained, has no file dependencies or network access, and produces no scientific certificate beyond these finite exact tests. The proof of the infinite-dimensional limit uses the general bounded-kernel Hoeffding decomposition and multivariate iid central limit theorem, not enumeration. The mathematical and historical claims have not received independent review.
