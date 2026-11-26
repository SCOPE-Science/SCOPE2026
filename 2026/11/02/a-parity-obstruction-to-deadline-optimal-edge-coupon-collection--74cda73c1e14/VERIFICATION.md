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

Under fixed i.i.d. edge draws the larger bipartition side receives exactly one ordinary coupon per round. Conditional on the rounds assigned to two coupon classes, averaging their masses cannot reduce the chance of seeing both (including zero or one such round). Iteratively averaging a largest and smallest mass converges to uniform: each averaging decreases squared distance to uniform by half the squared spread. The saturated matching can be extended by one incident edge for each remaining B-vertex, making coverage equivalent to collecting the uniform B-coupons and attaining both the Stirling-number CDF and b H_b, including b=1. For a=b>=2, equality at t=b forces uniform B-marginals by AM–GM. Two B-vertices cannot share a positively supported A-neighbor, since selecting that neighbor for both would miss A with positive probability; b disjoint nonempty supported sets in A are singletons. On C_(2m+1), the complement takes a minimum edge cover bijectively to an m-matching: missing two consecutive edges would leave a vertex uncovered. The unmatched vertex determines the matching of the remaining even path, giving 2m+1 covers and the stated earliest-deadline probabilities. The strict comparison follows from ((2m+1)/(m+1))^m >= (7/4)^m > m+1 for m>=3. If all vertex hazards equal 2/n, consecutive hazard equations force step-two periodic edge weights, hence uniform on an odd cycle. Otherwise a vertex has hazard s<2/n, so (1-s)^t eventually strictly exceeds the uniform failure upper bound n(1-2/n)^t, including s=0. This establishes nonexistence of a universal optimizer, not a uniform-in-p threshold.

## originality

PASS

The classical uniform coupon bound and maximum-matching count are inputs, not the distinct finding. In the checked material I found no equivalent graph-supported all-deadline classification or theorem implying the odd-cycle early/late conflict. The strongest comparisons concern either other sampling mechanisms, pairs of prescribed laws, or expected time rather than a universal CDF optimizer.

## value

PASS

The all-deadline objective is a natural strengthening of expected-time optimization for a coverage process. The exact support classification on balanced graphs is useful for designing a sampler; contrasting it with nonexistence on all odd cycles of length at least seven gives a structural parity boundary in the cycle family. The comparison separates first-feasible cover counts from long-time vertex hazards rather than reporting a finite crossing for one parameter pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
