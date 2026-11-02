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

# Reproducibility and proof boundaries

The file `verify.py` uses only the Python standard library. From the directory containing the delivered files, execute:

```sh
python3 verify.py
```

The executable checks the exact integer reduced-Laplacian determinants against the Chebyshev product over multiple graph sizes and conductances, verifies stationarity for interior optima, compares the unique predicted orbit-constant solution against budget-normalized, individually asymmetric alternatives, and checks numerical approach in both asymptotic regimes. The recorded run passed **815 assertions**.

These are finite diagnostics, not an exhaustive search or a proof of the all-parameter theorem. The critical infinite claims are established in RESULT.md by strict logarithmic-determinant concavity, the exact Fourier product, the sign of the endpoint derivative, and two analytic limiting arguments. Independent mathematical examination remains unperformed.
