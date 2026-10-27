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

Use Python with `numpy` and `scipy` and run `python verify.py` in this directory. A completed execution returned `PASS: 674 identity and independent finite-matrix/flux checks`.

The program checks the finite sine-sum against the closed coefficient for all source vertices and ring sizes from 3 through 17, at three positive loss strengths. It independently constructs the magnetic Hamiltonian, solves the continuous Lyapunov equation for exact finite-flux integrated survival, checks its residual, and checks the predicted small-flux values on sizes 5 through 11, with two positive loss strengths and two flux magnitudes. These are numerical corroborations; finite checks cannot establish the universal claim.

The proof's critical analytic checks are: (1) all real eigenvalues at zero flux are the simple Fourier sine dark branches; (2) the two colliding Fourier poles in the rank-one secular equation give the quadratic resonance width; (3) distinct slow eigenvalues prevent nonintegrable slow cross terms after rescaling; (4) roots-of-unity Parseval evaluates the finite positive sum; (5) zero initial dark overlap implies \(O(1)\) rather than a smaller unidentified divergence. The result applies to fixed finite size and positive fixed loss only. Independent scientific audit has not been performed.
