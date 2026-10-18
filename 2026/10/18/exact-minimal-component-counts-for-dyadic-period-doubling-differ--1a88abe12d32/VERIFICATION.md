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

The proof uses exact infinite identities for the period-doubling substitution and a finite-fibre dynamical argument. Independent audit has not been performed.

The reproducible auxiliary script `check_dyadic_pd_lifts.py` was executed with Python 3 and produced a PASS after checking 20,106 first-return intervals, with offsets \(2\), \(4\), \(8\), and \(16\), across the admissible cylinder levels through \(n=9\). It compares the substitution recurrence to the valuation formula and computes return translations by direct coordinate sums. This finite check is a sanity test, not a replacement for the all-parameter proof. The new claim begins at \(r=2\).

Mathematical boundary checks: for \(n\ge r+2\), the number of summands in all constant-coordinate sums is even; for the last coordinate, complementing every summand leaves the parity invariant. The block-cocycle calculation works for both possible return lengths. The final component census requires the orbit-closure and fibre-exhaustion arguments in `RESULT.md`; return-group size by itself is insufficient.
