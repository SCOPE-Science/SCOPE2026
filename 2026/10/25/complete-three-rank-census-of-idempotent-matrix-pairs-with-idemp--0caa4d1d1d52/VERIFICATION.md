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

# Finite arithmetic verification

The standalone file `verify_idempotent_products.py` uses matrix multiplication, Gaussian elimination, idempotence tests, finite-field arithmetic and a second optimized binary-matrix implementation. Run `python3 verify_idempotent_products.py` from the directory containing this file. There are no external Python dependencies.

Exhaustive rank-triple comparisons were carried out at \((n,q)=(1,2),(2,2),(3,2),(2,3),(3,3),(2,4),(2,5),(4,2)\); in particular the arithmetic implementation of \(\mathbb F_4\) uses the field relation \(\alpha^2=\alpha+1\). Each observed rank-triple count agreed with the formula. The \((4,2)\) case covers 802 idempotent matrices and 375244 qualifying ordered pairs, across 35 nonempty rank triples. Further exact-integer coefficient and commuting-ratio checks covered dimensions 1 to 7 and field orders 2, 3, 4, 5, 7.

Expected success line: `VERIFY_OK_IDEMPOTENT_LINEAR_PRODUCT_RANKS`.

No finite test is claimed to exhaust all dimensions or field orders; the universal statement rests on the explicit block-algebra proof in RESULT.md. An independent mathematical audit has not been performed.
