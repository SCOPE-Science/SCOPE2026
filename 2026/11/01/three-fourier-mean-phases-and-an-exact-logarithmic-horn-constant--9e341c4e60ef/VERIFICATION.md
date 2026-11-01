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

# Reproducibility of the quartic Fourier-mean classification

Use Python 3 with NumPy and SciPy installed, then run `python verify_fourier_quartic.py`. The program independently evaluates the unnormalised axial cosine integral with adaptive oscillatory quadrature, checks beta/gamma constants, and compares nonaxial chord-integral computations with the axis limit and sign symmetry. It reports 17 passing diagnostics under the tested environment.

The exact axis formula is \(H(t)=4\int_0^1 (1-x^4)^{1/4}\cos(tx)\,dx\). The predicted leading endpoint asymptotic is \(4\sqrt2\,\Gamma(5/4)t^{-5/4}\cos(t-5\pi/8)\). The coefficient of the axial pole is \(5\sqrt\pi\), and multiplying by the quartic angular scaling factor \(4/3\) gives \(20\sqrt\pi/3\).

The script verifies finitely many floating-point identities and neither validates the all-frequency estimates nor substitutes for the oscillatory argument in RESULT.md. In particular, the continuity and stationary-phase uniformity in the angular parameter and the global finite-area statement require the analytic proof. The absolute Fourier convention is essential: other conventions rescale the constants.
