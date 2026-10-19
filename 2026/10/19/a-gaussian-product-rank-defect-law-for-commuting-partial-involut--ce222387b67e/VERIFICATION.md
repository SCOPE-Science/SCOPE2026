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

# Reproduction and scope

Run `python3 verify.py` in a directory containing the extracted standalone file. It requires only the Python standard library and prints `VERIFY_OK` after all assertions succeed.

The script independently generates every partial involution on zero through six labeled points, composes every ordered pair as partial maps, tests commutation, records the cycle types of products, and checks both the fully marked labeled-block recurrence and every realized prescribed-product fiber formula. It also checks the first seven sequence coefficients. Exhaustive computation at these finite sizes does not certify all sizes or a probabilistic limit.

The general proof in `RESULT.md` is a combinatorial decomposition plus a uniform single-saddle Cauchy estimate for a degree-four exponential entire function, followed by convergence of moment-generating functions. Verification of the analytic argument is mathematical rather than an exhaustive machine search. Independent assessment has not been performed.
