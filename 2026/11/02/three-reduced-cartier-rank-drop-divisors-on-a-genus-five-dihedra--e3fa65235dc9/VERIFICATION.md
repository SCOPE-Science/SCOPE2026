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

Run `python3 verify.py` from this directory (Python standard library only). The script reconstructs the coefficient and Legendre polynomials, computes raw Hasse--Witt matrices and fifth powers for every smooth prime-field parameter for 44 prime characteristics between 5 and 199, checks squarefree factors, and computes the pairwise gcd degrees for characteristics 13 and 19.

Observed output:

```
EXACT_OVERLAPS 13 degrees= [2, 4, 6] pairwise_gcd_degrees= [0, 0, 0]
EXACT_OVERLAPS 19 degrees= [3, 6, 9] pairwise_gcd_degrees= [0, 1, 0]
VERIFY_OK 44 prime characteristics and all smooth prime-field parameters
```

These finite tests are not a proof over all characteristics or all algebraic-closure parameter values. The symbolic proof is in RESULT.md. No independent audit or external validation has been performed.
