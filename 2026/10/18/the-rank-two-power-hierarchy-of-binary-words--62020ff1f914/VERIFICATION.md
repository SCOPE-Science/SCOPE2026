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

# Verification protocol

Run `python3 verify.py` in the extracted package directory (Python 3 standard library). It checks the exact closure of the two-sided context-state transition, counts the complete 37-state automaton and its 32 two-letter states, verifies all 30 square signatures and 16 cube signatures, tests power stabilization on each representative, and validates a canonical complete transition certificate. The general stabilization proof for every exponent at least three is symbolic and appears in `RESULT.md`.

The program independently enumerates all literal roots through the proved sharp length bounds, verifies both minimum-length histograms, and implements the two-round Ehrenfeucht--Fraisse game for pairwise distinct output signatures. The state-closure argument, not this finite literal enumeration, proves global completeness. Successful local execution printed:

```text
VERIFY_OK states=37 mixed=32 word_types=90 square_types=30 cube_types=16
SQUARE_MIN_ROOT_HIST={2:2,3:6,4:10,5:10,6:2}
CUBE_MIN_ROOT_HIST={2:2,3:6,4:6,5:2}
POWER_STABILIZATION=3 SHARP_WITNESS=01
```

The empirical verification is specific to the included code and certificate. No independent audit or general automated proof beyond the stated mathematical recurrence is asserted.
