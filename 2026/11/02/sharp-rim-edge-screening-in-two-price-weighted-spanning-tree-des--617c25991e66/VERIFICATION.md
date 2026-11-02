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

The proof in `RESULT.md` is analytic and applies to all integer wheel sizes \(m\ge3\) and positive real prices and budgets.

To reproduce the supplementary finite checks with Python 3 (standard library only), run:

```sh
python3 verify.py
```

The exact-rational tests independently build each grounded Laplacian and compare its determinant with the proposed closed form. The derivative identity is tested with rational substitutions across many dimensions. The numerical tests check the scalar root and asymptotic bounds; perturbed edgewise nonuniform feasible allocations are evaluated by a separate Cholesky log-determinant routine.

Expected result: `VERIFY_OK exact=2725 analytic_numerical=292 asymmetric=1800 total=4817`.

These finite tests are not an exhaustive enumeration of all real parameters or all edge allocations. The global and infinite-dimensional quantifiers are established by the strict-concavity, exact Fourier-product, scalar monotonicity, and limit arguments in the proof. Independent audit is not yet performed.
