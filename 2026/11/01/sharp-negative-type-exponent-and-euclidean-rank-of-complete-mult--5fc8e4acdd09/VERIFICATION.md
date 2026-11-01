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

# Verification and reproducibility

`checker.py` is included in the same package. Run with Python 3, NumPy, and SymPy installed:

```bash
python checker.py
```

Actual result on the packaged program:

```text
PASS: 1730 exact-rational, symbolic and numerical assertions on finite part-size profiles.
Limits: finite matrices and numerical eigenspectra are diagnostics, not the proof.
```

The program verifies the exact zero-sum quadratic identity for rational input \(\rho\), symbolic small-profile threshold polynomials, and the signs/nullities of compressed negative-distance forms for assorted parts in dimensions up to 16. Floating-point eigenvalue and binary-search evaluations use explicit tolerances, so those comparisons are numerical diagnostics only. The analytical steps proving the all-dimensional claim are given in `RESULT.md`: exact block decomposition, Schur complement, monotonic unique root, explicit negative witnesses, and Schoenberg's embedding-dimension criterion. No independent mathematical validation has been performed.
