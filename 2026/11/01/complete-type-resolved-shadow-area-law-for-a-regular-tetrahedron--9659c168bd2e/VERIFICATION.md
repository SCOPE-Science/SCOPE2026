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

# Reproducing the checks

With Python 3 (standard library only), execute `python3 verify.py` in the directory containing that file. The program prints `PASS: 5444 deterministic checks and 400,000 independent Haar-random directions` and the baseline type probabilities if the checks pass.

The program verifies the two spherical-segment formulas using a separate polar-area quadrature, projects the four tetrahedral vertices independently into 700 explicit viewing planes and computes their planar convex hulls, confirms strict numerical CDF range and monotonicity on a 1,999-point grid, and cross-checks the first two type-conditional moments against earlier exact expressions by a separate Simpson integral. It also generates 400,000 independent normalized Gaussian view directions and compares their type-and-area counts with the analytic distributions at eleven thresholds.

The finite checks **do not prove** the theorem for all orientations. The mathematical proof is in `RESULT.md`, in particular the exhaustive spherical-region decomposition, the analytic integral for the spherical cap/hemisphere segment, and the local area-element argument for the lower-endpoint expansion. Historical priority and independent mathematical validation are unresolved.
