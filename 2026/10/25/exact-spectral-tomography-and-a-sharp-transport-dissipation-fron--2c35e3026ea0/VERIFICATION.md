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

The complete theorem and proof are in `RESULT.md`; `verify.py` provides supplementary calculations. Execute `python verify.py` with Python 3 and NumPy. The program requires no downloaded source or saved measurement data.

The exact test cases use \(D_1=0.7\), \(D_2=1.3\), \(L=2\pi\), and \(V(z)=\cos z+0.4\cos(2z+0.37)\). The checker derives Fourier weights, checks the Haar spatial force-square integral, validates a time-integral identity for the stationary force autocorrelation, verifies the thermodynamic coefficient and strict multi-mode upper bound, and constructs its sinusoidal equality witness. It compares reconstructed exponential spectral components with the direct covariance curvature and compares the long-time diffusion gain with the exact Haar potential variance.

A separate seeded Euler–Maruyama simulation integrates the **two original particle equations** with independent driving noises, the physical common force, and a relative position updated by the noise difference alone. It samples 30,000 initially uniform pairs, 900 steps over a physical time of 1.5. The expected cross-displacement covariance is approximately \(0.622446828534\) and the seeded simulation yields approximately \(0.639177066138\). The expected entropy-production rate is approximately \(1.8021978022\). All implementation assertions passed when executed.

The proof, not the stochastic simulation, establishes the infinite Fourier sum, all-time conclusions and uniqueness of maximizing potentials. Monte Carlo error and time discretization remain finite; this checker does not certify any continuum statement or independent audit. Ideal noiseless infinite-time inverse identification is not a practical stability theorem. The literature comparison and limitations are given in `REVIEW.md`.
