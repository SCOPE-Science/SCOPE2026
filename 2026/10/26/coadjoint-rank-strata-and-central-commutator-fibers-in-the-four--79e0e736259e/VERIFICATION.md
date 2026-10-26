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
# Computational reproducibility

The primary reproducibility entry point is `python3 artifacts/verify.py`. Its only dependency is the Python standard library. It reconstructs the Kirillov matrices using matrix-unit products, enumerates all six-dimensional functional parameters over four distinct finite fields (including an extension field of characteristic two), and obtains the rank distributions:

- \(q=2\): ranks \((0,2,4,6,8)\) have multiplicities \((1,3,11,29,20)\).
- \(q=3\): \((1,6,48,278,396)\).
- \(q=4\): \((1,9,123,1227,2736)\).
- \(q=5\): \((1,12,248,3764,11600)\).

For \(q=2\), the same code enumerates all \(1024\) possible first matrices and solves the corresponding ten-variable linear equations for the second matrix. It finds \(48640\) pairs with zero additive commutator and \(38400\) pairs with commutator \(E_{14}\). This is exhaustive linear-system enumeration over the entire full triangular algebra, not a sampling claim.

The optional symbolic identity check `python3 artifacts/check_pfaffians.py` requires SymPy and recomputes all size-eight principal Pfaffians of the ten-by-ten matrix over the polynomial ring \(\mathbb Z[a,b,c,d,e,f]\). It verifies precisely six generating polynomials (up to signs) and crucial size-six and size-four witnesses. Both scripts were executed and returned their named success messages.

**Limits.** Finite-field enumeration alone would not establish the theorem for all prime powers; universality comes from the explicit polynomial Pfaffians, algebraic case reductions, exact character orthogonality, and symbolic expressions in the proof. These checks do not constitute independent mathematical validation.
