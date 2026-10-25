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

# Computation and dependency notes

Invoke `python3 verification/verify_section_rank.py` with a standard Python 3 installation. No downloaded packages, external datasets, or certificates are needed. The script checks five exact-rational ellipsoid parameter tuples against independently computed coefficient matrix ranks; 180 off-center or centered plane sections are compared with area from a separate two-dimensional Gram construction; and the special focal identity is evaluated exactly at twelve rational sphere points. All assertions passed in the preparation of this result.

The central analytic facts are (i) the Euclidean plane-area Jacobian under an invertible linear map, (ii) invertibility of a three-offset Vandermonde matrix, and (iii) odd/even linear independence on the sphere. These prove the finite-rank classification for every ellipsoid, without discretization assumptions. The exclusion of nonellipsoidal finite-rank bodies depends on Fish–Ryabogin–Sun–Yaskin, arXiv:2610.10229, Theorem 4.2. No computational test or review here constitutes an independent audit of that source theorem.
