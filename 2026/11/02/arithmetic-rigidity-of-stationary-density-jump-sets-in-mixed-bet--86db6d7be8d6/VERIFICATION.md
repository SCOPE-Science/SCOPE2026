---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For B_lambda x={lambda x}, the transfer-operator step identity L_lambda 1_[0,t) = floor(lambda t)/lambda + 1_[0,{lambda t})/lambda holds. Sum over all finite words from t_empty=1 with positive weights a_w=product(p_lambda/lambda). As r+s=q<1, series H converges uniformly and in BV and stationary h=H/Z by mass preservation, with 1<=Z<=1/(1-q); uniqueness invokes the pre-existing Suzuki result. Every endpoint contributes a noncancelling downward jump a_w/Z. For irrational beta, the distinct orbit {b^j(beta-1)} has jump >=(1-q)s r^j. For beta=c/d reduced noninteger, B_beta^j(1) has reduced denominator d^j, jump >=(1-q)s^j; these yield J(epsilon) liminf lower bounds. Integer multiplication mod1 is ergodic for Lebesgue a.e. beta-1, giving generic dense jumps. Independently checked exact rational beta denominator growth 36 steps over c/d=3/2, 4/3, 7/4. Finite tests do not prove infinite orbit claims.

## originality

PASS

Best-knowledge PASS *only for arithmetic infinite-step rigidity*, quantitative jump-count and generic dense-jump consequences; the positive endpoint expansion and uniqueness are expressly prior in Suzuki 2024. The new deductions are short but require proving there are infinitely many distinct noncancelling endpoints for all irrational/rational noninteger beta, not a direct theorem or table of the inspected source.

## value

PASS

A natural robustness phenomenon: mixing even two individually finite-step invariant-density maps (doubling and golden-ratio beta) produces infinitely many density jumps at every positive mixing probability. The exact arithmetic witnesses and logarithmic quantitative jump-count obstruction are structurally informative for BV invariant-density regularity and numerical representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
