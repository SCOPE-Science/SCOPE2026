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

The complete proof is in `RESULT.md`. A standalone Python checker `check_latitude.py` uses fourth-order coordinate moments to independently construct full ambient and latitude Gram matrices, then tests their generalized spectra and global design branches on finite dimension and height grids. Run `python check_latitude.py` with NumPy and SciPy available. The checker passed 834 tests; finite computations cannot certify the global all-dimensional statement. The analytic proof supplies that statement. Normalization, complex harmonic coefficient range, degenerate heights, and the distinction between E-optimal frame bound and condition-number optimality are explicit.
