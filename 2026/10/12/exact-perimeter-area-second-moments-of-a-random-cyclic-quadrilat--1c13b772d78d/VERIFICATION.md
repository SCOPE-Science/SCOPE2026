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

Four iid uniform points ordered cyclically give gaps Dirichlet(1,1,1,1). P=2Σsin(πD_i), A=(1/2)Σsin(2πD_i) by chord lengths and oriented shoelace; for cyclic four-point order the signed total is the nonnegative polygon area. The marginal density 3(1−x)² and bivariate density 6(1−x−y) integrate eight required sin-product expectations. Recalculated all eight elementary trig integrals independently with SymPy, reproducing EP=24(π²−4)/π³, EA=3/π, EP²=8+132/π², EA²=1/2+105/(16π²), EPA=140/(3π²) and Cov=4(216−19π²)/(3π⁴)>0. A 1,000,000-sample independent seeded Dirichlet Monte Carlo yielded covariance 0.389921 vs exact 0.389800 (diagnostic only); symbolic integrals prove claim for radius one.

## originality

PASS

Finch (2016) explicitly leaves joint perimeter–area analysis open and derives E[A²] only under a conjectured angular density; the present exact Dirichlet pair integral proves that value and yields E(PA)=140/(3π²). Wang–Li–Xu (2023) gives the general sine-Dirichlet representation and n→infinity asymptotics but its inspected full paper does not state this finite-four covariance. Ingredients credited; exact natural mixed moment is a best-of-knowledge new evaluated result.

## value

PASS

The natural joint area–perimeter dependence of a fixed four-vertex random cyclic polygon was explicitly left open by the primary study. Exact covariance and correlation quantify that dependence and the unconditional area second moment removes reliance on a proposed but unproved angular density. Four vertices are the object of a well-established concrete problem, not an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
