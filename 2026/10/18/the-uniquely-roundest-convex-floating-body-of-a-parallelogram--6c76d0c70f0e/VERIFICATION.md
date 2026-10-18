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

## Analytical verification

The proof checks four logically independent steps: the exact area quantile for square caps; support-function equality of the proposed hyperbolic contour and all quantile supporting lines; full inradius/circumradius extrema and contact transitions; and optimality among all affine ellipsoid sandwiches via the convexity of the inverse-shape constraint under the square dihedral group. Strict one-variable derivative signs on all three open intervals prove uniqueness at \(\alpha_*=3/2-\sqrt2\).

## Standalone computation

Run `python3 check_floating_square.py` from the extracted package directory. The script uses only the Python standard library. The actual checker run printed `VERIFY_OK normalization_samples=45009 support_samples=45009 boundary_samples=90009 min_parameter=0.085786437626905 min_BM=1.022162169058788 max_support_discrepancy=4.44e-16`. The tests sample directions and parameters, compare the cap-quantile and contour-support expressions, maximize boundary radii independently, and check the closed-form optimum. Finite sampling is not a completeness argument; the analytical proof supplies that argument.

## Scope and limitations

The proof is for \(0<\alpha<1/2\) and planar nondegenerate parallelograms. The exact square contour itself is previously described in Gupta's 2017 article and is used as an acknowledged input, not asserted novel. The new contribution is the sharp affine-roundness optimization, with residual historical-priority risk. Independent validation and any externally issued certificate have not been performed.
