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

# Verification

The standalone `verify.py` uses the Python 3 standard library only. Run it from a directory containing the script:

```bash
python3 verify.py
```

Expected terminal output begins `VERIFY_OK`. The script checks the exact first disagreement and encoding-length claims for all indices \(4\le k\le20\); performs 28,632 position comparisons; independently recomputes the last-digit description of the word at 25,000 indices; and checks the finite-word commutation recurrence. The run completed successfully during preparation of this package.

The state-complexity lower bound is **mathematical**, not a computer enumeration: it follows from a four-state validity filter, a two-state unshifted-word output automaton, and the shortest accepted word argument. The external published upper bound is cited rather than rederived. No independent mathematical audit or external validation has occurred.
