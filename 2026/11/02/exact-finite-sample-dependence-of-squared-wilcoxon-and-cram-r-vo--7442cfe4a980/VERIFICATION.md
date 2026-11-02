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

The proof derives the finite-population quadratic-form covariance by decomposing zero-row-sum symmetric kernels into constant, first-order, and degenerate second-order components. The coefficients follow by sampling without replacement; no limit theorem is used for the finite-sample statements.

Run `python3 check_rank_energy.py` from the package directory. This checker uses only the Python standard library, enumerates every binary word of each split for \(3\le N\le11\), and compares the exact mean, covariance, and both variances. It also checks the strict covariance sign and the equality classification. Observed: `PASS: exact enumeration N=3..11, every 1<=a<N; 486 rational assertions`.

Finite tests do not establish the all-size theorem: the algebraic proof in RESULT.md does. Historical-priority comparison is incomplete where cited primary full texts are inaccessible. No independent audit has been performed.
