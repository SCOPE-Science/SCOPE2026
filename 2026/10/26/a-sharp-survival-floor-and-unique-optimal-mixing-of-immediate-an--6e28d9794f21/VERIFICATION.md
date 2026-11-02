---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For 1<R<2, 1/R<s≤1, θ∈[0,1], exponential modes in the specified positive second-order recurrence give λ²=R(1−θ)cosh(t) λ+Rsθ cosh(2t), and the precisely defined speed is c(θ)=inf_{t>0}logλ/t. The weighted implicit differentiation in RESULT.md gives strictly positive gθ″(t), while gθ(0)>0 and its large-t linear asymptote has a coefficient Lθ<1; hence each cθ has a unique finite minimizer. At θ=0 the endpoint derivative switches at s_c(R)=R/(1+tanh² t_R), t_R tanh t_R−logcosh t_R=log R. For s≤s_c, a fixed-tilt test yields strict global superiority of θ=0, including equality via the nonstationary shifted tilt. For s>s_c the maximizing θ is interior; the vanishing θ-derivative fixes unique tilt τ=atanh(sqrt(R/s−1)), and monotone tilt derivative fixes unique θ_opt=(v−u)/(2z−u−v), speed v. Differentiating log s_c in the R(t) parametrization yields sech²t[t−tanh(2t)], with unique zero t*=0.957504024…, giving s_min=0.878135713950414…. Independent numerical minimizations across below/above regimes and the global floor agreed. The theorem is explicitly about the linear exponential-envelope functional, not nonlinear selected fronts.

## originality

PASS

Targeted source and implication comparisons did not identify prior coverage of the precisely scoped final theorem; best-of-knowledge PASS with named residual risks, not a priority certificate.

## value

PASS

Optimizing a short/fast and delayed/long dispersal channel is a natural structured-population design question. This result classifies the entire admissible phase diagram, an interior strategy that beats both pure channels, and a nontrivial survival floor and reentrant growth window. It is an analytically determined optimization boundary rather than a mere simulation of one seed-bank scenario.

The dated certificate retains the supplied scientific assessment, sources and limitations.
