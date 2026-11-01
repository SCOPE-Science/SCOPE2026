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

# Verification record

The analytic proof is in `RESULT.md`, using only explicit arclength densities, a measure-preserving two-angle coordinate transform, Taylor expansion near the two maximizing pairs, dominated convergence for the joint rescaling, and classical complete elliptic integral expansions at parameter one. A fixed positive shape parameter and a shape parameter proportional to the distance deficit have different quantifiers; no uniform error over arbitrary shapes is assumed.

The standalone `check_ellipse.py` implements the exact two-angle probability integral with arclength weights and numerical quadrature. Execute `python check_ellipse.py` with Python 3, NumPy and SciPy. A successful local check prints `VERIFY_OK cases= 15`: nine crossover comparisons, three fixed-eccentricity tail comparisons and three cusp comparisons. Each test has finite numerical tolerance and therefore supplements rather than proves the analytic arguments. The input shape is an exact ellipse, endpoints are independent and uniformly distributed by arclength, and the distance is Euclidean. The proof does not cover arbitrary convex curves, dimensions above two, finite-sample statistical estimation or maximum statistics from an increasing number of sampled points.

Independent audit: not performed.
