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

# Reproducible numerical checks and their limits

Install `numpy` and `scipy`; run `python verify.py`. The script regenerates every test from its embedded seed, prints `ALL_TETRAHEDRAL_JOINT_AREA_SILHOUETTE_CHECKS_PASSED`, and checks:

1. Exact density integrals against the solid-angle silhouette masses, independent area-weighted first moments and second moments, with absolute quadrature error tolerances below \(2\times10^{-11}\).
2. A separately derived convex-hull projection at 2,500 random directions, testing both the hull's vertex count and geometric area against the analytic cone and area identities.
3. The constant-posterior identity at 21 deterministic interior area values and the correctly rescaled known unit-edge unconditional density on its two constant branches.
4. Monte Carlo checks on 450,000 further random normals, including each type's area mean and the posterior over an interior subinterval.

The script is not a proof of exact density identities at uncountably many values. Those follow from the two spherical cone coarea calculations in RESULT.md. The code does not supply a historical originality certificate or an independent mathematical audit.
