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

# Verification of the mathematical claim

The mathematical proof uses the exact conditional Brownian bridge splitting, a two-dimensional Gaussian posterior precision calculation, strict AM–GM optimization, singular-support KL divergence, and KL disintegration. These are universal analytic steps; no finite computation is used as a substitute for a theorem.

## Reproduce the finite diagnostic checks

Execute `python verify.py` with Python 3 standard library only, with this file and `verify.py` in the same directory. The expected deterministic console output is:

```
PASS 10704 exact-rational assertions
Example C=I, maximal conditional path information (nats): 0.143841036226
Unique maximizing cut for (a,b)=(1,4): 1/3
```

The checker uses independent exact-rational formulations of the endpoint conditional correlation, Gaussian path submatrix determinant ratios and posterior precision. It checks the optimizing cut and singular residual-noise positivity. The sampled path checks use one strictly interior observation on each side of the cut, in addition to both endpoints. The Brownian-bridge proof upgrades the finite-dimensional observation to arbitrary entire continuous path segments. The code does not purport to certify an infinite family by finite enumeration.

## Scope and remaining risk

The statement is for centered Gaussian endpoint laws, standard unit-time Brownian bridge residuals and fixed interior cuts. The independent audit remains unperformed. The classical Gaussian mutual-information literature, including the older paper by Baker (1970), may have uninspected equivalent formulations; this is a scientific priority limitation rather than evidence of a proof error.
