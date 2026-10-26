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
# Exact verification

Run `python verify.py` in this directory after installing SymPy 1.12 or newer. The script reads the embedded `CERTIFICATE.json`, regenerates all twenty-four integer polynomials, verifies their products of listed integer factors, and tests every modular witness using exact finite-field arithmetic. It checks squarefreeness at each witness prime, the irreducibility evidence for all twenty-eight nonlinear factors, the discriminants \(-23\), \(-31\) and \(257\) used for field disjointness, and the reported group-frequency vector.

The script was executed with a successful result:

```
CERTIFICATE_OK rows=24 nonlinear_factors=28 groups={'S7': 8, 'S6': 8, 'S3xS3': 4, 'S3xS4': 4}
```

The mathematical implications from certified Frobenius cycle types and common-quotient exclusions are supplied in `RESULT.md`. Finite computational output does not on its own prove those group-theoretic lemmas. No external or independent audit was performed.
