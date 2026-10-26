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

# Verification
The pure-Python `verify.py` checks Fibonacci word totals, all exact one-ended prefix counts for lengths through 13 with test prefixes through 6, exact two-ended counts against powers of the binary adjacency matrix, and constructive integer-cylinder representations for sampled algebraic integers. Expected output on a normal Python 3 interpreter:

```
GOLDEN_FO_EXACT_OK 721 19
```

Finite enumeration is confirmatory only. The infinite logical assertion uses effective bounded-degree Hanf locality and a uniform exponentially small failure probability for each fixed interior factor. The arithmetic realization uses exact conjugate eigenvalues and integrality; no floating-point check is used to prove it. The checker uses floating point only in exploratory finite tests of existence and approximate evaluation of algebraic identities. No independent scientific audit has been performed.
