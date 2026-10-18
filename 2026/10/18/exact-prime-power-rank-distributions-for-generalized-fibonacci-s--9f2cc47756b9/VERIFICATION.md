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

# Reproducible checks and limits

From the directory containing the standalone verification script, run:

```bash
python3 verify.py
```

The program uses only the Python standard library. It calculates the first zero index from the defining second-order recurrence for every parameter in each of 25 odd prime-power rings not exceeding 1300, covering primes 3, 5, 7, 11, 13, 17, 19, 23 and 31. It independently forms the proposed totient distribution, compares exact integer multiplicities, asserts the total number of parameter classes, and checks two explicit small-ring tables. The expected output is `VERIFY_OK rings=25 parameters=4815`.

The mathematical proof is in `RESULT.md`. The executable checks finite instances only; it does not independently establish the infinite assertions, the originality assessment, or independent certification. Independent audit is not performed.
