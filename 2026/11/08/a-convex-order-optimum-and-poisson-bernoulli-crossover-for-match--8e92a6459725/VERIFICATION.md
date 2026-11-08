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

The accompanying `verify.py` script uses exact rational arithmetic and independently computes Laplacian cofactors, finite degree probabilities, and complete small-graph spanning-tree enumerations. It returned `VERIFY_OK 212 exact rational assertions` when executed against the included source. The general proof is the analytic block-determinant reduction, followed by the exact convex-expectation derivative and convergence of binomial and Bernoulli generating functions. The enumerations cover only the stated small graph sizes and are not a substitute for the analytic infinite-parameter argument. No independent mathematical audit has been performed.
