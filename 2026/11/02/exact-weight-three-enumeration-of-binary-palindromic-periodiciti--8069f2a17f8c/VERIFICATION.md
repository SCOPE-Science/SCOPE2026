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

# Verification evidence

Execute `python3 verify.py` alongside the six documents. The script uses only standard-library Python and independently applies the defining condition by enumerating all word periods and all palindrome splits of each candidate period. It compares the literal decision to the cyclic-gap theorem for all 7,315 weight-three binary words of lengths 3 through 21, then separately aggregates by direct enumeration at each length. It calculates coefficients of the displayed rational function using an explicit integer polynomial recurrence, and compares them with all ordered positive-gap sums for lengths 3 through 160.

An actual local execution returned:

```
VERIFY_OK direct_word_cases=7315 gap_triples=1330 rational_lengths=158 initial_values=[1, 4, 10, 14, 25, 36, 52, 68, 93, 116, 150, 182, 225, 268, 324]
```

Additional exact symbolic partial-fraction extraction and a twelve-residue coefficient check through length 200 agreed with the stated quasipolynomial. Those checks corroborate, but do not replace, the combinatorial proof. Neither a human audit nor any independent scientific validation is represented here.
