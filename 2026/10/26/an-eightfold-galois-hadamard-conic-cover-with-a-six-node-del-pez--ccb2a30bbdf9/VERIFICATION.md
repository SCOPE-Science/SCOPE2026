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

# Verification details
The accompanying `verify.py` runs exact symbolic equalities in SymPy. It checks the factorization of the quartic branch polynomial, a rational parametrization of the diagonal conic, the identity \(w^2=B(z)\), and the quadratic invariant relation. It verifies that each triple among the four branch-line coefficient vectors has determinant of absolute value \(4\). It prints `VERIFY_OK` on success.

The proof of the full Galois assertion relies on the finite degree-eight map, faithful order-eight action, and characteristic-zero separability. The six \(A_1\) points follow from the pairwise transverse branch-line intersections. These are general theoretical arguments; finite symbolic computations only check their critical algebraic identities. No independent audit or external mathematical certification has been performed.
