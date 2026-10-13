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

This result has an analytic proof and an independently replayable, self-contained exact-arithmetic checker (`verify.py`). The checker uses Python's `fractions.Fraction` only, evaluates the complete eight-dimensional vector field and Jacobian at the stated equilibrium states, generates characteristic polynomials via Faddeev–LeVerrier elimination, and constructs exact Routh first-column signs. The expected report is

```
theta 0 A 0 Routh +++++++++ RHP 0
theta 0 A 13/375 Routh ++++++++- RHP 1
theta 0 A 1/10 Routh +++++++++ RHP 0
theta 1 A 0 Routh +++++++++ RHP 0
theta_c 0.065556345820
VERIFY_OK
```

The local-instability counts are exact consequences of rational sign decisions; no finite search is used to prove the universal equilibrium count. The proof itself derives the positive-root classification for every \(\theta\ge0\), and the verifier tests rational sample identities. The check neither establishes nonlinear global convergence nor confirms absence of all possible unindexed prior literature; those limits are outside the claim. No independent audit is claimed.
