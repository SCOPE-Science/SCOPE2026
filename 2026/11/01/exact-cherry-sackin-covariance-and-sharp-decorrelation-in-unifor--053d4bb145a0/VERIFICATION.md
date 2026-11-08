---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Derived the first and mixed raw moments from Catalan root decomposition: T=x+T², C=2TC+x², S=2TS+x(T²)′, M=2TM+2CS+x(2TC)′+2x², with T=(1-sqrt(1-4x))/2. The finite coefficient identities imply Cov(C_n,S_n)=n/(2n-3)*(n-1-n q_n/4), q_n=4^(n-1)/binom(2n-2,n-1). Independent enumeration of every plane binary tree for n2..8 gave covariance 0,0,-4/25,-20/49,-46/63,-406/363,-8744/5577, matching the formula; checked cherry variance from marker second derivative. Exact adjacent ratio q_(n+1)/q_n=2n/(2n-1) exceeds a_(n+1)/a_n=n²/(n²-1), a_n=4(n-1)/n, yielding negative covariance for all n≥4, not a finite extrapolation. Established uniform-model Sackin variance asymptotic (10/3-pi)n³ is explicitly cited external input; Catalan central binomial asymptotic then gives covariance ~-sqrt(pi)n^(3/2)/8 and sqrt(n) Corr→-sqrt(pi)/(2sqrt(10/3-pi)). Correlation undefined n2,3 because Var C_n=0.

## originality

PASS

Blum–François–Janson provide the uniform Sackin variance and a different (Colless) correlation, while the relevant fringe-tree papers focus on marginal cherry or other subtree statistics. The exact mixed cherry–Sackin identity and universal negative sign were not located in the inspected primary results or topical mathematical-record search. Credit the cited variance constant and all Catalan fundamentals as prior; assessment is qualified.

## value

PASS

Cherry count is a standard local shape index and Sackin depth a standard global imbalance index, making their covariance and sharp decorrelation rate a natural quantitative test of redundant information in a phylogenetic null model. An exact sign boundary at n4 and the explicit asymptotic constant are meaningful beyond separately known marginal moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
