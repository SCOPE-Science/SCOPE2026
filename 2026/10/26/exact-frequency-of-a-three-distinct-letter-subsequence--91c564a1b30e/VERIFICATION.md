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

Reproducibility: run `python verify.py` with Python 3 and the standard library. The script enumerates every word over alphabets of sizes 3 and 4 through length eight, counts literal `012` subsequences by a descending dynamic-programming update, and compares the exact-two counts with coefficients of the displayed rational generating function.

Observed output:

```text
m=3: n=0..8 matched; counts n=4..8: 3, 20, 83, 276, 807
m=4: n=0..8 matched; counts n=4..8: 3, 35, 248, 1382, 6669
VERIFY_OK
```

The finite enumeration checks are not used as an all-length proof. The proof in `RESULT.md` supplies the exhaustive case classification and the neutral-symbol insertion identity. No independent audit or independent validation is represented as performed.
