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

**Theorem scope:** all indexed words over the fixed binary alphabet, for every positive length. The proof supplies the infinite-range argument; the checks below test its interpretations and intermediate formulas on finite instances only.

**Actual executable check:** `python verify.py` using Python 3 standard library. The program independently evaluates the greedy two-letter arch count at all cuts for every binary word of each length from \(1\) through \(18\), totaling \(2^1+\cdots+2^{18}=524286\) source words. It independently builds the full scattered-subsequence set for each rotation through length \(9\). It then tests the precise number of harmful cuts, cyclic transition-run characterization, all binomial coefficient counts, the two-state trace recurrence, and the Lucas totals. Observed terminal marker:

`VERIFY_OK exhaustive_binary_words= 524286 explicit_subsequences_n=1..9 distribution_n=1..18 weighted_transfer_trace_n=1..18 bad_cut_positions=checked`

**Limits:** finite checks do not establish the result for all lengths, independently certify novelty, or replace the mathematical proof. Integer arithmetic is exact, and the executable uses no external data or modules. Independent scientific validation has not been performed.
