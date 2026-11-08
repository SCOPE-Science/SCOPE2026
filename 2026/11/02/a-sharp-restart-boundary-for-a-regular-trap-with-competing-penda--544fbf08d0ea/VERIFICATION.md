---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

At every core vertex, next-step return to apex has probability q=r+(1-r)/(d+1), independent of core topology; decoys return after one step. This proves exact strong lumpability of the target, core, decoy, apex classes. Solving first-step PGF equations yields the stated rational pgf, and differentiating F=(m+L)/(1-r)+m(d+1)/(1+dr)+L-1 proves strict convexity, unique minimizer r=0 iff md(d+1)<=m+L and otherwise r*=(sqrt(md(d+1)/(m+L))-1)/(sqrt(md(d+1)/(m+L))+d). Core geometric excursions coupled by inverse uniforms give stochastic monotonicity in d. For m,d->infinity, L/m->lambda<infinity, success at each apex trial is p~1/[m sqrt(1+lambda)(1+sqrt(1+lambda))], failed-trial duration has limiting mean 2 and bounded second moment, implying T/m exponential with mean 2 sqrt(1+lambda)(1+sqrt(1+lambda)); exact mean agrees. Independently recomputed 36 exact rational full-vertex expected hitting times including nonisomorphic 2-regular C6 vs disjoint triangles; proof establishes all admissible cores.

## originality

PASS

Qualified best-of-knowledge PASS for full topology-invariant law and sharp pendant-count optimization and rare-target exponential asymptotics; elementary renewal identities are prior tools.

## value

PASS

An apex connected to a regular trap and L decoy leaves is a natural search model with competing long excursions and fast failures. Exact all-deadline topology invariance, a critical pendant load, unique optimal resetting and exponential rare-target limit provide useful, motivated structural results beyond generic reset formula substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
