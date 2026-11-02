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

From the directory containing these files, run `python3 VERIFY.py` using Python 3 and no additional packages. It enumerates every word with exactly three one-positions for lengths \(3\) through \(80\), computes the complete two-symbol nonadjacent read deck from a running eligible-prefix count, derives linear run numbers independently, and compares each run-type support with the exact table in `RESULT.md`. It also independently counts literal eligible coordinate pairs at lengths \(3\) through \(14\). The run completed with `PASS` results, checking 1,663,740 source words and confirming the stated threshold.

The verifier is finite, and therefore cannot prove assertions for all larger word lengths. The actual all-length argument is the run-composition interval proof in `RESULT.md`. The publication-priority comparison remains qualified by potentially unindexed work; an external independent scientific audit has not been performed.
