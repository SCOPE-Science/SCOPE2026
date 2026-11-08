---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the central plane O∩(q,t,1)^perp with 0<=q<=t<=1, independently checked its six edge-intersection polygon vertices, area B(q,t) and diameter D(q)=2sqrt(1+q²)/(1+q). Exact symbolic differentiation of B(q,t)^2 equals a negative positive-factor multiple of P_q(t), where P_q is concave with P_q(q)=3q(1-q)>0 and P_q(1)=-3q²(1-q)<0. Therefore for 0<q<1 its unique positive root T(q) lies strictly inside (q,1), and B is decreasing then increasing. The endpoint gap B(q,q)^2-B(q,1)^2=2(1-q)^3/(1+q)^3>0 proves unique maximum at t=q. Continuity supplies every intermediate area. The q=0,1 degenerate sections yield D=2 with area [sqrt2,2] and D=sqrt2 with A=3sqrt3/4; inversion of D checked. Symbolic identities and independent numerical polygon checks corroborated exact analysis; no finite sample substitutes for continuum sign proof.

## originality

PASS

Best-of-knowledge mathematical implication comparison of actual primary material and published records. Novelty is provisional, with explicit unresolved historical-source risks.  The prior exact octahedron diameter formula is explicitly excluded from the novelty assertion.

## value

PASS

This solves the entire sharp two-invariant area–diameter feasibility region for central sections of a canonical polytope, including a rigid unexpected asymmetric interior minimizer, a distinct symmetric maximizer and endpoint degeneracies. The conditional classification is mathematically stronger and different from the known marginal diameter law, and serves as an exact benchmark for convex section geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
