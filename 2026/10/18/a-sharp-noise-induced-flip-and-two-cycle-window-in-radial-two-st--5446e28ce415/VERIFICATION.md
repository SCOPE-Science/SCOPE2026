---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The normal subproblem enforces z·v=−(s−1)/2 with v parallel to z, and the tangential minimizer is −g. Conditional mean zero and squared norm σ² hold for the two noise signs. Orthogonality removes the sign samplewise, giving Fη(s)=(s−3)²/(4s)+η and a positive lower bound η for every new iterate. The fixed-point quadratic has exactly one positive root since its root product is negative; the root increases with η, and Fη′=1/4−9/(4s²) crosses −1 there precisely at s=3/√5, giving ηc. A distinct pair r,t must satisfy rt=9/5 and r+t=6−4η; conversely these two relations give Fη(r)=t and Fη(t)=r by substitution. Their positivity and distinctness are equivalent to 0<η<ηc. The product of derivatives is 9/4−(25/9)(3/2−η)², increasing from −4 to 1; its −1 crossing gives η−. F_{3/5}(3)=3/5, F_{3/5}(3/5)=3 and F′_{3/5}(3)=0. This is one unordered primitive radial orbit, not an angular orbit. The open thresholds classify strict multiplier stability, not nonlinear behavior at the endpoints. The formal fixed-step example is not an instance of the cited complexity guarantee.

## originality

PASS

Credit prior coverage of the generic SQP scheme and the general period-two multiplier and collision for degree-two rational maps. The exact radial multiplier is a specialization, not an independently novel dynamical theorem. The supported distinct contribution is the formal SQP circle realization with conditionally unbiased tangent noise, its samplewise noise-controlled radial reduction, and the resulting positive radial stability and infeasibility witness for a concrete stochastic iteration.

## value

PASS

The example separates the deterministic SQP drift from its radial dynamics under a genuinely unbiased tangent oracle: zero conditional mean does not remove the samplewise effect of the squared tangential step. The same circle constraint and step can support repulsion, stable radius oscillation and stabilization by adjusting noise alone, and the exact superattracting orbit stays infeasible. The thresholds specify exactly where this local noise effect occurs in the model, not a paper-sized contribution on rational dynamics or a refutation of an in-regime convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
