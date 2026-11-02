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

The standalone `verify.py` uses only Python standard-library integer arithmetic and a fixed random seed. It enumerates exact binomial rows for primes \(2,3,5,7\), exponents \(1\) through \(5\), and row indices \(0\) through \(400\), plus 300 deterministic pseudorandom extra cases below row 2000. It compares actual maximum run lengths with the theorem, confirms both endpoint runs, and checks every possible forbidden window in those rows. A separate base-\(p\) subtraction counter checks the digitwise witness on reduced rows through \(400\) for exponents through \(4\).

From the packaged script, execution with `python3 verify.py` returned:

```
VERIFY_OK exact_rows=8320 forbidden_windows=1221990 digit_cover_certificates=667809
```

These are bounded checks. The universal proof uses Kummer's theorem and a direct constructive covering argument. No independent audit or external mathematical certification has been performed.
