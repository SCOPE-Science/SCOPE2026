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

The analytical proof derives the planar support function directly from the convex hull of an equatorial disk and two axial points. It differentiates the perimeter integral with correct moving-boundary cancellation and reduces the derivative sign to the strictly increasing scalar function \(G_t\), which proves uniqueness on the continuum of directions and aspect ratios. The threshold derivative and limiting expansions are derived separately.

Run `python check_projection_perimeter.py` (requires NumPy and SciPy). The checker performs numerical quadrature with crossover points exposed to control integration error, independently constructs projected planar hulls, and compares representative global minimizers and asymptotic coefficients. These finite tests do not establish historical novelty or replace the analytical inequality. No independent external mathematical audit has been performed.
