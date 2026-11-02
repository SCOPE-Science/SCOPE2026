---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

From homogeneous BDF1 half-step and doubly stabilized CN endpoint, m=u+h u(1-u²)/(2+sh) and Phi=[(1/h+vh-s/2)u+(s+1)m-m³]/(1/h+vh+s/2). For s>=2, delta<1/2, e=delta u(1+u), m=u+(1-u)e, and R(u)=s e+m(1+m)(1-e) is strictly increasing on [0,1], since R'= (s-m(1+m))e'+(1-e)(1+2m)m'>0. Thus Phi([0,1]) subset [0,1] iff a+s/2>=R(1), algebraically Q>=0; Q<0 yields open overshoot near 1. For s<s_c, replacing h by inverse t shows the positive threshold F_s has one maximum (strict decreasing cubic derivative); reentrance has exactly two roots below v_*(s). Boundary s=2 gives v*=1/4 and s>=s_c all steps safe. With interval invariance, strict inward motion guarantees convergence by monotone bounded iteration. Independently checked derivative identity symbolically and exact offending u=9/10,s=4,v=0,h=2 giving Phi=313211996289/312500000000>1.

## originality

PASS

Hou–Ju–Qiao 2023 original equations (2.11a,b) and Theorem 2.1 establish a sufficient full-grid maximum-bound condition, not necessary/sufficient homogeneous scalar conditions. Their unconditional sufficient bound in second stabilization includes mesh dependence. The current statement exactly restricts to spatially homogeneous solutions and adds necessity plus a reentrant safe-unsafe-safe step interval. Prior CN/AB two-level results use different extrapolation and cannot be substituted. Qualified best-of-knowledge assessment.

## value

PASS

A sharp invariant-region threshold for the actual published integrator is structurally meaningful: it distinguishes necessary homogeneous restrictions from conservative sufficient gridwise conditions, gives explicit unsafe data, and discovers nonmonotone step-size safety. This is a natural numerical-analysis phase diagram with practical diagnostic use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
