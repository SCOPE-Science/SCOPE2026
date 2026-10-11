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

The theorem for all nondegenerate tetrahedra is an analytic integration theorem, not a finite or probabilistic certificate. The critical identities follow from the spherical divergence theorem applied to the degree-one and centered degree-two spherical harmonics of each opposite-face normal.

The independent executable `verify.py` reconstructs face normals, areas, and spherical vertex cones from three tetrahedral vertex sets, including two asymmetric tetrahedra. It compares finite formula moments against direct two-parameter spherical-cone Gauss--Legendre quadrature. The maximum observed absolute error across all cone areas and first/second cone moments was
\[
3.55\times10^{-15}.
\]
For a regular tetrahedron with edge length \(2\sqrt2\), it independently checks the closed conditional first and second moments and the known unweighted and unconditional benchmarks. It samples 600,000 isotropic directions for regressions and computes 2,800 explicit 2D convex hulls to check projected area and silhouette type.

Reproduce in a Python environment with `numpy` and `scipy` installed by running `python verify.py`. The script checks all listed assertions and prints `VERIFY_OK`. The random generator has a fixed seed.

The calculations are finite numerical diagnostics; no claimed bound for every tetrahedron is inferred from their sample size. The exact formulas and arbitrary-shape domain are proved in `RESULT.md`.
