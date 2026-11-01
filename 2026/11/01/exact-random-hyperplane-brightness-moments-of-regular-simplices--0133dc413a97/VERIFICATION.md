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
Run `python3 verify_projection_brightness.py` from a directory containing the accompanying standalone Python file (Python 3 standard library only). The package program passed 210 checks, including the exact low-dimensional Cauchy projection identities, circle quadrature for the zero-sum sphere in three coordinates, exact second-moment identities, asymptotic correction diagnostics and seeded Gaussian experiments. The independently known Cauchy means are \(\mathbb E P_3=3\sqrt2/\pi\) for an equilateral triangle and \(\mathbb E P_4=\sqrt3/2\) for the regular tetrahedron, where the subscript here denotes vertex count. The program uses independent quadrature and a Gaussian representation rather than hard-coding these geometric checks as simulation targets.

These checks are finite numerical reproducibility evidence. The exact general formulas depend on the proved bivariate Gaussian integral and spherical moment normalization; the central limit theorem depends on the coupling and a published cube-width limit, not on numerical experiments. No independent audit has been performed.
