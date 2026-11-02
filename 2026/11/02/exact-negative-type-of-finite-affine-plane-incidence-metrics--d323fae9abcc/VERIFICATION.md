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

The complete algebraic proof is in RESULT.md. Its inputs are the finite affine-plane incidence axioms, two exact incidence-matrix products, an exhaustive orthogonal decomposition of the zero-sum hyperplane, and two elementary convexity inequalities on powers.

Execute `python3 affine_negative_type_checker.py` with Python 3 and NumPy installed. The checker independently generates the prime-field affine planes at orders 2, 3, 5, and 7; calculates shortest-path distances by breadth-first search; verifies the predicted distance matrix from incidences; tests the incidence identities; and checks centered powered-distance inertia below, at, and above the proposed exponent. It also checks the constant-population and paired-mode tests and builds a direct parallel-class witness above the exponent.

Observed successful execution: `AFFINE_NEGATIVE_TYPE_CHECK_OK` with `OK` at each order 2, 3, 5, and 7. The checker has floating-point inertia comparisons (tolerance \(10^{-8}\)); it is supporting evidence only. No finite sample establishes the all-order theorem, proves the existence of planes at untested orders, or validates the result independently.
