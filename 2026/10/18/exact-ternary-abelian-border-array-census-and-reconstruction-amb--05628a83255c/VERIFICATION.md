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

The two included complete C++17 programs independently produce the complete census and the length-sixteen inverse-fiber histogram. A reproducible build from this directory is:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_canonical.cpp -o canonical
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_labeled.cpp -o labeled
./canonical canonical_table.csv canonical_hist.csv
./labeled labeled_table.csv labeled_hist.csv
cmp canonical_table.csv labeled_table.csv
cmp canonical_hist.csv labeled_hist.csv
cmp canonical_table.csv census_table.csv
cmp canonical_hist.csv ambiguity_histogram_n16.csv
```

These compilation and comparison steps were executed successfully against the actual included source files. Both programs recompute every possible word type needed for the specified length range, rather than sampling. The canonical program processes exactly \(7{,}174{,}454\) restricted-growth words at length sixteen; the independent labeled program processes \(14{,}348{,}907\) words with first symbol zero. The full CSV files matched byte-for-byte.

Checks of `ambiguity_histogram_n16.csv` yielded \(353\) positive frequency levels, total array count \(1{,}151{,}825\), total canonical-generator count \(7{,}174{,}454\), exactly \(468{,}549\) one-generator arrays, and exactly one array with the greatest generator count \(16{,}384\).

The finite enumeration is exhaustive only up to length sixteen. No infinite sequence formula follows from it; the separate maximum-fiber theorem has an elementary all-length proof in `RESULT.md`. Independent external mathematical review has not been performed.
