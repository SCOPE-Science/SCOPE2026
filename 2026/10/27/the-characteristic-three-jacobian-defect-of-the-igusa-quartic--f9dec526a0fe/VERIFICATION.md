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

The exact computation script `verify_char3_igusa.py` was run with SymPy 1.14.0. Its output was:

```text
VERIFY_OK
pair_partition_lines=15
direction_point_hilbert_ranks_deg_0_to_3= [1, 4, 10, 15]
jacobian_hilbert_series= (-t**6 - 3*t**5 + 3*t**4 + 6*t**3 + 6*t**2 + 3*t + 1)/(t**2 - 2*t + 1)
reduced_union_hilbert_series= (5*t**3 + 6*t**2 + 3*t + 1)/(1 - t)**2
excess_sheaf_length= 6
hessian_rank_at_(0,0,1,1,2)= 3
```

The script checks exact arithmetic over \(\mathbb F_3\), the 15 pair partitions, direction-point ranks, the leading monomials of a Gröbner basis for the Jacobian ideal, the resulting Hilbert-series comparison, and the Hessian rank at a point where the three pair-values are distinct. The analytic proof of the support classification is given in `RESULT.md`.

Limits: the script verifies the finite computations used in the proof; it does not determine the full local Artin-algebra isomorphism type of the embedded excess. The original 1962 paper's full text was not obtained. No independent audit or independent validation is claimed.
