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
# Reproducibility and verification

The argument is a complete analytic proof for arbitrary dimension \(d\ge2\) and positive orthotope side lengths. `RESULT.md` gives definitions, normalization, exact ball integrals, finite Vandermonde inversion, generic sample-number minimality, and the spherical-cap asymptotic. No computational result is used to extrapolate an infinite theorem.

Run `python3 verify.py` from this package directory. The standard-library checker passed 76 diagnostic assertions at preparation time. It independently evaluates the two-dimensional polar formula, tests normalizations and first/last coefficients in dimensions two through five, solves Vandermonde inverse problems, numerically checks first-cap asymptotics for planar rectangles and squares, and simplifies the three-dimensional onset coefficient to \(m/2\).

The checker is a diagnostic, not a proof of the general statement, not an exhaustive literature search and not independent certification. The claim's sampling theorem applies only when the tested radii lie inside the common short-range polynomial regime. The asymptotic describes the first threshold and not subsequent transitions. Independent audit has not been performed.
