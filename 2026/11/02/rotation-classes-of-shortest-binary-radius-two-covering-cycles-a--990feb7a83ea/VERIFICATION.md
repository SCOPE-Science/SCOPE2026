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

# Reproducibility and verification scope

The complete finite checks are in `enumerate.cpp` (Hamming-ball bitset unions) and `crosscheck.cpp` (direct target-by-target Hamming comparisons). Both programs enumerate every indexed binary string for each tested length, including all lengths below the optimum. They use no third-party software libraries. The exact 44 per-length rows are in `checks.csv`, and the full list of minimum-cycle representatives is `orbits.csv`.

The mathematical proof identifies the exact finite domain with an integer interval and proves that the tested predicate is equivalent to covering. The two exhaustive algorithms gave the same counts and orbit classes on execution. Observed program output is supported by source-level exhaustive enumeration, not treated as a standalone impossibility certificate.

The only claimed cases are orders seven through nine with radius two; no all-order extrapolation is made. The minimum lengths were known previously. The new result is the orbit classification; its historical priority is not independently certified.
