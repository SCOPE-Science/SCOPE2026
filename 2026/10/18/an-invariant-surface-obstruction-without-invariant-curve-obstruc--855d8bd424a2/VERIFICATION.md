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

# Reproducibility and limits

Run `python3 verify.py` from a directory containing the extracted package files. No third-party modules or network access are required. The script reconstructs all 18 walls from the declared fan, uses exact integer determinant identities for anticanonical degrees, checks their symbolic formulas at 56 values of the free integer parameter, verifies the ray-7 convex-hull witness and the toric surface's five-ray star, checks the zero-degree curve pairing, and enumerates bihomogeneous monomials for the first 30 positive multiples of the surface divisor.

Expected output: `VERIFY_OK wall_profiles=56 fan_cones=12 walls=18 ray7_convex_witness=true surface=Bl_p(P1xP1) noninvariant_curve_degree_zero=true linear_series=30`.

The theorem's infinite parameter range is justified by the affine-linear wall expressions, not by the bounded numerical loop; the section-count formula for all positive integers is justified by the bound on the maximum local monomial degree, not by the finite enumeration. The curve criterion and toric smoothness/completeness are used from the literature. Independent audit is not performed.
