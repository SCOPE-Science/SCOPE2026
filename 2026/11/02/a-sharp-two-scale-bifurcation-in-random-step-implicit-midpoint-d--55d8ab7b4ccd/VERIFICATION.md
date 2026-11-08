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

Midpoint update multiplier R(H)=(1−lambda H/2)/(1+lambda H/2)=−tanh((x±a)/2) where x=log(lambda h/2). Independence gives E|u_N|²=|u0|² q_a(x)^N and q_a(x)=1−2(1+cosh(a)cosh(x))/(cosh(a)+cosh(x))². For c=cosh(a), y=cosh(x)>=1, Q_c'(y)=2(cy+2−c²)/(y+c)³. Therefore one optimum x=0 for 1<=c<=2 and two x=±arcosh(c−2/c) for c>2; q minima are (c−1)/(c+1) and (c²−2)/(2(c²−1)). At c=2 expansion is 1/3+x^4/54+O(x^6); arcosh inversion gives x*=sqrt(3sqrt3)*sqrt(a−a_c)+O((a−a_c)^(3/2)). A midpoint atom vanishes only at x=±a, strictly distinct from optimal |x|<a for a>0; hitting that atom has geometric waiting time with p=1/2 and worse mean-square value. Independently verified derivative and quartic symbolic identities and scanned 1400 mean-square/global test points. Per-iteration objective only, not per unit physical time.

## originality

PASS

Implicit midpoint stability multiplier and A-stability are classical; Abdulle–Garegnani analyze randomized physical time steps for integration accuracy and geometric properties; Lie–Stahn–Sullivan study randomized numerical integration error including additive perturbations. Neither inspected work has the exact fixed-log-spread, cost-per-update scalar mean-square optimization with pitchfork 7+4sqrt3. A published related stage-law optimization varies implicit-stage parameter rather than the physical time-step scales, so matching numeric constants need not indicate equivalent feasible sets. Older stochastic rational recurrence literature remains risk.

## value

PASS

Binary uncertainty in positive time steps is a natural stochastic numerical relaxation design. A complete optimal per-step damping classification, exact symmetry breaking, quartic critical sensitivity, and contrast between expected squared residual and pathwise exact finite stopping provide useful mathematical structure. The model is deliberately scalar and fixed-update-count; it does not claim general numerical accuracy superiority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
