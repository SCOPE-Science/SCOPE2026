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

# Exact arithmetic verification

From the directory containing the standalone package, execute:

```sh
python3 checkers/verify.py
```

Observed output:

```text
VERIFY_OK checked_prime_pairs=14028positive_pairs=94notable=[(7, 11), (11, 29), (17, 19), (37, 41), (151, 199)]exact_arithmetic=yes
```

The script uses only Python's standard library. It sieves primes up to 6000, takes each pair of distinct primes greater than five at an even separation from 2 through 140, directly evaluates the sum remainder using modular Fibonacci fast doubling at the full semiprime modulus, and separately predicts both local remainders using only the fixed gap and quadratic characters. Exact equality and the gap-2/4 theorem are asserted for all 14,028 tested pairs. A finite search is not a proof for unbounded primes or differences; the unrestricted field-theoretic argument is in RESULT.md.
