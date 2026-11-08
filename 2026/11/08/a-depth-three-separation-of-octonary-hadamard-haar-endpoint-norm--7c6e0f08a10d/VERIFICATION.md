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

Run `python3 verify_octonary.py`. It uses only the Python standard library and exact integer/rational arithmetic, with no external data files.

The completed execution reported:

```
LOCAL_PROFILE_CENSUS_AND_40_EXACT_CORNER_INEQUALITIES_PASSED
EXACT_BELLMAN_INDEPENDENT_RECURSION_CHECKS_PASSED depths=0..4
DEPTH 0 SIGNED_ROW_L1 1 BINARY_3D 1
DEPTH 1 SIGNED_ROW_L1 5/2 BINARY_3D 5/2
DEPTH 2 SIGNED_ROW_L1 73/16 BINARY_3D 73/16
DEPTH 3 SIGNED_ROW_L1 857/128 BINARY_3D 839/128
DEPTH 4 SIGNED_ROW_L1 9049/1024 BINARY_3D 8761/1024
DEPTH 5 SIGNED_ROW_L1 89945/8192 BINARY_3D 86471/8192
DEPTH 6 SIGNED_ROW_L1 859993/65536 BINARY_3D 822841/65536
FULL_DIRECT_KERNEL_WITNESS_CHECKS_PASSED depths=0..6
ALL_OCTONARY_HAAR_DIAGNOSTICS_PASSED
```

The exhaustive 128-sign Walsh calculation plus symbolic four-corner comparison validates the only nontrivial finite local lemma used in the arbitrary-depth proof. The finite-depth Bellman and direct-row tests corroborate but cannot independently establish the infinite induction, which is in `RESULT.md`.

No independent review has been conducted.
