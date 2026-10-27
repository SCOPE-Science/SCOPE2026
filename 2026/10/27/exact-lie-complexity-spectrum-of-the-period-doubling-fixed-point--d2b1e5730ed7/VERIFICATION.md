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

# Reproducible finite checks

Run `python3 verify_period_doubling_lie.py` with any current Python 3 implementation. The script uses only standard-library Python. It generates a length-\(2^{14}\) prefix of the period-doubling fixed point and an extension of length \(2^{15}\), checks factor sets agree in these two samples for all \(1\le n\le192\), enumerates full cyclic orbits, and checks the exact 0-or-2 length spectrum. It separately checks the two-phase factor decomposition and conjugacy-class bijection at all 96 even lengths through 192.

Expected final output:

```
PERIOD_DOUBLING_LIE_PASS n=1..192 exact=2 iff odd_part_in={1,3} substitution_factor_and_orbit_bijections=96
```

These finite comparisons do **not** prove that the finite prefix contains all possible factors, nor that the formula persists after length 192. The self-contained mathematical proof in RESULT.md covers the infinite theorem through the parity exclusion, exact factor identity, bijection, and base cases. Independent audit has not been performed.
