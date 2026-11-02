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

# Reproducibility and limitations

The supplied `verify.py` requires Python 3 and no third-party packages. From a directory containing `verify.py`, run:

```shell
python verify.py
```

The observed output from the packaged scientific script was:

```text
CHECKS_PASS 25394
```

The script independently evaluates the full damped RKC stage recurrence and the stability polynomial in exact rational arithmetic for even stage counts from two to eight and several strictly positive damping values. It also enumerates finite sign sequences exactly and checks their first and second moments against the claimed finite-time recursion. Numerical checks cover negative Chebyshev extrema, strict interior contraction, sharp variance bounds, exact threshold \(T_s(\omega_0)=2\), small-damping scaling, and the large-stage limiting formula. These are reproducibility checks, not claims of external validation or complete machine certification of an infinite-parameter proof.

The mathematical proof establishes the infinite random-series representation, the exact support and its connected-component classification, the uniform sharp variance maximum and the asymptotic threshold. It depends on the stated fair independent outer samples, same-sample internal stages, strictly positive damping, exact scalar quadratic gradients, even stage count and \(0<t<H\). No theorem is claimed for finite-precision effects, nonlinear stochastic losses, odd stage counts or the undamped neutral points. Published priority beyond the inspected material is not independently certified.
