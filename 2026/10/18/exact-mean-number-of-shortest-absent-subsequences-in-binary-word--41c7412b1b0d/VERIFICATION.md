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
# Verification of the expected shortest-absence formula

The standalone `verify.py` requires Python 3 only and uses exact integer/fraction arithmetic. It independently enumerates every binary word through length \(14\) and directly tries target strings in increasing target length. It checks \(s(w)\) against all absent strings at the greedy-arch minimal length, totals against the cubic recurrence, and exact full three-state and reduced two-state weighted coefficient arrays for lengths through \(100\).

Execution: `python3 verify.py`.

Observed output:
```
ALL_CHECKS_PASS direct_all_words_n=0..14 recurrence_n=0..100 three_state_n=0..100 safe_paths_n=0..100
TOTALS_n_0_to_15 [2, 2, 8, 12, 34, 62, 152, 304, 698, 1458, 3248, 6924, 15210, 32734, 71440, 154432]
```

The identity is proved for all lengths by the exhaustive transition partition, monotone-surplus argument, and renewal-generating-function calculation in RESULT.md. Finite checks provide supplementary error detection; they do not certify the infinite statement. No independent audit has been performed.
