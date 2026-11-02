---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Let C=binom(n,3), B=3C, a_j=(m)_j/(N)_j. The identity W=P-3T converts induced-wedge count into centered cherry P and triangle T. Direct overlap enumeration yields exact E[T],E[P],E[T^2],E[P^2],E[TP] with common-edge or fully disjoint edge-set union probabilities a_j. Independent rational graph enumeration of ALL labelled simple graphs for n=4,5,6 across all 34 edge-count strata reproduced the finite covariance and boundaries. A separate symbolic SymPy simplification verified for arbitrary n,m the factor -C*a3*6(N-m)(N-m-1)K/((n+1)(n+2)(N-5)(N-4)(N-2)). K>0 for n>=5; n=4 gives K=24-4m>0 for 3<=m<=4. When m<=2 no triangle; when m>=N-1 counts deterministic. In G(n,p), overlap on one edge gives 3 C p^4(1-p)[2(n-3)-(3n-8)p], with positive/negative transition threshold 2(n-3)/(3n-8). Symbolic dense-limit calculations independently recovered -p^4(1-p)^2 covariance coefficient and both variance constants, giving the stated correlation. The general result follows from overlap algebra and positivity, not extrapolation.

## originality

PASS

Published work on moderate deviations for non-induced cherries and triangles and Janson subgraph statistics provide general covariance frameworks and may already cover some asymptotic constants, but the inspected results do not assert the all-n,m strictly negative induced triangle–open-wedge finite sign and the exact positive-to-negative G(n,p) contrast. Best-of-knowledge PASS with genuine risk of an unindexed exact cross-covariance identity in older joint induced-subgraph literature.

## value

PASS

The all-parameter strict sign versus edge-count conditioning and explicit model reversal supply a natural interpretable random-graph dependence phenomenon. Exact finite boundaries and a nontrivial factored positivity polynomial go beyond computing an arbitrary isolated moment; known marginal concentration and asymptotic covariance alone do not establish this sign classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
