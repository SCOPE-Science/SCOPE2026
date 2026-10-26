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

The claim is verified analytically from the stated model and the uniqueness criterion in the cited paper. For each fixed row, the row sum is a sum of independent Bernoulli-marked binomial variables; for each fixed column, the column sum is a sum of independent terms across rows plus an independent binomial term. Their exponential moments are bounded by the displayed constants. Markov's inequality and a union bound give failure probability at most \(n^{-q}\), and the induced matrix norm inequality controls the Euclidean operator norm.

The theorem is a sufficient condition only. The constants are not optimized, no lower bound is established, and no numerical enumeration is used to infer an infinite-family result. The result assumes independent off-diagonal Bernoulli edges with parameter \(p_0/n\) and fixed \(p_0,q\).
