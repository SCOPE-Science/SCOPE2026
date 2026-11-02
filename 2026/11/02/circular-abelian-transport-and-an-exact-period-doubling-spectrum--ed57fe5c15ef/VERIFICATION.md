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

`checker.py` is a standalone Python 3 script requiring only the standard library. Running it directly checks each exact minimum/maximum recurrence, the summed transport identity and the period-doubling closed form against direct circular-window counts for every binary input of lengths 1–8 and for complete period-doubling spectra at ranks 0–11.

Observed output:

```
PASS: 510 exhaustive binary input words; 12 complete period-doubling spectra
```

The finite checks are not an exhaustive proof over arbitrary inputs or unbounded ranks. The proof for all cases is given in `RESULT.md` and does not depend on code execution. No independent audit has been performed.
