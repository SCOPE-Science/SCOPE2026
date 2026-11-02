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

# Verification and reproducibility

Execute `python3 verify_gap_universality.py` with Python 3.9 or later; only the standard library is required. The script explores all balanced host words in seven complete finite parameter families and tests every length-\(k\) target against **all embeddings**, computing the exact minimized maximum jump, not merely one greedy witness. For universal hosts it compares the literal answer against the consecutive permutation-block displacement formula; for all balanced hosts it checks universality versus block decomposition. It tests exact radius frequencies, all cumulative bounds, and the restricted-permutation factor directly.

Completed replay:

```
PASS bounded_drop_counts=27 q=2..7
PASS q=2 k=2 balanced_hosts=6 universal_hosts=4 pattern_checks=21 radius_spectrum={2: 2, 3: 2}
PASS q=2 k=3 balanced_hosts=20 universal_hosts=8 pattern_checks=107 radius_spectrum={2: 2, 3: 6}
PASS q=2 k=4 balanced_hosts=70 universal_hosts=16 pattern_checks=532 radius_spectrum={2: 2, 3: 14}
PASS q=2 k=5 balanced_hosts=252 universal_hosts=32 pattern_checks=2614 radius_spectrum={2: 2, 3: 30}
PASS q=3 k=2 balanced_hosts=90 universal_hosts=36 pattern_checks=549 radius_spectrum={3: 6, 4: 18, 5: 12}
PASS q=3 k=3 balanced_hosts=1680 universal_hosts=216 pattern_checks=16244 radius_spectrum={3: 6, 4: 90, 5: 120}
PASS q=4 k=2 balanced_hosts=2520 universal_hosts=576 pattern_checks=20834 radius_spectrum={4: 24, 5: 168, 6: 240, 7: 144}
VERIFY_OK parameter_cases=7 balanced_hosts=4638 universal_hosts=888 exact_pattern_checks=40901
```

The finite experiments are not extrapolated to infinite parameter ranges. The full proof of the all-parameter formulas is in RESULT.md. No external formal certification or independent audit is claimed.
