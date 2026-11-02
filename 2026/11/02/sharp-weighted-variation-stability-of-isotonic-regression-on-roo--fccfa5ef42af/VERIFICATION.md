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
# Verification and limits

Run `python3 check_star_isotonic.py` in the directory containing the accompanying source. This stand-alone standard-library script uses rational arithmetic and seeded reproducible tests; it does not download data or call outside services. Its expected terminal marker is `CHECKS_OK` and expected total is **224239**. The checks cover the independent pooled-projection oracle, exact face-column upper bound, exact two-input inequality for sampled input pairs, equality witnesses for every column and for the identity branch, and uniform / matched-mass specializations.

These finite tests are diagnostic and do not imply exhaustive coverage of arbitrary dimensions or continuously varying weights. The analytical proof in RESULT.md establishes the all-dimensional and all-positive-real-weight statement. The self-review is passed; independent audit has not been performed. Neither a Lean certificate nor an independent validation is claimed.
