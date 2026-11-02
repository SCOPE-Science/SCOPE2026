---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For dX=g(X)dB with g=x²/(1+x), f=x/(1+x), a=x²/(1+x)^3, cap C(z)=min(z²,1), Q=exp(fz+(a/2)(C-h)-(f²/2)h), and M_h(x)=E Q(x,sqrt(h)Z)>0. The multiplier Q/M is strictly positive and has conditional mean one. Since |f|≤1 and 0≤a≤4/27, capped exponential tails admit Gaussian moments of every fixed q at every finite h; a Jensen lower bound on M_h(x) uniform in x gives moment induction and genuine martingale, not merely local. At small h the Gaussian tail |z|>1 has exponentially small contribution; Taylor gives a centered Milstein expansion xQ/M=x+gz+(gg'/2)(z²-h)+xρ with Eρ=0, E|ρ|²=O(h³) uniformly. Direct symbolic algebra confirmed x(f²+a)=gg'. Bounded f,a derivatives and Lipschitz g,gg' plus solution moment bounds yield centered Itô–Taylor local error O(h³) in conditional mean-square and global strong order one by discrete Gronwall. The uncapped quadratic Gaussian at x=2 has infinite q-moment for h≥27/(4q); this is a known comparison. Finite quadrature supports but does not certify the stochastic convergence.

## originality

PASS

Bréhier–Cohen (2026) establish positivity and strong order one for the uncapped exponential integrator under small-step moment restrictions. The inspected abstracts and the audited manuscript's explicit formula comparison distinguish the proposed capped z² tail and exact conditional-moment normalization that together give unconditional all-coarse-step moments and true martingality for a specific nonlinear scalar diffusion. Earlier logarithmically truncated Euler and bounded-domain methods preserve different properties and use different formulas; no same four-property single scheme located in Resultary or accessible primary abstracts. Best-of-knowledge PASS with significant uninspected-full-text risk.

## value

PASS

The method resolves a concrete conflict between positivity, exact mean preservation, coarse-step moment existence, and first-order strong accuracy for a motivated nonlinear positive martingale; the exact normalizer caveat is explicit and the scheme is mathematically nontrivial beyond a single routine Euler step.

The dated certificate retains the supplied scientific assessment, sources and limitations.
