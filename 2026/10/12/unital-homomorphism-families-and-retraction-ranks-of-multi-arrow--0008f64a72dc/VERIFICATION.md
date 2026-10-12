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

The supplied `checker.py` is a Python 3 standard-library program. Run `python3 checker.py` in a directory containing that file. It constructs the multiplication table of the triangular two-vertex path algebra explicitly and exhaustively enumerates all possible images of a basis in the test configurations, checking each table relation and unit preservation before counting maps. For equal source and target dimensions it independently checks composition-idempotency and linear rank. The test cases are \((r,s,q)=(1,1,2),(1,2,2),(2,1,2),(2,2,2),(1,1,3)\). For \((2,2,2)\), there are exactly 70 homomorphisms and the rank multiplicities of idempotent endomorphisms are 2 (rank 1), 4 (rank 2), 12 (rank 3), 1 (rank 4). Formula-only checks of Gaussian coefficients include \(n=1,\ldots,7\) and prime-field sizes 2, 3, 5. The final program line must be `VERIFY_OK`.

The checker does not enumerate all maps in large dimension, all extension fields, or all infinite fields. Those quantified results follow from the algebraic classification proof rather than experimental extrapolation. The checker has no external data inputs or dependencies.
