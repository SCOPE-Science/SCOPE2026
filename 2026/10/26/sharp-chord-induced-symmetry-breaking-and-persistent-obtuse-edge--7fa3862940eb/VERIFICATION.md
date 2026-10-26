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

# Verification record

The analytical claim covers every integer \(m\ge4\) and every positive chord weight \(\kappa\). Its proof uses explicit vertex force balances, a strictly increasing scalar coupling map, fixed-endpoint harmonic-energy minimization, rank-one inertia, and a Taylor expansion. The signed chord contribution is treated explicitly even when its cosine is negative.

Execute `python3 verify.py` from the directory containing this document, using only the Python standard library. Observed output:

```
VERIFY_OK
SIZES 4 5 6 7 8 9 12 16
VECTOR_FIELD_AND_HESSIAN_TESTS 232
CRITICAL_K_M4 0.3535533905932738
OBTUSE_END_K_M4 0.541196100146197
Finite numerical corroboration only; all-size proof analytical
```

The script separately assembles the full edge-based vector field and Hessian, verifies direct equilibria at four reflected/oriented branches, tests positivity of the phase quotient minor, and identifies a negative twist Hessian direction beyond the exact onset. Tests are finite floating-point checks and do not replace the complete proof or constitute external audit. Independent scientific audit has not been performed.
