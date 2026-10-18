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
# Reproduction and scope

Run `python3 checker.py` using Python 3 standard library. The reported execution passed 103624 individual exact-polynomial, exact-rational matrix and finite-dimensional numerical assertions. The generator identity, the reversal matrix, the tridiagonal square and the critical sine basis were also checked independently by direct analytic derivation. The proof of the fixed-parameter limiting spectral measure uses rank-one interlacing and control of normalized odd moments. The proof of the exponentially small boundary mode uses a convergent rank-one Hilbert–Schmidt scaling limit for the exact inverse, not extrapolation from numerics.

The checker covers selected parameters and sizes; it is not an infinite proof. Historical priority remains potentially limited by an inaccessible 2016 matrix-spectral paper. No independent audit has been performed.
