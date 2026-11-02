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

The standalone `verify.py` uses standard-library finite-field operations and direct six-term determinant expansion. Run it with `python3 verify.py`; it requires no additional data or third-party packages. It exhaustively checks every diagonal and every possible off-diagonal triple over the prime fields of orders \(3,5,7,11\), then independently checks eight specified diagonals over the quadratic-extension field \(\mathbb F_9\).

Observed execution output:

```
VERIFY_OK prime_fields=3,5,7,11 extension_field=9 determinant_fibers=17820 independent_matrices=1911396 singular_and_nonzero_cases=yes
```

The finite checker and proof employ different approaches: six-term determinant enumeration versus quadratic-form counting. Exhaustiveness refers only to the explicitly named finite fields and diagonals. The proof, not the enumerations, establishes the theorem for every odd prime power. No independent mathematical audit was performed.
