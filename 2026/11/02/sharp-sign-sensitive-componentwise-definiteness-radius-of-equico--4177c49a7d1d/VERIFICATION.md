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

# Reproducibility and limits

Run `python3 verify.py` from a directory containing the adjacent standalone `verify.py` file. The script requires only the Python standard library. It compares all sign-vertex matrices through exact-rational Schur-complement elimination for dimensions \(2\) through \(7\), using six correlation values per dimension: two admissible negative values, zero, and three positive values. For each set, it checks all sign vectors up to a common sign flip on both sides of the derived boundary and verifies even/odd comparisons on the positive branch. The recorded output was:

```
PASS: 36 independent parameter settings; 1512 exact-rational vertex LDL tests; both sides of each threshold and parity checks.
```

The calculations check finite rational samples only. Universal statements, exact endpoint singularity and the formulas in real parameters are established analytically in `RESULT.md`. Numerical evaluation of the threshold in the verifier uses 65-digit decimal arithmetic solely to choose rational points on the two sides; all positive-definiteness tests use exact fractions. Independent audit has not been performed.
