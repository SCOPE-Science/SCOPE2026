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

Execute `python3 verify.py` in the directory containing this file. No external modules, online data, or third-party code are required.

The program verifies three distinct descriptions of the equilibrium count: direct binary action enumeration, admissible even-parity edge enumeration, and parity-filtered two-state trace products. It exhaustively enumerates all \(1016\) type words for \(3\le n\le9\) for this comparison. It then computes exact first and second moments by enumerating all type words at each cycle size through \(n=12\), comparing these with the four-state tensor transfer expressions. It checks polynomial annihilation identities on integer-doubled matrices to avoid floating point rounding.

Observed completion markers:

```
EXACT_CHARACTERISTIC_IDENTITIES_OK
DIRECT_ACTION_AND_EDGE_ENUMERATION_OK 1016
EXACT_MOMENTS 3 13/4 25/2 zero_profiles 0
EXACT_MOMENTS 6 169/16 1021/8 zero_profiles 2
EXACT_MOMENTS 12 133225/1024 10180257/512 zero_profiles 0
VERIFICATION_OK
```

These finite results are not a proof for unbounded cycle length, for other behavioral type distributions, or for arbitrary networks. The full-range proof is the parity-bijection and tensor characteristic-polynomial argument in RESULT.md. Independent audit is not performed.
