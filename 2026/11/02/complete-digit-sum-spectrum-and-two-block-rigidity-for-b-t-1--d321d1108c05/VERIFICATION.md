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

The supplied `verify.py` executes using Python 3 and only the standard library.

Observed output from an exact-arithmetic execution:

```
VERIFY_OK constructive_cases=1728 lower_bound_instances=25200 exact_short_length_cases=16 arithmetic=exact
```

The constructive checks range over bases 2–13, exponents 1–8, residue indices and four separated-block counts. The exhaustive short-length checks enumerate all positive multiples strictly below the two-block boundary for 16 specified parameter pairs. All arithmetic uses arbitrary-precision integers.

These are finite checks and are not an infinite proof. The unrestricted mathematical argument is the digit-sum nonincreasing modular folding, explicit separated-block construction, and exhaustive two-block remainder partition given in `RESULT.md`.

Independent mathematical audit has not been performed.
