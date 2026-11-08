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

The sole critical point is c=sqrt(2)-1. Exact critical three-return numerator factorization gives (-577+408 sqrt(2))*(mu-1-sqrt(2))*Q(mu). mu=1+sqrt(2) produces a fixed point, not primitive three. Transformed polynomial coefficients Q(4t/(1+t))*(1+t)^6 are all negative; Q(4+t) has one sign change; Q(4)<0 and leading coefficient positive give a unique mu>4 root inside [56449/10000,1129/200], near 5.64492767524668. Exact rational/surd endpoint inequalities in RESULT.md give K_mu(J) subset int A, K_mu(A) subset int B, K_mu(B) subset int J for J=[.413,.415], A=[.9685,.9686], B=[.0872,.0875], and |(K_mu^3)'|<.11. Contraction proves an attracting least-period-three cycle for the whole band, not a maximal band.

## originality

PASS

Exact unique supercritical primitive-period-three parameter and a rigorously certified attracting interval for the named rational logistic family; existing primary reports studied same map but numerical bifurcation windows and lower-period stability do not imply exact algebraic existence and uniform contraction.

## value

PASS

An explicit superattracting period-three algebraic root and robust certified attraction interval are meaningful nontrivial dynamics in a named chaotic-map model, distinguishing stable windows from merely numerical chaos plots and giving an exact reproducible benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
