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

# Reproducibility and limits

The supplied `verify.py` uses standard Python only. Running `python verify.py` performs exact prime-field arithmetic and prints `VERIFY_OK_QUADRATIC_JET_DIFFERENTIALS` on success.

It reconstructs the algebra's monomial action on the quadratic basis and the full derivation matrix from its degree-one and degree-two coefficients. It exhaustively checks *all* square-zero derivations over \(\mathbb F_2\) and \(\mathbb F_3\) when \(d=2\), finding rank polynomials \(1+21T+66T^2\) and \(1+104T+624T^2\), respectively. Separately, it exhaustively enumerates all 1,024 compatible quadratic terms for a fixed nonzero rank-one square-zero linear part when \(d=3,q=2\), obtaining operator-rank frequencies \(256\) at rank \(3\) and \(768\) at rank \(4\). It verifies a second characteristic-two canonical induced-complex rank and normalizations for dimensions 2 through 5 and field orders 2, 3 and 4.

The code's finite elimination arithmetic is over the prime fields in the exhaustive and canonical tests; counts labeled \(q=4\) in formula normalizations are integer-polynomial evaluations, **not** independent extension-field enumerations. None of the finite checks proves the all-prime-power statement. The complete proof uses the two-block derivation form, characteristic-two chain-map decomposition and Gaussian rank enumeration, as given in `RESULT.md`. Independent mathematical audit has not been performed.
