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

The source file `verification/check_pq_star.py` uses Python 3 and only its standard library. From this directory run:

```
python verification/check_pq_star.py
```

The observed result is `PQ_STAR_LOEWNER_EXACT_CHECKS_PASSED sizes=9 vertices=144 positive_contacts=138`.

For each integer \(1\le m\le9\), the checker constructs the full vertex set directly from the star PQ construction, verifies the nonnegative rational vertex weights, calculates the full covariance matrix independently from weighted centered vertices, checks every entry against the proposed analytic projection decomposition, and evaluates the three Mahalanobis squared distances exactly. It distinguishes the zero-weight but boundary-contact hub vertex at \(m=4\) from the strictly interior hub at \(m\ge5\). It also checks covariance eigenvalue positivity and the continuity of parameter formulas at the transition.

The general result for every integer \(m\ge1\) is justified by the symbolic covariance and vertex-orbit identities and the determinant optimality argument in `RESULT.md`. The nine tests are a reproducibility check, not an exhaustive or independent proof for all parameters. Verification uses the actual embedded checker file; no outside computation certificate is required. No independent mathematical audit was performed.
