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

# Verification of aggregate cyclic two-gram profiles

Execute `python3 VERIFY.py` using Python 3 and the standard library. The script enumerates literal circular binary words, constructs their exact two-gram count tuples, and checks them against the interval characterization. Its coverage is all 64 ordered pairs of lengths \(2\) through \(9\), 64 triples of lengths \(2\) through \(5\), and 81 quadruples of lengths \(2\) through \(4\). It checks the symbolic two-strand formula and the all-length obstruction template for \(2\le r\le12\).

Actual local execution result:

```
VERIFY_OK two_length_pairs=64 triple_length_tuples=64 quadruple_length_tuples=81 sharpness_k=2..12
```

The independent-audit channel remains **not performed**. This program is a finite mathematical cross-check, not an independent audit or exhaustive test of unbounded lengths. The general result is proved in `RESULT.md`.
