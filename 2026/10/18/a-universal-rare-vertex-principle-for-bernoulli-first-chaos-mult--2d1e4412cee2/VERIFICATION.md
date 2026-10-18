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

The proof is analytic. Its decisive steps are the endpoint-secant convex-order comparison for two centered Bernoulli variables, successive conditional replacement of input-vertex coordinates, and a telescoping binomial identity. No finite check is used to justify any all-dimension assertion.

Running `python verify.py` in an ordinary Python 3 environment produced:

```
PASS: exact rational row inequalities: 126
PASS: homogeneous closed forms: 60
PASS: complex-valued row comparisons: 62
Finite checks do not prove the universal theorem or asymptotic limits.
```

Exact rational enumeration verifies the matrix-kernel implementation and all heterogeneous vertex comparisons for the supplied dimensions; floating-point complex checks use a tolerance of \(10^{-10}\). Asymptotic limits were established by analytic probabilistic arguments rather than numeric extrapolation. Independent audit has not been performed.
