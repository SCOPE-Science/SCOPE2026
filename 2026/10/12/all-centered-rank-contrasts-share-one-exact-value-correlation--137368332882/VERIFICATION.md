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
# Verification

The proof is analytic for every \(N\ge2\), every nondegenerate atomless parent with finite variance, and every nonzero deterministic zero-sum contrast.

`checker.py` performs three exact-rational consistency checks. It enumerates all rank permutations for uniform samples through \(N=8\) and verifies the contrast covariance and rank variance for several distinct contrast directions. It enumerates every pooled-rank allocation for every two-sample split through total size \(N=12\) and verifies the Mann-Whitney covariance and correlation-squared formulas. It also checks the sharp Gini-variance bound for the beta-power family with distribution function \(F(x)=x^k\) on \([0,1]\) through \(k=500\).

The computations use no floating-point approximation. They supplement rather than replace the universal proof.
