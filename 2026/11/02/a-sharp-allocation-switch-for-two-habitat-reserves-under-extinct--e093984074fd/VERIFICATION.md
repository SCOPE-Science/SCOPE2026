---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The four-state CTMC 11,10,01,00 with absorption at 00 and extinction rates u=theta/x,v=theta/(A-x), rescues c=beta(A-x),d=beta x has the first-step equations (u+c)T10-cT11=1, (v+d)T01-dT11=1, (u+v)T11-vT10-uT01=1. Inverting the transient generator independently in exact symbolic algebra confirms T11=((u+c)(v+d)+v(v+d)+u(u+c))/(uv(u+v+c+d)) and substitution T=[A-z/A+(beta/theta)z^2/A]/theta with z=x(A-x). For feasible x in [m,A-m], 0<m<A/2, z spans [m(A-m),A^2/4]; f(z) strictly convex for beta>0, so maxima only at endpoint z. Their difference has sign beta(z_-+z_+)/theta-1; hence unequal extremes for beta<beta_c, three-way tie at beta_c, equal split for beta>beta_c. Derivative sign yields coexistence of local extrema on theta/(2z_+)<beta<theta/(2z_-). All-parameter claims analytical; symbolic exact rational independent test passed. No positivity/boundary gaps found.

## originality

PASS

Prior two-patch stochastic reserve design and heterogeneous-patch models use related extinction-time objectives but the fully inspected 2000 Etienne-Heesterbeek source varies identical reserve count/size rather than jointly optimizing two unequal areas with recipient-area rescue. The specific endogenous-rate coupling and exact switch formula are not derived by cited results; potential older heterogeneous CTMC specializations are a substantial priority risk.

## value

PASS

The two-reserve reserve-design tradeoff is a motivated ecological optimization problem with an exact and discontinuous allocation decision boundary. Although the CTMC algebra and convexity are elementary, the combined area-dependent extinction/rescue model yields a nontrivial full global phase diagram and simultaneous local maxima relevant as a benchmark, not a generic symbolic exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
