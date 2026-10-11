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
# Mathematical verification

The accompanying `verify.py` uses NumPy and SciPy to reproduce local constrained maximizers on real positive mass simplices, solve the mean-zero cycle-Laplacian equation, and check the four-cycle exact Green energies \(1/2\) and \(1/4\). It also independently evaluates the top eigenvalue of the symmetrized matrix for the Hilbert exponent \(p=2\). The finite test suite covers dimensions \(2,3,4,5,7\), exponents near and away from two, both signs of small perturbations, and the four-cycle grouped-versus-alternating comparison. Expected output: `VERIFICATION_OK cycle=28 hilbert=12 general=50 total=90`.

Run `python verify.py` with Python 3, NumPy and SciPy. The analytic proof supplies the universal all-parameter conclusion. Numerical minimization tolerances and finite sampling do not certify all parameter values, third-order remainders, or independent scientific validity. Complex fields require no separate optimization because phase alignment is proved exactly in the simplex reduction.
