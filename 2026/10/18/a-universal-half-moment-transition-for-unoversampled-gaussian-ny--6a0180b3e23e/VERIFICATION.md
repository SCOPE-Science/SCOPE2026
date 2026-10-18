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

# Reproduction and limitations

Run `python verify.py` in a clean Python environment with the versions described in `requirements.txt`. The code uses deterministic-seeded Gaussian matrices and direct numerical integration of the spherical formulas. `verification_output.txt` contains an actual run of the accompanying script.

The 140 direct matrix cases compare the Nyström residual trace and two unitarily invariant norms with the inverse quadratic form of an independently recovered null vector. Sixteen planar angular integrations confirm the exact \(\sqrt{\lambda\varepsilon}\) formula. Four ranks and several moment orders check leading coefficients; anisotropic two-dimensional leading spectra and the finite-threshold rare-event law are also checked. The checks use tolerances appropriate to numerical quadrature at finite \(\varepsilon\); in particular, the slow critical logarithmic convergence is not artificially presented as high-precision finite-parameter equality.

Finite tests do not prove the formulas for all dimensions, all positive spectra, all moment orders, or arbitrarily small eigenvalues. The accompanying proof gives the required exact-algebra and dominated-convergence arguments. All computations concern real Gaussian sampling in exact-arithmetic mathematical definitions; floating-point computations are only reproducibility checks. Independent audit has not been performed.
