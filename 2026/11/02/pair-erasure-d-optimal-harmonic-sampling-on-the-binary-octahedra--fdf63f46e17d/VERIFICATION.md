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

# Verification of the exact two-erasure determinant census

Run `python check_erasure.py` with Python 3, NumPy, and SymPy. The program constructs all 48 quaternionic coordinates and 24 antipodal representatives, computes degree-12 Chebyshev values, classifies every unordered pair using relative quaternion multiplication, forms the exact integer Gram matrix, and checks its identity with the 4-cycle Cayley adjacency matrix. It checks the entire exact 24-by-24 characteristic polynomial and rational inverse, all 276 class-dependent inverse entries, the determinant-factor numerators, and one directly evaluated 22-by-22 determinant in each class. Executed successfully: all assertions passed.

The mathematical proof in RESULT.md independently uses the explicit character table of \(S_4\), Chebyshev recurrence, and Jacobi's complementary-minor identity. The checker uses floating point only to classify the finitely many explicit quaternion-coordinate types; all determinant and spectral comparisons after this construction are exact rational/integer equalities. The result does not claim exhaustive previous-literature coverage, external audit, or independent mathematical certification.
