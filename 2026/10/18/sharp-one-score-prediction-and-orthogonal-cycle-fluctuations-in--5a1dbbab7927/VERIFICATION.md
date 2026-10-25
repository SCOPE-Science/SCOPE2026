---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The deterministic score formula C=binom(n,3)−sum_v binom(S_v,2) follows by counting unique 2-outdegree winners of transitive triples. Completing squares gives C−EC=−(1/2)sum_v Q_v. For v≠w, conditioning on edge vw, the residual Bernoulli edge sums are independent, and each conditional centered square has zero mean; hence Cov(Q_v,Q_w)=0. Binomial fourth moment gives Var Q_v=m(m−1)/8, so Var C=n m(m−1)/32. Given S_v=s, non-v edges remain fair; conditional mean is binom(m,3)/4+s(m−s)/2. With specific winning set A and losing set B, triangles through v are Binomial(s(m−s),1/2); the induced tournament C0 is uncorrelated with these cross-edge indicators, establishing conditional variance 3binom(m,3)/16+s(m−s)/4. Conditional projection explains exactly 1/n of variance; symmetry implies zero linear Cov(C,S_v). Independently exhausted orientations at n=3,4,5 and every feasible s; all rational moments agreed, without using finite enumeration as an all-n proof.

## originality

PASS

Best-of-knowledge review of the final claim and stronger implications: specific exact result not found to be subsumed by inspected primary sources; acknowledged overlapping premises and priority risks are itemized.

## value

PASS

Predicting cyclic-triangle counts from one vertex outdegree in the canonical fair tournament is a natural local-to-global inference problem. The exact nonlinear optimal predictor, complete conditional mean/variance at each score, and precisely 1/n explained-variance fraction give a meaningful finite-parameter fluctuation law, rather than simply rewriting the classical deterministic score identity. The shortness of some deductions is not by itself a value failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
