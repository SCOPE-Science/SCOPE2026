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

# Verification of the uniform-edge chord law

Execute `python -m pip install -r requirements.txt` and `python verify_random_edge_law.py`.

The script independently integrates the proposed angular density, checks the exact moments \(1\), \(128/(27\pi)\), \(5/2\) and \(70/9\), and tests the complete \(n=4\) CDF at five points against the spherical two-point chord law. It reconstructs faces and distinct edges with `scipy.spatial.ConvexHull` for \(n=4,6,12,30\), verifies the exact edge count \(3n-6\), and compares both sample-mean quadratic energy and four CDF thresholds with the analytical beta-product law. All checks completed successfully with `ALL_SHAPE_DENSITY_CDF_AND_HULL_CHECKS_PASSED`.

Observed simulated mean quadratic energies for \(n=4,6,12,30\) were respectively 11.87143748, 21.19561833, 36.23795323 and 49.11996772; exact predicted means are 12, 21.42857143, 36.26373626 and 49.11290323. Maximum absolute sampled CDF discrepancy at the four thresholds was respectively 0.00815, 0.01177, 0.00365 and 0.00178. Finite simulation and quadrature only corroborate the analytic identities; they are not certificates for all sample sizes or historical priority.

All calculations use Euclidean distances between points on the unit sphere. Independent external validation remains unperformed.
