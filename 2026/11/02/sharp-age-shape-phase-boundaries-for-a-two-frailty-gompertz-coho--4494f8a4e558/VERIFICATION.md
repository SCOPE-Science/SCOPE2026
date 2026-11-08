---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

From the two survival functions derive high-frailty survivor weight p(u)=1/(1+exp u) with u=k(exp(ct)-1). Population hazard H=Delta(1+u/k)(A+p), A=a/Delta, has derivative sign g(u)=A+p-(u+k)p(1-p). Its derivative is p(1-p)[(u+k)tanh(u/2)-2], whose bracket strictly increases from -2 to infinity, giving exactly one strict global minimum. At that minimum g=A-1/(exp(u*)-1), vanishing only at u*=log(b/a) and k=kc; g(0)=(k0-k)/4 and g(infty)=A>0. These signs force all four cases, with endpoint zero correctly excluded at k=k0. Nondegenerate Taylor coefficients g_k=-p(1-p), g_uu=p(1-p)(2A+1) give square-root split. Independent root counts at A=1/4 for k=0.1,1.8,2,2.95,3,3.3 matched cases; witness k=2 roots 0.634307250 and 2.418458919.

## originality

PASS

General mixture hazard identity H=E_survivor h and derivative = mean hazard derivative minus survivor-weighted variance is prior work. The specialized equal-weight two-atom shared-slope Gompertz exact fold/endpoint root census was not found in inspected accessible primary text. A closely relevant 2009 mixture-rate review was available only in limited excerpts, so specialized prior overlap is a material priority risk.

## value

PASS

The exact necessary-and-sufficient phase diagram is an interpretable structural effect of survival selection: two increasing individual hazards can yield a nonmonotone aggregate with two turning points. Boundaries and bifurcation exponents are useful for survival/hazard model theory and are not an arbitrary parametrization or small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
