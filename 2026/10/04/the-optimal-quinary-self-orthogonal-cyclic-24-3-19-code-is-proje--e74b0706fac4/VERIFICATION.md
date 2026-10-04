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
`artifacts/verify.py` uses only the Python standard library.

It implements \(\mathbb F_{25}=\mathbb F_5(u)\) with \(u^2=3\), checks that \(1+u\) has order \(24\), reconstructs the exact \(5\)-cyclotomic defining set, multiplies the corresponding root factors, and verifies that the resulting degree-\(21\) polynomial has coefficients in \(\mathbb F_5\) and divides \(x^{24}-1\).

The verifier builds the three cyclic generator shifts, checks rank \(3\) and mutual orthogonality, exhausts all \(125\) codewords, verifies the complete weight distribution, checks all generator columns for projective distinctness, derives the generalized Hamming weights, and confirms that the minimum-support complements are exactly one full cyclic orbit. No floating-point arithmetic or optimization solver is used.
