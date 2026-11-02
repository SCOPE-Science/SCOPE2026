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

# Reproducible verification

Run `python3 verify.py` with Python 3. The script uses exact integer arithmetic only, independently recomputes the original floor recurrence for inputs at most \(900\), and compares it to the divisor recurrence. Up to \(10000\), it checks the full squarefree formula against independent prime factorizations, the congruence with the classical Möbius function, and the prime indicator equivalence.

Observed output:

```text
VERIFY_OK n_max=10000 original_recurrence=900 squarefree_exact=6082 nonsquarefree_parity=3917 primes=1229 moment_values=[1, 2, 6, 26, 150, 1082] arithmetic=exact
```

The exhaustive finite tests do not establish any claim for integers beyond their checked ranges. The unrestricted assertions are proved algebraically in `RESULT.md`, using the divisor recurrence and a finite nilpotent-algebra coefficient extraction for each fixed squarefree input. Independent audit: not performed.
