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

Run `python3 verify.py` from the extracted package directory with a standard Python 3 interpreter. The checker independently enumerates all simple bipartite graphs in 90 fixed-edge size/count strata; independently sums exactly weighted Bernoulli graphs for 12 triples and all ordered replacement sequences for 16 settings; and compares a six-point sparse-limit diagnostic. The finite comparisons use exact fractions; only the asymptotic diagnostic uses floating-point functions. The proof's general all-parameter sign and asymptotic limit require the identities in `RESULT.md`, not finite experimentation.

Expected successful output consists of `FIXED_EXHAUSTIVE_PASS`, `BERNOULLI_EXHAUSTIVE_PASS`, `REPLACEMENT_EXHAUSTIVE_PASS`, `SPARSE_LIMIT_DIAGNOSTIC_PASS`, and `VERIFY_OK`. This is computational cross-checking, not independent scientific validation.
