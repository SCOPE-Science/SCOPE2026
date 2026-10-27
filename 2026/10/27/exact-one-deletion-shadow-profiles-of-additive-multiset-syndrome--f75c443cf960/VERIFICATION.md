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

# Reproducible checks and proof boundaries

Execute `python3 support_spectrum_check.py` with Python 3 and only its standard library. The included `support_spectrum_check.out` records its actual output. The script directly enumerates all weak compositions in 100 group/length instances, recomputes the syndrome and the number of positive coordinates, and derives the claimed polynomial independently by Möbius sums without floating-point roots of unity. It also constructs and deduplicates one-symbol transfer neighbors in 15 group/length settings.

The observed success messages are `ADDITIVE_MULTISET_SUPPORT_OK 100 parameter settings 27824 enumerated codewords` and `CROSS_SYNDROME_TRANSFER_OK 15 parameter settings`. The computation checks all residue classes for each tested configuration; it does not enumerate all finite abelian groups or all lengths. The general result rests on finite-group character orthogonality and the explicitly reconstructed generating-function calculation in `RESULT.md`. The checked objects are the *one-sided deletion shadows* of fixed-length multiset compositions; same-length metric balls are not substituted for them.

The output file is included as observed experimental evidence only. No independent audit or external mathematical certification has been undertaken.
