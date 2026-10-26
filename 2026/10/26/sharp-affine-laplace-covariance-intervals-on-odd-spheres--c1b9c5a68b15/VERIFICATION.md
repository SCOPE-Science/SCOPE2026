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

The analytical derivation begins from a finite trigonometric support identity for the Gegenbauer weight and uses the first \(m\) vanishing even derivatives at the origin to determine an exact rational Laplace transform. Parameter differentiation gives every Schoenberg coefficient. The two coefficient extremizers are the constant mode and the asymptotic even-frequency tail; positivity, excluded-parameter witnesses and strict positivity are proved at all degrees.

The accompanying `verify_spherical_affine.py` evaluates 105 Gegenbauer integrals by high-precision quadrature and checks 35 exact symbolic Fourier moment identities and 1,500 finite harmonic sign inequalities, with the recorded output in `check_output.txt`. Numerical disagreement is below \(8.6\times10^{-50}\). For full reproduction, execute `python verify_spherical_affine.py` with SymPy and mpmath available.

No finite computation certifies the infinite degree assertions; those depend on the displayed analytic argument. The bibliography was compared at the level of the primary texts stated in the report. Equivalent uncatalogued findings remain a residual originality risk. No independent mathematical audit has been performed.
