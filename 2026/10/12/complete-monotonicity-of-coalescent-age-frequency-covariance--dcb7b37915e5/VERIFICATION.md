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

Independence of exponential holding times T_k and merger topology gives c_(n,r)=sum_k E[W_(k,r)]Var(T_k). With the established E[W]=k C(n-r-1,k-2)/C(n-1,k-1) and Var(T_k)=4/[k²(k-1)²], obtain exact sum. Repeated Pascal finite difference yields nonnegative binomial terms and a strictly positive k=j+2 summand in every permitted order; n=2 boundary and r endpoints included. Product-form expectation and uniform 8/[k(k-1)] majorant justify dominated convergence for r/n->alpha including alpha=0,1; sum gives g(alpha). Independent exact Fraction computations n=2..13 confirmed every defined alternating difference and c_n1=4/n,c_n,n-1=2/(n-1). Those finite checks do not replace infinite proof.

## originality

PASS

Known branch-size expectation and generic coalescent moment-computation frameworks are credited prior. The new specific strict all-order finite-frequency inequalities and explicit macroscopic covariance profile are not the fixed-r first-moment statements or generic computational method in the inspected primary literature.

## value

PASS

The exact signs of every frequency difference and nonconstant scaling profile describe a natural frequency-resolved covariance structure in Kingman genealogies, beyond one-off moments and a useful analytic input to frequency-spectrum comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
