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

# Verification procedure

The result is a complete finite enumeration, not an inference from a sample. Both source files are standalone and require no external data. In a directory containing them, run:

```sh
python3 verify_direct.py
c++ -std=c++17 -O2 verify_correlations.cpp -o verify_correlations
./verify_correlations
```

The Python program computes each histogram entry by direct per-window symbol summation and asserts the exact count distribution. The C++ program computes prefix sums and all endpoint differences independently, storing signatures as exact `std::vector<int>` keys in ordered maps, and asserts the same counts. The programs enumerate each of the 16,384 input words, not merely representative orbits. Their twelve four-word equivalence-class lists were compared exactly, and agree with `ambiguous_classes.json`.

Expected histogram: `1:128, 2:8104, 4:12`; total 8,244 distinct signatures and 16,384 input words. Every signature is a complete count vector indexed by substring length and number of ones, so equality tests account for every Parikh vector with multiplicity. Reversal preservation is a mathematical consequence of this observation; palindromic singleton characterization follows from the exhaustive counts.

This reproducibility record does not assert independent external validation or a result for other lengths, alphabet sizes, or incomplete/noisy observations. Literature priority remains subject to the access caveats in `REVIEW.md` and `RESULT.md`.
