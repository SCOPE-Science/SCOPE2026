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

# Verification record

The complete proof appears in `RESULT.md` and the independently executable tests in `verify.py`. The tests were run with Python 3; the output was:

```
gap necklaces n=6..80: all thresholds and boundary fiber classes agree
independent marked-word census n=6..17: all boundary cases agree
independent word-frequency identities n=6..37: agree
ALL TESTS PASSED
```

Finite checks alone cannot prove the full result. The unbounded proof derives a triple-read criterion, gap-multiset invariance without triple reads, uniqueness at the sharp length, and a complete integer-partition classification of the immediately shorter spectra. The exceptional small finite cases are exhaustively covered by the executable checker. No formal proof assistant or independent human assessment was used.
