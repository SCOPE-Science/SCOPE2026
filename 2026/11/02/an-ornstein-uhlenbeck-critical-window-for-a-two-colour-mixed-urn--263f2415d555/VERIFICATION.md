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

The theorem's analytic proof is in `RESULT.md`; the finite and numerical checks below are supplementary and have no authority to certify an infinite-dimensional probability limit.

The complete standalone checker is `urn_window_verify.py`; it requires only Python 3 standard libraries. Run from the directory containing the files:

```sh
python3 urn_window_verify.py
```

The program was executed against this version and returned:

```text
exact assertions passed: 2917
asymptotic diagnostics passed: 56
Total passed: 2973
```

The exact tests enumerate finite two-colour difference laws at several rational mixture probabilities through twelve draws, verify probability normalization and the exact conditional drift, reconstruct the first two moments from their finite-state probabilities, and test the harmonic critical identity for five hundred parameter values. Numerical diagnostics evaluate the exact moment recurrence in the inverse-log critical window and independently approximate the deterministic bracket integral for \(\tau\in\{-2,-1,-1/2,0,1/2,1,2\}\).

The central infinite claim is **not** established by these tests. Its proof requires the gamma-product representation, a uniform second-moment bound, the negligible dependent predictable-bracket correction, the Lindeberg criterion, functional martingale convergence, the left-endpoint Doob estimate, and a separate exact variance recurrence, all supplied in `RESULT.md`. The limiting covariance and the \(\tau=0\) specialization are checked symbolically in the argument. No independent audit, formal proof assistant or external certification was performed.
