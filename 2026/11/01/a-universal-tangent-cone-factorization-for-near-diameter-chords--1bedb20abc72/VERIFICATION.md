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

The complete mathematical argument is in `RESULT.md`. The executable `verify_cone_endpoint.py` checks the exact regular-simplex tangent-section Gram determinant for dimensions two through eight and independently verifies the reduction to the known orthotope product coefficient for dimensions four through six.

The script also samples 400,000 pairs of points from the tangent-section simplices associated with a diameter of the four-dimensional unit-edge simplex. Each sampled affine line is clipped directly against all five facet halfspaces. With the exact invariant-line Jacobian retained, the inferred coefficients at thresholds 0.15, 0.06, 0.02 and 0.006 are respectively 0.302264485, 0.257342315, 0.236140106 and 0.228696137, converging to the theorem's value 0.225079079. These checks are finite and do not certify an asymptotic theorem.

The proof itself relies on polyhedral tangent cones, strict vertex extremality, local gauge convergence, a beta convolution volume identity and the Cauchy projection normalization. Claims about the full chord distribution, higher-order remainder, and independent verification are not made.
