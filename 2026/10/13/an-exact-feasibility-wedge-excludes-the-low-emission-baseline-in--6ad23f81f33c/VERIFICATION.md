---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Using A=m+(1-alpha)delta>0, D=4m theta-2(1-alpha)phi, L=A(delta theta+phi)/(2theta phi)>0, U=A^2/D, existence of positive k requires D>0. Exact independent symbolic factorization confirms U-L=-(2delta theta+phi)A(m theta-(1-alpha)phi)/[2theta phi(2m theta-(1-alpha)phi)] when D>0. This yields the necessary-and-sufficient open wedge, including excluded boundaries. Independently recomputed exact L,U for four baseline pairs: (theta,phi)=(.7,.75): (2421/1750,-729/50); (.7,.9): (897/700,-729/200); (1.45,.75): (7137/7250,729/700); (1.45,.9): (2559/2900,729/550). The third assumption can only restrict further. It is a feasibility-of-reported-assumptions finding, not falsification of out-of-domain trajectories.

## originality

PASS

The algebra is elementary and not credited as a new general inequality; originality is the particular published game’s unrecognized lower feasibility boundary and its exclusion of prominently used nominal simulations. Searched primary paper and related green-supply-chain evolutionary models, with no identified existing correction. The source-specific novelty survives bounded comparison, with document-display limitations recorded.

## value

PASS

This is mathematically motivated because a major nominal numerical branch is outside the exact domain assumed to derive equilibria and stability. Identifying the feasible wedge materially changes how the published simulations can support the theoretical model. Not a mere type check: the incompatibility affects announced model interpretation, while not proving those trajectories false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
