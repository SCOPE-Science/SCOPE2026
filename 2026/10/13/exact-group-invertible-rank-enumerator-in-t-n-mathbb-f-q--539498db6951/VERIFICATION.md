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

`verify.py` is a standard-library verifier for the finite consistency checks. It constructs every upper-triangular matrix in the stated small fields, computes rank by exact finite-field Gaussian elimination, squares the matrix, and tests \(\operatorname{rank}(A^2)=\operatorname{rank}(A)\). It compares the resulting rank histogram with
\[
\binom nr(q-1)^r q^{\binom n2-\binom{n-r}2}.
\]

The exhaustive cases are \(q=2\) through \(n=5\), \(q=3\) through \(n=4\), \(q=5\) through \(n=3\), and \(\mathbb F_4\) through \(n=3\). The non-prime field uses an explicit implementation of \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The script separately checks both closed-form induction recurrences through dimension \(12\) for several field orders.

A successful run begins with `VERIFY_OK`. These computations do not constitute the proof for unbounded \(n\) or arbitrary prime powers; that proof is the rank/recurrence argument in `RESULT.md`.
