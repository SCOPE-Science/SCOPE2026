---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two equilibrium balance equations give a unique inverse at every interior occupancy and ab=ef/[(1−p)(1−q)]>ef. The positive equilibrium for such rates is unique by direct substitution. In log odds X=log(p/(1−p)), Y=log(q/(1−q)), the budget is E exp(X)+F exp(Y)+E exp(X−Y)+F exp(Y−X). It is strictly convex and has bounded sublevels above the two finite log-odds target floors. Its two partial derivatives sum to E exp(X)+F exp(Y)>0, so at least one target binds. Setting the Y derivative to zero at p=u gives exp(Y)=r; setting the X derivative to zero at q=v gives exp(X)=t. The latter edge minimum reaches p=u when v/sqrt(1−v)=s, with the stated radical solution. At (u,v₋) the Y derivative vanishes so the X derivative is strictly positive, making the X edge minimum strictly below u there; monotonicity of t in v gives v₋<v₊. Strict convexity and the edge derivative conditions yield exactly the three reported branches, with equality at their shared endpoints. Substitution gives the stated costs (the edge terms in inverse odds and odds are equal at their optimum). The claimed attracting equilibrium follows from the invariant square and cooperative flow: at h times the equilibrium, 0<h<1, each derivative is strictly positive by the balance equations, and at (1,1) both are negative. Monotone solutions from those bounds converge to the same unique positive equilibrium and sandwich every strictly positive initial state. The proof's word 'beats' at an inclusive phase boundary should be read as equality there; the Finding explicitly has the correct coincident branches.

## originality

PASS

The supported distinct claim is the exact unique minimum and full three-regime phase diagram for two simultaneous positive equilibrium occupancy floors and fixed extinction rates. The balance equations, elementary log-convex programming tools and positive-equilibrium threshold are not credited as new. Nearby catalogue allocations address different objectives, and the closest inspected network allocation problems constrain decay to the zero state instead of two positive equilibrium coordinates.

## value

PASS

The two separate occupancy targets are natural constraints in the seasonal model. The phase diagram determines when the cheapest policy deliberately exceeds one target and precisely where both targets start or stop binding. It yields cost and the two separately implementable rates at all targets, a usable quantitative answer distinct from simply checking persistence or solving for equilibrium.

The dated certificate retains the supplied scientific assessment, sources and limitations.
