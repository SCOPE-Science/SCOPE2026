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

# Reproducibility and scope of checks

The self-contained `verify_kneser_exact.py` was run with Python 3 and emitted:

```text
CHECK_OK adjacency_matrix_entries= 123188 exact_signed_certificates= 767 rational_spectral_heat_tests= 225
```

It checks the adjacency-square identity for every entry of each \(KG(n,2)\) with \(5\le n\le19\); verifies exact signed-filter certificates, including all six Petersen polygon witnesses and the outsider-permutation matching; and verifies exact rational spectral-multiplier heat identities. All rational comparisons are exact.

The supplemental `check_kneser_lp.py` requires NumPy and SciPy (`scipy.optimize.linprog` and `scipy.linalg.expm`). It was run successfully and emitted:

```text
n 5 signed/heat passed
n 6 signed/heat passed
n 7 signed/heat passed
n 8 signed/heat passed
n 9 signed/heat passed
CHECK_OK signed_and_heat_lp_checks 75
```

It compares the claimed norms to direct Kantorovich-dual optimization over graph-edge inequalities and to matrix-exponential heat rows. These are floating-point checks with numerical tolerances, not exact certifications.

The proof in `RESULT.md` is the source of the all-dimensional and all-time claims. Neither finite checker verifies the entire infinite parameter domain, nor has an independent mathematical audit been performed.
