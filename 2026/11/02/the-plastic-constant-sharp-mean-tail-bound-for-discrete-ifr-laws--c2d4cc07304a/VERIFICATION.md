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

The proof covers all integrable integer-valued laws with log-concave survival and p_(m+1) >= p_m > 0, not merely finite-support laws. After shifting m to zero, t=S_1 and x=t/p_0 >= 1. Monotonicity of the positive survival ratios, with the zero-tail case included, gives E(X_+) <= t^2/p_1 <= tx and S_(-k) <= min(1,t(1+1/x)^(k+1)). Thus the mean condition gives F_t(x)=sum_{j>=1}(1-t(1+1/x)^j)_+ <= tx. At c=a-1=a^(-4), with a^3=a+1, the first-term bound on [1,a], two-term convexity bound on [a,3], four-term convexity bound on [3,6], and decreasing Riemann-sum bound on [6,infinity) prove F_c(x) >= cx, strictly away from a. Both the endpoint values and their strict signs were checked with rational arithmetic (331/250<a<4/3; the logarithm certificate uses 402/581>175/256). Monotonicity in t excludes t<c. Equality forces t=c, x=a, p_1=p_0 and zero mean; saturation term by term forces S_(-1)=1 and a constant ratio 1-1/a to the right of S_1. The specified survival law has decreasing ratios, adjacent masses a^(-5), and positive and negative mean contributions a^(-3), proving attainment and uniqueness up to translation. This is an analytic infinite-support proof; the supplied finite examples are not used as evidence of the universal inequality. Replay from RESULT.md §§1–3 with exact rational endpoint checks and the displayed survival sequence.

## originality

PASS

The closest prior theorem and its proof concern the same discrete-IFR problem, but the supported distinct claim is the sharp ratio-one constant and its unique equality law. The geometric survival comparison itself is prior technique. No matching or stronger covering statement was found in the inspected sources.

## value

PASS

Equal-or-increasing adjacent mass is a natural discrete threshold regime outside the sharp theorem's proved parameter range. The result resolves a strict mean-exceedance bound in that regime where formal extrapolation would be false, and the unique one-left-atom/geometric-right-tail extremizer identifies the mechanism. It makes no unsupported claim about other mass ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
