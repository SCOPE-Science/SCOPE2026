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

# Verification

The package contains independent complete enumerators in `verify.py` and `verify_full.cpp`.

Run from a directory containing those files:

```
python3 verify.py
c++ -O3 -std=c++17 verify_full.cpp -o verify_full
./verify_full
```

Expected success markers:

```
POWER94_CURLING_CANONICAL_VERIFY_OK
POWER94_CURLING_LABELED_VERIFY_OK
```

The Python search uses restricted-growth alphabet normalization and obtains 1728 canonical terminal words at length 84, all using three symbols; its four joint class sizes are 672, 336, 480, 240. The independent C++ search retains all letter labels and obtains exactly 10368 words, with four joint class sizes 4032, 2016, 2880, 1440. Each procedure checks that no valid word can extend to length 85. Both classify every terminal source by exact critical exponent, not sampled words, and both reconstruct the curling symbols using all possible square-suffix periods.

No infinite-word claim, probabilistic inference, or external mathematical certification is asserted. The original paper's independent count of 10368 is a cross-check; the detailed joint distribution is verified by the included programs. Independent mathematical auditing has not been performed.
