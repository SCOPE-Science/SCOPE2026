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
# Verification notes

The analytical proof in `RESULT.md` supplies the critical universal upper bound, the rectangular polar-partial-isometry nuclear lower bound, and the exact incidence Gram spectrum. Check the prescribed column sums, both endpoints \(b=0\) and \(a+bk/v=0\), the value \(k=1\), and the distinction between maximizing over all widths versus evaluating an arbitrary matrix.

Reproduce the finite numerical checks with `python3 verify_sparse_sign.py` after installing `requirements.txt`. In the test environment the script printed:

```
EXACT_SCHUR_COLUMN_CHECK_OK full_orbit_instances= 180
RANDOM_SUPPORT_POLAR_LOWER_CHECK_OK cases= 1155
BALANCED_HADAMARD_BOUNDARY_OK
```

These tests use floating-point singular values but exact integer incidence counts. They are finite checks only, not an independent mathematical proof or evidence of historical originality. The Schur-factorization step and the complete-design singular-value identity in `RESULT.md` are the infinite-family justification. No external scientific assessment has been undertaken.
