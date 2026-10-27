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
# Numerical verification and analytic limits

The independently written `checker.py` assembles the two quadrature intensity maps on a Frobenius-orthonormal Hermitian matrix basis. Squared-output integrals are evaluated with 14-point Gauss-Hermite quadrature, exact for the relevant squared degree-eight polynomial after factoring the Gaussian. Checked angles: \(0.23,0.7,1.1,\pi/2-0.02,\pi/2,\pi/2+0.02\). In every case rank is eight, the displayed kernel has a residual below \(10^{-13}\), and the determinant matches \(\sqrt2\cos\delta\). An explicit phase-inequivalent pair was checked at distances \(0.01,0.001,0.0001\), verifying its exact sinusoidal upper witness and approximately constant ratio to the distance.

`checker_output.txt` records the actual executable output, and `requirements.txt` lists dependencies. These finite checks do not prove a uniform result for all nearby angles, nor do they assert a certified novelty assessment. The rigorous argument is given in `RESULT.md`.
