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

Run `python3 verify.py` from the same directory. Only the Python standard library is needed. It recomputes \(H_n=\sum_{k=0}^n\binom nk^4\) exactly, propagates seven rational initial pairs to index 96, checks the determinant propagation at every step, and evaluates both numerator and denominator \(p\)-valuations for the 22 primes from five through 89. The prime-local obstruction is also tested against the actual rational solution with initial values \((0,1)\).

Expected terminal lines:

```
VERIFY_OK recurrence_depth=96 initial_pairs=7 Wronskian_checks=672
PRIME_OBSTRUCTIONS_OK primes=22 largest_prime=89
```

Finite numerical checks are corroboration. The general statement for all \(n\ge0\) and every prime \(p\ge5\) depends on the exact determinant identity and the two distinct roots modulo \(p\), both proved in `RESULT.md`. Independent external mathematical validation has not been performed.
