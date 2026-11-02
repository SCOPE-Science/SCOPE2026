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

Run the self-contained Python checker from this package: `python verify.py`. Dependencies: Python 3, NumPy and SymPy. Its symbolic computations verify that the derivative of the CDF equals the claimed density, that both endpoints normalize properly, and that the first two area moments are the displayed exact constants. The Gaussian positive-wedge angular integral is symbolically reconstructed, and its angle-density moments and normalization are independently integrated.

The checker additionally generates 260,000 independent pairs of genuine uniform spherical sites after fixing the first site at the pole, constructs their bisector normals, and compares the empirical first two area moments and four CDF values to their exact counterparts. A separate experiment approximates the labelled Voronoi areas of 150 random three-site configurations by 22,000 independent sphere probes for each realization; its membership method does not use the spherical lune-area identity. The successful execution ended with `ALL_CHECKS_PASSED`.

Finite sampling cannot certify an exact distribution and is used only for diagnostic agreement; the theorem is proved analytically in `RESULT.md`. The Gaussian angular kernel used as a lemma is previously published. There is no independent mathematical audit.
