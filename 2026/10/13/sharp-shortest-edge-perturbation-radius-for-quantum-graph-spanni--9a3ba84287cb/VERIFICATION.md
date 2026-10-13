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

# Reproducibility

The enclosed `verify.py` uses Python 3 standard-library exact fractions, integer graph enumeration and exact weighted-Laplacian determinants. Execute `python3 verify.py`; the recorded replay output is:

```
VERIFY_OK finite_exact_cases= 157 K3_F(5/4)= 49/12 K4_F(5/4)= 2175/64
```

The finite verification covers complete graphs of orders three through five, all connected simple graphs of orders two through four with each choice of a distinguished shortest edge, and the weighted cofactor/cotree identity on these cases. The infinite graph-order conclusion rests on the analytic proof in RESULT.md, not finite tests. The spectral determinant normalization is imported from the published source [1, Eq. (40)], not numerically derived from a finite sample. Independent audit has not been performed.
