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

For A=1+y>1, squaring A=(u²+2)/sqrt((u²+2)²−4) gives the unique positive u²=T(y). Constant blending cancels in the fractional levels: δ=fy and w_c²=t_E²[T(cy)−T(y)]. To check the decisive strict inequality, write R−1 as H/J, with H and J the integrals of h=s^(−3/2)(ys+2)^(−3/2) on [a,b] and [b,1]. In H′J−HJ′ the double-integral integrand is h(s)h(t) times 3(t−s)/[(ys+2)(yt+2)], positive almost everywhere. The fixed compact integration intervals allow differentiation and the two limits: normalized kernels tend to s^(−3/2) and s^(−3), giving the claimed L and U. Positive widths fix the sign lost in squaring. The physical restriction is exactly y≥δ, so continuity and strict monotonicity give the unique inverse on [R(δ),U); equality at the lower endpoint is precisely f=1. The upper endpoint is only a limit, with f and u₀ tending to zero at fixed δ. With one positive width, each y≥δ gives a distinct physical fit by rescaling t_E, even at the unblended datum. No exceptional interior a,b or finite y was omitted. Replay: RESULT.md §§1–4 is the all-parameter proof; CHECK.py and VERIFICATION.md were inspected, not run. Their finite decimal checks do not certify uniqueness or numerical stability.

## originality

PASS

The forward duration formula and the broad idea of exact shape-based recovery are not the contribution. The distinct claim is strict global ordering by the ratio of two finite fractional-excess widths, with its full physical image and sharp inverse/one-width alternative. Neither the strongest compared publication nor the related Resultary record contains a theorem implying this result for all ordered fractions.

## value

PASS

Three simple summary measurements resolve an exact identifiability question for a standard model with severe practical blending degeneracies. The strict feasibility boundary is an independent model-consistency test, the attained boundary distinguishes the unblended case, and the one-width family explains what information a second crossing provides. This is not a noise-stability, measurement sufficiency or survey inference claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
