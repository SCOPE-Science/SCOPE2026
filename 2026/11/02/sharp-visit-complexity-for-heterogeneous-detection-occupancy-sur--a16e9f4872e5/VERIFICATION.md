---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

From the full labeled law the all-zero event on each visit subset is a marginal; conditional independence and the Poisson zero probability make this the common mixture transform evaluated at that subset's total duration. Conversely inclusion–exclusion over the visits required to be positive recovers every cell. Thus coincidences of subset sums give no additional sample, and time zero supplies normalization for free. For two admissible measures with at most k positive rates each, the difference has at most 2k+1 distinct exponential terms, including a possible term at the common rate zero. Dividing by one nonvanishing exponential and applying Rolle to the derivative inductively gives the at-most L−1 distinct-zero bound for L nonzero terms. Agreement on at least 2k positive times and at zero forces the measures to coincide. For the reverse implication, increasing ordered rates and strictly positive masses summing to less than one form a nonempty open 2k-dimensional parameter space. The evaluation map into m<2k dimensions is continuous and cannot be injective by composing with a coordinate embedding and applying invariance of domain. This is failure of global injectivity, not a proof that every point has a nontrivial fiber. Binary weights give exactly 2^n−1 distinct positive sums and scale to any total duration; equal durations give n. For two classes, a sorted triple a≤b≤c that is not constant yields the four strictly increasing positive sums a,b,a+b,a+b+c if a<b, or a,2a,a+c,2a+c if a=b<c. The Prony construction is valid for exactly k distinct active classes as in its Vandermonde argument; for a strict upper bound the Hankel rank is the actual active count and that smaller leading block is used. Source and VERIFICATION.md were inspected, not executed. Independently, exact rational evaluation of the two listed measures gave common first moments F(0),...,F(3)=(1,3/5,9/20,3/8) and fourth-moment difference 33/27200, verifying the equal-effort ambiguity and its separation by (1,1,2).

## originality

PASS

The sharp global criterion for arbitrary positive durations and the minimum visit count at fixed total effort are distinct from the inspected occupancy mixture and general latent-class identifiability statements. The classical exponential zero bound, Prony recovery and zero-inflated binomial setup are ingredients, not original claims. The decision does not determine absolute priority.

## value

PASS

An exact criterion for which schedules preserve identification is useful beyond a sufficient recipe. It identifies how duration collisions lose information and quantifies the best-possible change from 2k equal visits to ceil(log₂(2k+1)) designed visits at the same total effort, under an explicit stochastic model. The sharp transition for two classes is a concrete design consequence. None of this asserts that an identifying design is well conditioned, more precise, or cheaper in a given field setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
