---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Stationarity of H(z) for arbitrary smooth H gives E[xy|z]=bz. Exact derivative (x²+s w²)/2 has σ(xy−x²−s w²), yielding E[x²]+sE[w²]=bm. Derivative balances of y²/2 and z²/2 eliminate E[xyz] and give E[y²]+b Var(z)=bm(r−m). Since b,r>0 this implies 0≤m≤r; m=0 forces y=z=x=w=0 on invariant support, whereas m=r would require dot z=−br while support sits at y=0,z=r, impossible. Conditional orthogonality yields Var(xy)=b² Var(z)+E dot z² and Cov(z,xy)=b Var(z), with correlation only for positive Var(z).

## originality

PASS

Relevant 2013 same-object full article and earlier bifurcation/boundedness sources do not supply all-invariant-measure conditional law or exact stationary parabola. Prior quadratic cancellation is acknowledged; the genuinely additional statement combines a fiberwise regression with coupled second-moment geometry. Best-of-knowledge with older 2010 bounds full-text access risk.

## value

PASS

The moment parabola and sharp invariant-mean interval constrain all compact stationary states of a natural atmospheric-wave feedback system, and the speed defect makes a measurable exact covariance relation; this has mathematical and dynamical motivation beyond routine numerical parameter checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
