---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The checker `check_monogenic.py` exhaustively enumerates each map and literal generated submonoid in degrees one through six, independently of its rational formal-series computation of the period-height count. It compares the full parameter profile and the aggregate transformation-to-submonoid count ratios in each height/period class. It prints `CHECKER_OK` on success.

The checker `verify_partition.py` separately sums permutation cycle types to evaluate the integer exact-count formula through degree eighteen, with rational weights and divisibility checks. It prints `PARTITION_CHECK_OK` on success.

The finite scripts check counts used as inputs to the argument; they do not certify a sharp asymptotic. The proof of that asymptotic in `RESULT.md` uses the generator multiplicity, the unique dominant pole of the shallow mapping series, and an entire-function bound for maps with a fixed bounded set of possible periods.
