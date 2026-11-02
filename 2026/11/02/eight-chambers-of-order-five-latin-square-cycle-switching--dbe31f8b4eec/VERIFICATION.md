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

The two fully standalone C++17 programs `verify.cpp` and `verify_alt.cpp` were compiled with `g++ -O3 -std=c++17` and executed against the complete order-five Latin-square space. The first enumerates all candidate cell subsets directly and rejects decomposable five-position swaps; the second independently computes relative derangement cycles. Both obtain exactly 161280 squares and edge counts 288000, 576000, 1036800 for lengths 2, 3 and 5, respectively, with component sizes {1:17280,72000:2} for lengths {2,3} and {2880:6,72000:2} for lengths {2,3,5}. Intercalate counts 0:17280 and 4:144000 were checked.

Each generator explicitly normalizes the first row, enumerates all 1344 completions, restores all 120 symbol images, verifies uniqueness and legal moves, and tests union-find component sizes. This is an exhaustive finite certificate, not a general theorem for orders other than five. None of the included programs verifies historical priority or constitutes independent scholarly assessment.
