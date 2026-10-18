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

The checker `check_monogenic.py` exhaustively enumerates each map and literal generated submonoid in degrees one through six, independently of its rational formal-series computation of the period-height count. The checker compares the full parameter profile and verifies that each generated submonoid has exactly the predicted generator fiber. It prints `CHECKER_OK` on success.

The checker `verify_partition.py` separately sums permutation cycle types to evaluate the integer exact-count formula through degree eighteen, with rational weights and divisibility checks. It prints `PARTITION_CHECK_OK` on success.

The infinite-degree statement relies on the written generator-fiber proof and labeled functional-digraph decomposition; finite scripts are cross-checks only. The sharp asymptotic additionally requires the unique dominant simple pole of the height-one mapping series and an entire-function bound for mappings with a fixed bounded set of possible periods. No external infinite certificate or independent audit has been performed.
