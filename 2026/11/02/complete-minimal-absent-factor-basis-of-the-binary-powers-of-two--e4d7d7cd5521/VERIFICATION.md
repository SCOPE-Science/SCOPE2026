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

The self-contained `checker.py` enumerates every factor up to length 160 in a prefix of length 8192 and compares every minimal absent factor computed from the factor language to the four families in the theorem. Its output was:

```
PASS: exhaustive factor-language comparison through length 160; 166 minimal-absent-word instances across lengths 2..160.
Counts n=2..16: [0, 1, 5, 0, 1, 3, 1, 0, 1, 1, 1, 3, 1, 1, 1]
```

Reproduce with `python3 checker.py`. Direct enumeration is limited to those lengths and that prefix; the all-length assertion follows from unique adjacent-one gaps, the middle-factor argument and exact boundary overhangs. The original 2002 article's complete text was not available for historical comparison. Independent audit has not been performed.
