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

# Verification of the sharp correlation cutoff

The self-contained standard-library script `verification/beta_star_verify.py` uses exact rational arithmetic. To reproduce, extract every file in this package without changing the paths and run:

```sh
python verification/beta_star_verify.py
```

It evaluates 1,260 complete sets of all distinct pair/subset inequalities for star sizes \(2\le d\le8\), every \(1\le r\le d\), and \(36\) positive rational Beta-parameter pairs. It independently compares each discrete second difference with the direct integrated probability expression. For three test cases, it also enumerates all possible infected/uninfected configurations, integrating their probabilities rather than invoking the beta-binomial tail formula.

The program outputs exact fixed-mean interactions \(-195/57344,0,3/256\) at correlations \(1/6,1/5,1/3\). All assertions passed in a fresh extraction of the delivered package. This is not an exhaustive test over positive real parameters or unbounded star sizes; those quantifiers are discharged by the analytic proof in RESULT.md. Independent audit: not performed.
