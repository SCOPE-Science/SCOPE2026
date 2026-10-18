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

The source GGWP Theorem 2.6 has positive survival equivalent P(T>t)~C t^(-1/beta), C>0. The exact tail-integral formula E(T^r)=r∫t^(r-1)P(T>t)dt shows E(T^r) finite iff r<1/beta, with log divergence at equality. Thus at beta=0.5 mean is finite but second moment and variance infinite; no finite population CV, skewness or kurtosis exists. Actual source Table 1 has FOUR parameter rows with beta=0.5 reporting finite variance, CV, skewness and kurtosis; manuscript prose claims all moments there. Source theorem and strict corollary contradict these assertions. An independent high-precision positive-tail constant calculation and boundary integral check corroborate normalization.

## originality

PASS

The generic regular-variation moment criterion is classical and the source already states a strict moment theorem, neither claimed new. The scientific contribution is diagnosing an explicit contradiction in this named 2026 paper and identifying all four invalidated Table 1 rows. Searches for an issued correction did not find one; possible later corrigendum remains a risk.

## value

PASS

The correction identifies incorrect existence claims for 16 reported population descriptive entries in a current applied probability model, not merely a new algebraic restatement: readers must not use finite variance or standardized summaries at the boundary for inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
