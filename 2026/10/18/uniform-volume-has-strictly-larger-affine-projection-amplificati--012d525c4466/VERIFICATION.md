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

# Verification and scope

Execute `python3 check.py` from this directory. The actual execution produced `PASS: 91 analytical-formula consistency assertions`.

The checker independently integrates the radial positive-part expectation and compares it with the explicit formula at dimensions \(1,2,3,5,11\). It verifies the endpoint norms \(1\) and \(5/3\) for interval cone and volume measures, the two exact disk norm constants by numerical quadrature of independent kernels, and the exact nonnegative comparison formula at representative regular polygons (including a triangle, which is centered but not centrally symmetric). No random sampling, stored external data, or specialized packages are required.

The infinite collection of dimensions, convex bodies, and evaluation points is not certified by numerical tests. The radial independence law, reproducing kernels, positive-part inequality, equality criterion, and symmetric-boundary strictness have analytic proofs in RESULT.md. The calculations do not settle priority against all existing literature.
