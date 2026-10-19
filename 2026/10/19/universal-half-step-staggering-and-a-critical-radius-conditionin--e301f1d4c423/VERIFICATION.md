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

# Verification of the two-ring theorem

The standalone executable `verify.py` uses NumPy to form \(F^*F\) directly from \(2n\) complex monomial evaluations, without constructing it from the proposed two-by-two blocks. It independently computes the proposed traces and determinants and compares their eigenvalues.

Observed checks: 160 direct diagonalization comparisons for \(n=2,\ldots,9\), including two equal-radius configurations, radii on both sides of one, and different phases; maximum absolute eigenvalue difference \(5.773159728050814\times10^{-15}\). Another 480 angular optimizations with nonconstant Bombieri weights checked spectral endpoints and log determinants; all passed. Twelve fixed-radius series for \(r=0.35,0.65,0.85\) confirmed the analytically predicted scaling trend. The largest absolute log-determinant comparison error, \(3.4722660302577424\times10^{-8}\), occurs with nearly singular numerical matrices; it is not an exact error certificate.

Run `python verify.py` in an environment with Python 3 and NumPy. The machine-readable recorded output is embedded as `verification_output.json`.

Numerical experiments do not establish assertions for arbitrary dimension, positive weights or radii. General correctness is supplied by the exact Fourier-block proof and its asymptotic argument. No independent scientific validation has been performed.
