---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

RESULT.md establishes an exact independent two-uniform-coupon-stream coupling conditional on reset indicators. The part chain [[r,1-r],[1,0]] has stationary frequencies (1/(2-r),(1-r)/(2-r)); move counts to B and A have means (1-r)/(2-r)t and (1-r)^2/(2-r)t and variance O(t). At t=((2-r)/(1-r))n(log n+x), fluctuations are o_P(n). Coupon missing-count factorial moments and deterministic upper/lower count sandwiches yield independent Gumbel limits, with A intensity c=(1-r)exp(lambda/(1-r)). The max CDF and logistic last-covered side follow from independent continuous Gumbels. Starting root already visited and no simultaneous completion are correctly handled. Local independent_checks.py compares direct labelled finite-state evolution against the two streams for small bicliques; experiments are corroboration rather than a proof of the asymptotic.

## originality

PASS

Fixed-r growing-complete-bipartite two-class Gumbel competition with n/log n part perturbation is not stated in inspected reset-cover-time and general coupon Gumbel primary results. Basic Gumbel coupon limits are explicitly prior; candidate novelty is the simultaneous two-stream coupling, critical ratio and terminal-side law. This is best-of-knowledge, not a priority guarantee.

## value

PASS

Cover times and last-visited classes are natural random-walk observables. The theorem computes a nontrivial critical n/log n window, two independent limiting clocks and explicit logistic terminal location, providing a sharp benchmark for resetting walks beyond a generic coupon-collector theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
