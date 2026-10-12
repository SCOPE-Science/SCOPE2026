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

The complete analytic verification is the four-step proof in `RESULT.md`. The local CDF expansions follow from uniform Taylor expansion on the unit simplex and a standard Dirichlet integral. The unique positive phase boundary follows from strict log-concavity and the positive derivative at zero. The crossing interval has rigorous rational-exponent integer inequalities. The logarithmic upper-tail rate is proved by convexity and a gamma survival bound, with a matching lower bound from an explicit event.

Run `python3 check.py` with the Python standard library. The checker passed 136 assertions; this included exact integer comparisons, independent numerical checks of the coefficient ratio and its sign away from a cancellation, bisection of the root in several finite dimensions, and endpoint consistency. Finite numerical checks do not prove uniqueness, the asymptotic inequalities, or every real parameter; those are provided analytically.

Unproved and unclaimed: exact number of CDF crossings, the cancelled-parameter sign, all stochastic-order relations outside the shown interval, general dependent summands, and a complete priority certificate. Independent scientific auditing is not performed.
