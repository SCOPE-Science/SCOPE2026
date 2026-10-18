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

# Reproducibility and limits
Extract all entries of the finding into one directory preserving relative paths and run `python3 artifacts/verify.py` there, using a standard Python 3 interpreter without external packages. The program tests the capped-count spectrum through grade ten, direct bounded-profile reduction, the explicit symmetric-chain decomposition and preservation of every upset for up to four letters, and randomly generated nested graded-modal truth conditions across representative finite stars.

Expected terminal output ends with `POSITIVE_GRADED_STAR_CLASSIFICATION_OK`; the run performed during preparation printed 10 spectrum checks, `SPERNER_WIDTH_SHARP_COMPRESSION_OK 27860`, `SHARP_CORE_UPPER_BOUND_OK 15235`, `SHARP_CORE_LOWER_BOUND_OK 100`, and `NESTED_POSITIVE_GRADED_EQUIVALENCE_OK 600000`. The checker verifies finite instances and is not an exhaustive machine proof of the unbounded mathematical result. The infinite-parameter statements rely on the independent mathematical argument in `RESULT.md`. This verification is author-side reproducibility; independent scientific audit has not been performed.
