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

The accompanying `verify.py` constructs full weighted star Laplacians, diagonalizes the complete matrices and forms time-averaged mixing matrices from their eigenspace projectors. It covers 245 parameter profiles, checks matrix rank and stochastic row sums in each profile, tests explicitly predicted kernel contrasts, and verifies 192 critical moment determinants by exact rational arithmetic.

Run with Python 3 and NumPy installed:

```bash
python verify.py
```

Expected terminal marker: `VERIFY_OK` and counts of `full_laplacian_profiles=245`, `matrix_entries=21805`, and `exact_moment_determinants=192`.

The mathematical proof establishes the theorem for all positive real conductances and unbounded integers. The finite numerical tests cannot substitute for that proof; their eigenvalue grouping tolerance is appropriate to the separated test profiles, not an exact-arithmetic certificate for all inputs. No independent audit has been performed.
