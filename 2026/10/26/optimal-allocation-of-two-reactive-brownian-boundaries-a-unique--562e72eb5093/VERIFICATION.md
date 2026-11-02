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

Independently solved the backward ODE -Fyy=1 with F_y(0)=tF(0), F_y(1)=-(S-t)F(1). This yields F= -y^2/2+(1+(S-t)/2)(1+ty)/(S+t(S-t)). SymPy independently differentiated this rational expression and confirmed the claimed quadratic g/(S+t(S-t))^2 exactly, the rescaled S H(p)+K(p) relation, and H(p0)=(2y-1)^3/32. The derivative polynomial g has g(0)<0<g(S), and g_t(0)=S(1-y)+2>0 and g_t(S)=Sy+2>0, proving its derivative positive on [0,S] and a unique strict global interior optimum for all y, including endpoints. The implicit derivative and H sign establish strict budget monotonicity except y=1/2; boundary y=0 yields exact S-t*=sqrt(S+4)-2, which must be handled separately from the nonuniform interior expansion. Independently bracketed roots for 25 (S,y) pairs; no continuum result inferred from those tests.

## originality

PASS

Radiation/Robin boundary modeling and reaction-diffusion first-passage equations are classical; the exact fixed-sum two-endpoint allocation, unique positive optimum even at boundary start, strict budget monotonicity and remote sqrt-budget scaling are the assessed additional statements. Earlier work optimizing reset rate or exterior steady-state flux changes objective or domain; no exact overlapping Robin allocation theorem identified, but elementary BVP optimization makes historical overlap possible.

## value

PASS

Splitting a fixed physical endpoint-reaction budget to minimize the first arrival time is a natural operational and analytic optimization. The result is a complete parametric classification, including strict interior optimality despite endpoint starts, monotone budget crossover and an unusual sqrt(S) distant-reactivity boundary layer, not an arbitrary numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
