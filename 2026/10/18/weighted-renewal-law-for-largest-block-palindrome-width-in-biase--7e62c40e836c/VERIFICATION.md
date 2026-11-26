---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A shortest proper border cannot overlap itself across the word: an overlap induces a strictly shorter border. A specified nonoverlapping border is the shortest exactly when its content is unbordered. Its occurrence has the squared letter weight, and the middle remains independent. The three terms of the recurrence correspond to the empty word, a nonempty unbordered word, and successful peeling, giving the claimed joint PGF including the length-zero term. Inserting at the middle preserves all shorter end tests; only the even-length insertion can create a new shortest border, of half the length, and its exceptional squares are indexed by unbordered halves. This gives the weight-squaring term. For two infinite streams, conditional on distinct first letters a,b, the sum of the subsequent match probabilities is pi_a*pi_b/(1-s) <= 1/2, so h<1. Each least match is an event determined by the letters consumed, permitting independent restart. With B(alpha)<1, the total length consumed has a finite alpha-exponential moment, also when weighted by any fixed power of the number of successful steps. On 2S_*<n the two peelings agree including their nonempty center, proving the TV and moment estimates. Independent exact rational arithmetic gives the cited Bernoulli constants; no frozen script was executed.

## originality

PASS

The closest primary results give greedy factorization, the equal-weight count recurrence, uniform width counts and a uniform limiting mean. The supported distinction is the exact probability law for arbitrary nonuniform iid letters together with its distributional limit and exponential controls, not the greedy rule or the equal-weight counts. No equivalent result was identified in the inspected material.

## value

PASS

It classifies the entire asymptotic width law under biased input, including extinction and exponentially rare even widths, and gives a computable distribution parameter and rate. This goes beyond a scalar limit or recomputation of a uniform count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
