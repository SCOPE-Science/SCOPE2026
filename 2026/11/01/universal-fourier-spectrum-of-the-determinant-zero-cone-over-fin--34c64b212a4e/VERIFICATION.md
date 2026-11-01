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

# Reproducible checks

Run `python3 check_determinantal.py` from this directory using the Python 3 standard library. It computes the entire zero-determinant fibre, enumerates every Fourier frequency, verifies the exact eigenvalue via cyclotomic divisibility rather than floating-point thresholds, and compares the count of nonzero coefficients with the stated rank. The tested cyclic rings are integers modulo 2, 4, 8, 3, and 9; the distinct noncyclic additive example is \(\mathbb F_2[t]/(t^2)\).

Completed output:

```
EXACT_CYCLIC_OK 2 1 size 16 cone 10 rank 16
EXACT_CYCLIC_OK 2 2 size 256 cone 88 rank 160
EXACT_CYCLIC_OK 2 3 size 4096 cone 736 rank 1408
EXACT_CYCLIC_OK 3 1 size 81 cone 33 rank 81
EXACT_CYCLIC_OK 3 2 size 6561 cone 945 rank 2673
EXACT_NONCYCLIC_OK F2[t]/(t^2) size 256 cone 88 rank 160
ALL_EXACT_DETERMINANTAL_CHECKS_OK
```

These checks are finite and exhaustive **only at the named rings**. They do not constitute a general proof or independent audit. The universal statement follows analytically from the ring-character derivation, cancellation identity, and smooth determinant-lift counting in RESULT.md. No certificate of independence is claimed.
