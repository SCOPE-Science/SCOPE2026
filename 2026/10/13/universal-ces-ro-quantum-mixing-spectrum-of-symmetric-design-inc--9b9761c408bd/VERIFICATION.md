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

# Reproduction and scope
Run `python3 verify.py` in the directory containing the script. It uses only Python's standard library and exact `fractions.Fraction` arithmetic. Expected output:

```
VERIFY_OK exact_designs=5 exact_matrix_entries=1456 ranks=3:3,4:4,7:13,11:21,13:25
```

The five constructed incidence graphs are symmetric-design cases of orders 6, 8, 14, 22, and 26. The script verifies design identities, squared-singular-space projector relations, the exact Cesàro block formula, its annihilating spectral polynomial, and matrix ranks with rational Gaussian elimination. The case with 11 points is a symmetric biplane, not a projective plane, testing the unrestricted design parameter. The nontrivial rank bound is independently checked by exact elimination. The theorem for all integer parameters relies on the printed proof; no claim of exhaustive parameter testing or independent audit is made.
