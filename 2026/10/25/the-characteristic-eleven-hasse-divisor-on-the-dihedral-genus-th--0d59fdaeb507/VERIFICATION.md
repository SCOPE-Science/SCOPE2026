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
# Reproducible checks

Run `python3 verify_p11.py` from the same directory. This standalone checker uses only the Python 3 standard library to carry out polynomial arithmetic in \(\mathbb F_{11}[a,z]\); no external symbolic-algebra package is required. A successful execution emits `VERIFY_OK`.

It verifies the coefficient extraction for \(1\le i,j\le3\), checks the anti-diagonal Hasse--Witt matrix and determinant, and computes squarefreeness and pairwise disjointness of the exceptional factors using polynomial Euclidean arithmetic in \(\mathbb F_{11}[a]\). It also checks which exceptional values occur already over \(\mathbb F_{11}\) as a finite consistency test.

The general algebraic proof, rather than finite-field enumeration, establishes the assertions for all \(a\) in an algebraic closure. Standard facts used without reproof are the Hasse--Witt coefficient formula for smooth hyperelliptic curves, its interpretation as the semilinear Frobenius action on first cohomology, and the Cartier-operator interpretation of the \(a\)-number. No Newton-polygon classification beyond \(p\)-rank or independent validation is asserted.
