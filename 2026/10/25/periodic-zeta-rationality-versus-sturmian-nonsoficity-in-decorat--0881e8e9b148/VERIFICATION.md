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

# Reproducible computational checks

Execute `python3 verify.py` using Python 3 standard library. This prints four tables of exact fixed-point counts for periods \(1\) through \(10\), followed by `ALL_40_COUNTS_EXACT`. The Sturmian mechanical word uses 70-digit Decimal precision. The code computes all allowed factors up to period ten, enumerates all ternary periodic words independently, checks adjacent-marker gaps and allowed intervening factors, then compares the resulting counts with the exact generating-series recurrence. The four tested supports are all nonnegative gaps, even gaps, zero together with powers of two, and a sparse support in the first ten gap lengths. For these finite periods only the intersection with gap lengths below ten matters; the supports may be extended arbitrarily at larger lengths, including to infinite sets.

Observed result: all 40 equalities passed. For all nonnegative gaps, period-\(1\) through period-\(10\) counts are \((1,5,16,45,121,320,841,2205,5776,15125)\). These are exhaustive computational checks in the tested finite ranges, **not** a proof of the count formula for all periods or of the analytic and nonsofic conclusions. Those statements depend on the marker-count argument, aperiodicity of Sturmian systems, Skolem–Mahler–Lech, and Pólya–Carlson, all explicitly explained in RESULT.md.

# Limits of verification

No independent audit or formal proof checker is asserted. The chosen finite test cases do not certify an infinite combinatorial identity, and no automated procedure here checks historical priority or the hypotheses of the two classical analytic/arithmetic theorems beyond the supplied written proof.
