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
The checker uses only exact rational arithmetic and the Python standard library.

For order one, it constructs the path-difference normal matrix and verifies on several sample lengths and rational smoothing parameters that its exact inverse has strictly positive entries and row sums equal to one.

For orders \(2\) through \(10\), it constructs the minimal binomial forward-difference row, verifies the Vandermonde norm identity, reconstructs the rank-one Sherman–Morrison inverse, and checks the negative step response. It also forms a strictly positive strictly increasing perturbation with rational amplitude below the analytic threshold and verifies that the same output coordinate remains negative.

The universal statements for every sample length at order one and every order \(p\ge2\) are proved analytically in RESULT.md. Finite replay is corroborative only.
