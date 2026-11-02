---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

From exact RESULT.md: conditioning on different sides gives independent u,v uniform on [0,1] after affine reduction; the chord supporting line x/v+y/u=1 intersects the homothetic barycentric core iff a(1/u+1/v)<=1<=(1-2a)/min(u,v)+a/max(u,v), with a=(1-t)/3. The two disjoint failure areas are A=2a+2a^2 log((1-a)/a) and B=3a^2-2a(1-2a) log((1-a)/(1-2a)); integrating the regions gives Q=1-A-B. Same-side segments miss every proper core and give atom sigma. The perimeter weights satisfy 1/3<=sigma<1/2 by Cauchy, convexity and strict triangle inequalities. Independently integrated the two failure regions by numerical quadrature at five thresholds t=0.05,0.2,0.5,0.8,0.95, agreeing with the analytic closed form. The all-triangle result rests on exact integration, not Monte Carlo. Example side triples (2,2,1),(4,4,7) have equal sigma 9/25 and different shape.

## originality

PASS

The full penetration CDF, its affine-universal different-side factorization, sharp shape-order envelope and non-identifiability are not shown by the inspected length-only or containment formulations. No identified Resultary finding dominates this exact statistic. Inaccessible old secant sources present a genuine possible prior-equivalence risk.

## value

PASS

The full distribution and universal conditional factorization are intrinsic geometric-probability data for a natural two-boundary-endpoint sampling law; simultaneous sharp stochastic shape order, equilateral rigidity and explicit nonsimilar equal-law examples are substantive all-triangle structural facts rather than a routine isolated probability. A future researcher can use the exact law to benchmark chord penetration and shape identifiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
