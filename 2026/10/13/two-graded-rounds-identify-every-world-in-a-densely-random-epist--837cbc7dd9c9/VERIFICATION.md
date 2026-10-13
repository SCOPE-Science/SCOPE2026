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

# Reproducible verification

The accompanying `verify.py` is a single standalone Python 3 script using only the standard library. Run `python3 verify.py` in the directory containing this file. It carries out direct finite row/column-set and row/column-multiset type refinements separately, not merely a call to the histogram sufficient condition. It compares the independent graded-depth-one partition with the explicit degree-triple partition; checks refinement monotonicity; verifies that distinct marked-neighbor degree histograms imply distinct depth-two types; enumerates every binary square matrix of sizes one, two, and three; and evaluates 2,100 seeded random matrices at the declared sample densities \(0.25\), \(0.5\), and \(0.75\).

Direct replay produced:

```
VERIFY_OK exhaustive_binary_square_matrices 530 random_trials 2100 parameter_batches 21
small_exact_depth2_full_counts {1: 2, 2: 8, 3: 144}
density,size (0.25, 20) full_depth2,not_full_depth1,ordinary_two (51, 100, 78)
density,size (0.25, 40) full_depth2,not_full_depth1,ordinary_two (96, 100, 100)
density,size (0.25, 64) full_depth2,not_full_depth1,ordinary_two (100, 100, 100)
density,size (0.25, 96) full_depth2,not_full_depth1,ordinary_two (100, 100, 100)
density,size (0.5, 20) full_depth2,not_full_depth1,ordinary_two (86, 100, 100)
density,size (0.5, 40) full_depth2,not_full_depth1,ordinary_two (99, 100, 100)
density,size (0.5, 64) full_depth2,not_full_depth1,ordinary_two (100, 100, 100)
density,size (0.5, 96) full_depth2,not_full_depth1,ordinary_two (100, 100, 100)
density,size (0.75, 20) full_depth2,not_full_depth1,ordinary_two (39, 100, 93)
density,size (0.75, 40) full_depth2,not_full_depth1,ordinary_two (94, 100, 100)
density,size (0.75, 64) full_depth2,not_full_depth1,ordinary_two (99, 100, 100)
density,size (0.75, 96) full_depth2,not_full_depth1,ordinary_two (100, 100, 100)
```

All finite comparisons passed. Random tests are diagnostics and do not constitute a proof of an asymptotic almost-sure claim. The general theorem uses the exact conditional histogram-difference identity, independent-bin anti-concentration, and concentration estimates established in RESULT.md. No independent mathematical audit was performed.
