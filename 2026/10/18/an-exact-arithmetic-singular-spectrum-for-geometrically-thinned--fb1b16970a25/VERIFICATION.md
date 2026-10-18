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

# Verification and reproducibility

Run `python CHECK.py` with the libraries listed in `requirements.txt`. The exact-arithmetic tests verify 720 rational block identities and Meixner three-term recurrences for bases 2, 3, 5 and 7. At dimensions 1600, the symmetric tridiagonal Jacobi eigenvalue tests recover the first eight exact eigenvalues \(1,\ldots,8\), with reported floating-point deviations below \(10^{-12}\) for bases 2, 3 and 5.

The principal infinite-dimensional evidence is the proof in `RESULT.md`: block isometry, closed inverse of the compact triangular operator, essential selfadjointness via Carleman's criterion, completeness and exact recurrence of the Meixner basis, then inversion of the positive Jacobi spectrum. Rational tests and finite truncations alone cannot establish an infinite-dimensional spectrum or exclude further spectral points. No independent audit or external certification has been performed.
