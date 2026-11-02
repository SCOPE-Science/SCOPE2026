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

The symbolic verifier `verify_symbolic.py` reconstructs the matrix of coefficients of the defining degree-eleven polynomial, checks the \(3+2\) block decomposition and determinant \(T\), expands the separability resultant over characteristic three, and checks transverse-derivative identities and examples. It completed with `SYMBOLIC_GENUS5_CHAR3_CERTIFICATE_OK`.

The separate stdlib-only verifier `verify_fields.py` uses polynomial Euclid to test squarefreeness rather than the resultant expression, reconstructs the Hasse–Witt matrix directly, and computes five Frobenius-twisted factors over finite fields. It completed with `GF3_EXHAUSTIVE_CARTIER_OK`, `GF9_EXHAUSTIVE_CARTIER_OK`, and `INDEPENDENT_GENUS5_CHAR3_FIELD_CERTIFICATE_OK`.

Over \(\mathbb F_3\), there are 20 smooth triples with \(3\)-ranks \(4:15,2:4,0:1\), and 7 singular triples. Over \(\mathbb F_9\), there are 656 smooth triples with ranks \(4:589,2:60,0:7\), and 73 singular triples. These checks are not a proof of an infinite algebraic-closure classification; the block-matrix proof supplies that argument. The code requires Python 3; SymPy is additionally required by the symbolic verifier. Independent external audit has not been performed.
