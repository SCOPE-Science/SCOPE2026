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

Run `python3 verify_zero_product_fourier.py` in the same directory. The checker uses only Python's standard library. It enumerates all composable pairs satisfying \(XY=0\), transforms their indicator using exact integer or Eisenstein-integer character arithmetic, and checks every frequency for the congruence, nonvanishing, and extremal singular values in five finite instances. The following outputs were observed from that standalone file before packaging:

```
EXACT_OK q 2 a 2 b 2 ambient 256 set_size 58 min_modulus 2 unique_eigenvalues 7
EXACT_OK q 2 a 3 b 2 ambient 4096 set_size 274 min_modulus 2 unique_eigenvalues 7
EXACT_OK q 2 a 3 b 3 ambient 262144 set_size 6168 min_modulus 8 unique_eigenvalues 13
EXACT_OK q 3 a 2 b 2 ambient 6561 set_size 417 min_modulus 3 unique_eigenvalues 7
EXACT_OK q 4 a 2 b 2 ambient 65536 set_size 1636 min_modulus 4 unique_eigenvalues 7
ALL_ZERO_PRODUCT_FOURIER_EXACT_TESTS_OK
```

These checks are exhaustive only for the listed finite instances. The theorem for all prime powers and dimensions is proved by the exact subspace Möbius identity and the divisibility argument in RESULT.md. No software-based or external independent audit has been performed. Priority against every possible historical theorem is not certified.
