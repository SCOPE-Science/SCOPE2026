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

Derived F_d(z)=(r^d+r^(m-d))/(1+r^m) by absorbing-interval recurrence with z=2r/(1+r^2), and M=(1-F)/(qF). Factoring mean difference H=(1-r)^2P yields reciprocal polynomial deg m-2 with P(0)=1 and P(1)=-d(m-d)kappa/6. Explicit midpoint coefficients change sign at most once so Descartes and reciprocity limit positive roots to two; plus endpoint multiplicity proves a unique crossing iff kappa>0 and none otherwise, including kappa=0. The normalized ratio is a secant slope of f(v)=sech(theta sqrt(v)), strictly convex because it is a Brownian exit-time Laplace transform, establishing strict distance nesting. Independent rational absorbing-chain matrices and coefficient signs checked m<=70.

## originality

PASS

Exact finite-ring MFPT is already in Riascos et al 2020 and 2022; the local small-q benefit criterion is already general restart theory and 2022 ring analysis. The assessed claim is stronger all-reset-probability no-reentrance and strict spatial nesting with a reciprocal polynomial root-count certificate. In primary 2022 Sec III/IV, plotted ring optima and local derivative do not furnish those global universal assertions; full relevant text inspected. Risk: a hidden implication of exact ring mean may be deemed routine, and other papers may prove uniqueness.

## value

PASS

In resetting problems negative small-q derivative need not exclude later reentrant benefits. This exact cyclic case proves local iff global, specifies one crossing over the entire rate interval and shows distances benefiting are strictly nested. The finite correction 5 distinguishes exact small cycles from Brownian continuum and yields a usable search ordering for reset targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
