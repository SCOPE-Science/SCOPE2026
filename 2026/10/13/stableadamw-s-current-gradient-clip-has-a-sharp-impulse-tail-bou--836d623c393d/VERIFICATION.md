---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The source bias-corrected recurrences telescope on a single impulse G at t=1 followed by zero gradients, giving v_t=(1-beta1)beta1^(t-1)G/(1-beta1^t) and u_t=(1-beta2)beta2^(t-1)G^2/(1-beta2^t). At t>=2 the current g_t=0 makes the published StableAdamW clipping RMS zero and its learning rate α. The normalized parameter update is α c1|G|/(sqrt(c2)|G|+epsilon); supremum over FINITE impulse amplitudes at each time is α c1/sqrt(c2). Its factor (beta1/sqrt(beta2))^(t-1) proves uniform boundedness exactly beta1^2<=beta2, with explicit finite boundary limit sqrt((1-beta1)/(1+beta1)); for beta1^2>beta2 choose t and then a sufficiently large finite G. The alternative v_t^2 detector yields a scalar cap α because its clip threshold D=sqrt(max(u,epsilon^2)) never exceeds sqrt(u)+epsilon. I independently checked recurrence/tail ratios for representative β values, separate from source randomized verifier.

## originality

PASS

Best-of-knowledge StableAdamW-specific exact current-gradient zero-tail gate, sharp impulse amplitude frontier, and contrast with the source-discussed but empirically rejected squared-momentum detector. The classical condition beta1^2<beta2 for Adam moment ratios is emphatically prior and not asserted as new. Full Wortsman et al paper Algorithm 2 and Appendix E contain the detector but not the stated zero-tail stress-test theorem. Resultary search returned adjacent optimizer moment studies, not this exact statement.

## value

PASS

A motivated robustness/safety property of an explicitly proposed optimizer design: large stale momentum can bypass a current-gradient clip after an impulse, with sharp parameter condition, while standard paper settings remain bounded. The result matters for selecting permissible decay parameters and contrasting two known detector choices; it does not claim real-world convergence failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
