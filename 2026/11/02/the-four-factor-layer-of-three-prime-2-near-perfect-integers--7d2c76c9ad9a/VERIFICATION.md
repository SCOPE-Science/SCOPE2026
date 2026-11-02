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

# Reproducibility and limits

Use `python3 verify.py` from this directory. No third-party dependencies, database, or network connection are needed. The checker reconstructs divisor sets with exact integer arithmetic and compares every unordered pair of *distinct* divisors against the exact deficit \(\sigma(n)-2n\). It enumerates only the prime pairs left by the explicit mathematical inequalities in `RESULT.md`.

A completed check produced:

```text
VERIFY_OK unique_examples=10 finite_4pq=32 finite_2p2q=6 finite_2pq2=4 p3_candidate_q=(5, 7, 11) sum_odd_bound=624/315
```

It also reconstructs the algebraic candidate set for \(2\cdot3^2q\) by solving the linear divisor equations, checks the strict odd-case inequality exactly, and requires precisely one omitted pair for each of the ten accepted examples. The exact finite candidate counts are 32, 6 and 4, for 42 integer instances total.

These tests do not establish universal statements by extrapolation. The proof of completeness is conditional on the elementary global inequalities and divisor-form reductions in the accompanying `RESULT.md`, which must be assessed mathematically. No claims are made about larger prime-multiplicity layers, and no independent external mathematical validation has been performed.
