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

# Reproduction and verification

Run `python3 verify_llds.py` using Python 3.10 or later; no additional packages or files are required. The executed checker returned:

```
LLDS_MINIMAX_SPECTRUM_PASS qary_source_words_tested=67752 distinct_subsequence_occurrences_tested=207 spectrum_entries_checked=290 generating_coefficients_n=0..80 q=2..5
```

The verifier computes optimal letter-duplicated subsequence lengths by a two-state-per-symbol dynamic program. It compares that optimum with explicit subsets for short words, and enumerates every input word on alphabets of sizes \(2\), \(3\) and \(4\) at tested lengths up to \(13\), \(9\) and \(7\), respectively. It independently checks both first-appearance position and the rational-function recurrence on cyclic prefixes for alphabet sizes \(2\) through \(5\). It also checks formal coefficients through prefix degree \(80\). All-length correctness rests on the proof in `RESULT.md`, not on finite tests. No external or independent audit has been performed.
