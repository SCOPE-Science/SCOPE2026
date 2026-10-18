---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For x0=(1,0), every y=(u,v) on the square has A=||x0+y||_inf and B=||x0-y||_inf with max(A,B)<=2 and min(A,B)<=1; Heinz monotonicity gives M_nu(A,B)<=M_nu(2,1), equality at y=(1,1). For arbitrary x, signed permutations reduce to (1,a), 0<=a<=1, and witness y=(1,-1) gives norms (2,1+a), so the reverse inf-sup bound holds. The argument handles nu=0,1 by the stated continuous arithmetic endpoint and nu=1/2 by geometric mean; axis attains infimum.

## originality

PASS

Best-of-knowledge new exact lower constant interpolating an explicit interval in the defining primary paper; related 2022 H_nu is a different optimization problem.

## value

PASS

Closes the explicit interval left in the defining study of a natural Banach-space geometric invariant; computes the full continuous parameter dependence and actual minimax geometry rather than an ad hoc table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
