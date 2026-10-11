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

# Verification

Run `python3 check_hyperbola.py` with standard Python 3. It constructs prime fields of sizes 3, 5, 7, 11, and 13 and the nonprime field of order 9 from the irreducible polynomial \(T^2+1\) over \(\mathbb F_3\). The test exhaustively constructs every ordered-pair fiber in each selected field and confirms that the origin is the only fiber of size above two. For each field it confirms the coefficient, tests twenty seeded complex integer-valued vectors against both raw collision and direct Fourier fourth moments, verifies every term of the global defect formula is nonnegative and sums to the actual difference, and tests a nonconstant-phase equality case.

Actual execution completed: all six fields passed; 120 random signals and six equality cases were checked. Comparisons involving floating-point characters use explicit numerical tolerance. The universal proof needs only exact algebra, characteristic odd, root uniqueness, arithmetic–geometric mean, and triangle inequality; these experiments are not an exhaustive proof for untested field orders. No external independent audit or formal certification was conducted.
