---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For source AdaMod with beta1=beta2=0, d=beta3 in [0.07,0.13], alpha*h/epsilon in [40/11,40/9], source m0=v0=s0=0 and x0=r=alpha/2-epsilon/h>0, direct substitution yields first step x1=(2d-1)r with |x1|<r. Normalized signed-state map H(u)=1/[1+kappa(u-1)], z'=d z+(1-d)H(u), u'=u(2min(H(u),z')-1), kappa∈[.45,.55], is an invariant strict contraction on [0.7,1.3]^2. Independently checked rational uniform derivative bounds F∈[18000/54289,22000/29929], |H'|≤22000/27889, row norms at most about 0.95503 and 0.81630, strictly below 24/25; min-switch continuous piecewise smooth. Thus every source trajectory obeys |x_t-(-1)^t r|≤(13/50)r (24/25)^(t-1) and approaches positive nonminimizer objective. For small strictly positive beta1,beta2 a four-state signed map has contracting autonomous fixed point and exponentially decaying bias-correction perturbations; finite-source entry and uniform contraction give persistence. Independently replayed actual printed bias-corrected recurrences 150 steps for (0,0),(.0002,.0001),(.001,.002) and confirmed initial objective decrease and limiting two-cycle; finite traces only corroborate the analytic proof.

## originality

PASS

The source AdaMod paper has a smoothed learning-rate-memory cap but no proved source-initialized nonzero two-cycle; Bock–Weiß Adam cycles do not include the AdaMod rate-memory and min-cap state. The exact invariant square and persistence with strictly positive moment coefficients are not implied by generic Adam cycles. Best-of-knowledge PASS with survey full-text access risk.

## value

PASS

A genuine optimizer safeguard intended to prevent early extreme adaptive rates can still converge to an attractive nonoptimal alternating orbit on a strictly convex quadratic after first-step improvement. The uniform nontrivial parameter rectangle plus positive-moment continuation and source initialization is a motivated structural failure mode, beyond a one-step negative check. Scope excludes default beta3 near one, noise and arbitrary parameter choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
