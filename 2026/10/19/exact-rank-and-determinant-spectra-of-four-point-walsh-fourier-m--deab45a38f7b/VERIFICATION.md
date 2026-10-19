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

Compile and run `checker.cpp` with `c++ -O2 -std=c++17 checker.cpp -o checker && ./checker`. The program uses integer signs, normalized integer \(3\times3\) minors, and inclusion-exclusion; no numerical tolerances or approximate ranks are used.

Expected output:

```text
N=8 pair_count=4900 ranks=0;84;1344;3472 det0=1428 det8=3136 det16=336 PASS
N=16 pair_count=3312400 ranks=560;104160;1612800;1594880 det0=1717520 det8=1505280 det16=89600 PASS
CHECK_PASS
```

These enumerate all unordered four-row and four-column choices, regarded as ordered row/column pairs, at orders eight and sixteen. The proof for arbitrary \(d\ge3\) uses the exhaustive classification of four vertices in the eight-vertex cube and an algebraic occupancy formula. The finite tests are corroborative rather than a proof for all dimensions.

No external or independent mathematical audit has been performed.
