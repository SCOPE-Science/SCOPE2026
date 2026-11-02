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

# Reproducible checks and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses unbounded integers, exact rational fractions, and complete enumeration of distinct-divisor subset sums. It generates the eight base divisors from their factorizations, verifies that each bit in the closed central interval is set, cross-checks the two key examples with a separate Boolean recursion, checks the sharp excluded integer \(22\) for \(7425\), and evaluates the rational boundary inequalities. It additionally checks five larger cases as consistency tests.

The bitset update `bits |= bits << divisor` is exhaustive because every subset either contains that divisor or omits it, and every divisor appears once. The analytic proof of all cases beyond the eight bases is in `RESULT.md`, not delegated to experimentation. No independent audit or formal machine proof has been performed.

Expected output:

`VERIFY_OK primitive_bases=8 maximum_base=570375 sharp_first_missing=22 sharp_base=7425 uniform_interval_start=23 base_divisor_counts=16,18,18,24,36,40,45,48 minimum_abundance=26 independent_boolean_bases=2 extensions=5`
