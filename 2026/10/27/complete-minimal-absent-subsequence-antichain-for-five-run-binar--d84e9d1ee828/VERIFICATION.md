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

# Verification of the five-run minimal-absent-subsequence classification

The proof in `RESULT.md` covers **all** positive run lengths by a complete run-count case split and exact feasibility tests. The standalone standard-library script `verify.py` is a separate finite cross-check, not a substitute for that argument. To run it, use `python verify.py` from the extracted package directory.

The code enumerates the entire set of scattered subsequences of each input word using a direct dynamic closure. It obtains actual minimal absent subsequences as absent one-character right extensions of existing subsequences with all single-letter deletions present. This constructs the entire minimal antichain, not only templates whose presence was presupposed.

Checks completed: exact complete-set comparisons for all \(5^5=3125\) parameter tuples with \(1\le a,b,c,d,e\le5\); a further 79 reproducible seeded larger parameter tuples of manageable total size; exact formula/cardinality and full fixed-length histograms for every \(n=5,6,\ldots,30\), including the full positive-composition count \(\binom{n-1}{4}\). Actual output:

`VERIFY_OK complete_subsequence_frontiers=3125 random_large=79 exact_length_histograms=26`

This independently implemented finite enumeration does not certify cases beyond its finite input ranges, mathematical priority, or the conclusions of an external auditor. The universal result relies on the complete proof, and the external independent audit remains unperformed.
