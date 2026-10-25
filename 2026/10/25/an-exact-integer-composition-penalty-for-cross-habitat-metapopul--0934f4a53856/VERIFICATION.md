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

The proof reduces the full, symmetric, block-constant colonization matrix to a two-dimensional invariant subspace, factors the spectral threshold as a positive ratio, minimizes that ratio on the continuous positive line, and then proves an exact identity for the integer rounding excess.

The reproducible `check.py` uses only the Python standard library. It independently diagonalizes full matrices by Jacobi rotations and compares their eigenvalues with the formula obtained from the invariant block. It checks 1,200 randomly selected finite network configurations, 21,309 eigenvalue/threshold comparisons, all integer composition minima against an explicit scan, and the exact five-patch example by rational arithmetic. Execute `python3 check.py`.

The numerical tests are not a replacement for the proof; in particular they do not verify arbitrary real parameters or all finite network sizes. The claim concerns linearized capacity-supercriticality, not survival with positive probability for all time in a finite absorbing stochastic process. Some historical full texts remained inaccessible and independent mathematical validation has not occurred.
