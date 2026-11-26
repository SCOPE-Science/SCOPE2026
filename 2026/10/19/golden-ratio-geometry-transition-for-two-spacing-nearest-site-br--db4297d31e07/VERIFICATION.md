---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the stopped interval (−b,a), checked the killed Green kernel via its zero boundary values, continuity at the origin and derivative jump −1/D. Its integral on the right reset-success region plus the right exit Laplace probability is sinh(kb)cosh(ka/2)/sinh(kL); reflection gives the left probability. Central resets give geometric retries with mean duration equal to mean trial duration divided by success probability. Writing u=ka/2 and v=kb/2, the resulting odds are p/(1−p)=sinh(v)/sinh(u) and the mean passage time has the stated hyperbolic form. Reflection alternates site types, so two consecutive adjacent-site passages give iid cycles of mean time 2τ and displacement {−L,0,L}, symmetric with second moment 2L²p(1−p). The variance rate remains valid even with displacement–duration correlation: if K is the first cycle whose finish exceeds t, the reward martingale stopped at K has zero mean and second moment E[K] times the one-cycle second moment. The event of including cycle i in that sum is decided before cycle i. The renewal law gives E[K]/t→1/(2τ), and the discrepancy between X_t and that stopped reward sum is uniformly bounded by 2L; it changes the variance by o(t). A fixed off-site start can be transferred at the first alarm, with square-integrable displacement and finite moments of the delay. This proves zero drift and the stated centered diffusivity. Rewriting the geometry-dependent factor as 2w+(cosh(s)−1)/w for w∈[1,c), c=cosh(kL/4), gives strict convexity and endpoint difference −2(c−1)(c²−c−1)/c. Hence the clustered endpoint is never attained, only equality of limiting and regular values occurs at c=φ, and all interior asymmetric spacings are then strictly suboptimal.

## originality

PASS

The resetting process, neighboring-site first-passage program and homogeneous formula are prior. The supported distinction is the centered alternating-gap variance, including the correction to the local raw-MSD average in the accessible earlier paper, and the exact optimizer transition at fixed r,D,L. A later exact general-periodic formula does imply the two-gap dispersion and the transition by endpoint comparison; this is real overlap, not evidence of earlier priority.

## value

PASS

The simplest nonuniform geometry reveals a real discrepancy between local raw mean-square increments and the true centered long-time variance, despite zero drift. The missing conditional-mean correction changes the two-gap optimization problem. The strict switch between an unattained merger supremum and a uniquely attained equal-gap maximum gives useful geometric information, with the tie case determined exactly rather than by a rate-optimized comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
