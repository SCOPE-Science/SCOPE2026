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

# Computational and proof checks

Running `python check.py` from the extracted package directory requires Python 3 and NumPy. The script checks column orthonormality, enumerates all distinct row pairs for the construction at \(N=5,6,7,11,23,50,100\), verifies the exact E-optimal value and every maximizing pair's condition number, and confirms an independently optimal condition number of one. It also checks the universal estimate on 4,600 randomly generated orthonormal frames.

These finite checks passed. In the theorem, the infinite quantifiers depend on the row-orthogonality identity, pigeonhole principle, determinant/trace bound, and exact symbolic row-support classification; none depends on extrapolating finite data. The paper does not claim an exact finite-dimensional universal supremum, backward-error bound, or independent validation.
