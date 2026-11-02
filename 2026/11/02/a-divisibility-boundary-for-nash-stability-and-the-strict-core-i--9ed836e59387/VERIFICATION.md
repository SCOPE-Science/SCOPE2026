---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof checks

The exact necessary-and-sufficient determinant inequality is proved by expanding all directed type-\(A\) and type-\(B\) unilateral utility comparisons. A separate Cauchy–Schwarz identity fixes both the optimum and its equality case; integral residuals give the divisibility direction. In the other direction, coalitions of the two sizes \((1,q)\) and \((1,q+1)\) prove inefficient Nash stability, and a directly constructed weakly blocking coalition proves failure of strict-core stability. The labeled count uses an exponential generating series.

Run `python verification/checker.py` from the package root with Python 3 and no third-party dependencies. The checker calculates all individual unilateral utility comparisons by cross multiplication independently of the theorem's determinant test. It enumerates every partition of the labeled population for \(25\) pairs with \(a+b\le10\), totaling \(684404\) tested partitions and \(5155\) Nash-stable incidences. It checks the determinant condition, divisible-case type proportions and rational social optimum, enumerative formula, explicit nondivisible equilibria and exact welfare deficits. Its terminal line is:

```
PASS: 25 parameter pairs, 684404 labeled partitions, 5155 Nash-stable incidences, direct deviations = determinant and divisibility/generating-function/witness checks all passed
```

The finite computation is not used as a proof of the universal statements. Publication priority remains subject to additional independent literature review. Independent audit has not been performed.
