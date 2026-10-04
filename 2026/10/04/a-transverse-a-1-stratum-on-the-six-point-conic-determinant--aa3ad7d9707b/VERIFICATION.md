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
The exact verifier reconstructs the affine quadratic Veronese matrix at the rational witness, checks rank \(4\), and checks vanishing of every first row-replacement determinant. It constructs the full Hessian from mixed two-row replacements, verifies Hessian rank \(3\), and verifies that the \((y_1,y_2,y_3)\) principal minor is exactly \(-576\). It then constructs nine explicit tangent directions to the five-collinear stratum, verifies that they are independent, and verifies that all nine lie in the Hessian kernel.

The computation is exact over \(\mathbb Q\). It verifies the finite local algebra at the witness; genericity follows mathematically from openness of the rank and nonvanishing conditions. It does not enumerate or classify lower-dimensional boundary strata.
