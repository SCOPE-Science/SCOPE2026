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

# Verification of the information-backflow band

Run `python3 verify_memory_backflow.py` from the directory containing `backflow_cover.csv`. Only the Python standard library is required. This reads 786 rows and tests each Kummer-series comparison using exact rational arithmetic; it also checks the integer factorial tail bound, that intervals cover the entire real rate interval \([1/5,1/2]\), and that each local strict increase exceeds \(1/400\) after Lipschitz extension.

Observed output in the completed package:

```
PASS: 786 exact rational local certificates cover 0.2 <= r/omega <= 0.5
Final covered endpoint: 0.500012808824
Uniform trace-distance increase: > 1/400 = 0.0025
Global Kummer truncation remainder < 1e-30
```

The script verifies a finite rational certificate. The mathematical reasons why the Kummer series describes the quantum protocol, why the two-state trace distance equals its modulus, and why the Poisson coupling extends the finite cover to all real parameters are given in `RESULT.md`. The certificate does not establish a sharp global boundary for information backflow, universal monotonicity outside the stated band, or an independently audited result.
