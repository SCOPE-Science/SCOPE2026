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

The claim concerns the smooth projective normalization of the equation stated in RESULT.md and its geometric Jacobian. Exact computations use \(\mathbb F_3\)-coefficient arithmetic and no floating-point data.

Run the following commands in the extracted package directory:

```
python3 verify_cartier_polynomial.py
python3 verify_cartier_binomial.py
python3 verify_fourth_iterate.py
```

The first computes each Cartier block by polynomial multiplication, extraction of exponents congruent to two modulo three, exact polynomial division, and elementary row reduction. The second computes all block coefficients by binomial sums, independently row-reduces those matrices, checks the entire 81-row `cartier_blocks.csv` certificate, and asserts rank 222. The third computes the fourth Cartier iterate on the differential basis and asserts that every block vanishes. The first two scripts agree on genus \(324\), rank \(222\), and \(a\)-number \(102\). The genus and basis completeness additionally rely on the explicit ramification and valuation argument in RESULT.md; the scripts do not constitute independent assessment of that geometric proof. No external independent audit has been performed.
