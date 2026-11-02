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

# Verification of the weighted complete-graph maximal bound

The complete proof is in `RESULT.md`; this file records reproducible finite checks. Execute `python verify_weighted_clique_maximal.py` using Python 3 standard library. Recorded output:

```text
EXACT_RATIONAL_2_BY_2_SPECTRAL_IDENTITY_OK 153
KNOWN_COUNTING_MEASURE_FORMULA_OK
EQUALITY_EXTREMIZERS_OK 210
RANDOM_INPUT_SHARP_UPPER_ENVELOPES_OK 12600
EXACT_INTEGER_SUBSET_SUM_REDUCTION_OK 320
ONE_THIRD_MASS_RIGIDITY_OK
ALL_WEIGHTED_CLIQUE_MAXIMAL_CHECKS_OK
```

The 153 rational identities check the eigenmatrix trace, determinant and discriminant exactly. All 210 two-level equality witnesses attain the proposed norm to numerical precision. Random-vector tests provide diagnostics only, not a proof for all functions. The small exhaustive SUBSET SUM reductions verify the encoding in 320 instances, not general NP-hardness; that follows analytically from the reduction in `RESULT.md` and the classical NP-completeness of SUBSET SUM. Neither this verification nor the current review is an independent audit.
