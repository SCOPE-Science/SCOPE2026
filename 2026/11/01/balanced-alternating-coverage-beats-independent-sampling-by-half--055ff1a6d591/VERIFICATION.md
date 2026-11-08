---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Actual seven-file Git tree, RESULT.md proof, check.py and verification record inspected. Starting-side observations at t have floor(t/2)+1 counts and other side ceil(t/2), independent uniform coupon collectors; iid counts yield a binomial mixture. The discrete coupon-completion CDF is log-concave, so its product at fixed total counts is maximized at the balanced split, proving all-horizon stochastic order. Exact gamma/Poissonization identity Delta=nH_(2n)-E max(T,Tprime)=1/2 sum_{k,l} p(k)p(l)(E|S_k-S_lprime|-|k-l|); local Gumbel coupon-completion mass, gamma-difference normal limit, and Bernstein off-diagonal/tail localization give Delta/log n->(int g^2)(int m)=1/4. The tie contribution is O(1/n), establishing the half-log gap. Boundary n=2 and fixed first vertex correctly handled. Independently recomputed 134 exact fixed-horizon stochastic-order checks; they corroborate but do not prove the infinite claim.

## originality

PASS

Best-of-knowledge: prior group-mixture coupon collector and simultaneous two-collector results overlap the mechanism but do not give this deterministic balanced group schedule versus iid stochastic order AND its exact half-log mean gap. Primary full-text access to Doumas was unavailable, so no whole-document noncoverage is asserted; the precise result remains a bounded priority risk.

## value

PASS

The temporal stratification of the same uniform marginal samples presents a natural optimization question; the result gives a uniform distributional improvement and an exact divergent second-order mean benefit beyond the classical O(n log n) cover-time scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
