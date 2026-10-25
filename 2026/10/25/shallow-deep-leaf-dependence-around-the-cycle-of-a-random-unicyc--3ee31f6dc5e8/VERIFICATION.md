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

# Reproducible checks

Run `python unicyclic_leaf_verify.py` with Python 3 and its standard library. The program uses exact integer and rational arithmetic, enumerates specified-root forests and, independently, connected simple graphs with exactly one cycle, and compares their mixed factorial moments with the claimed closed expression.

Recorded output:

```
PASS 203 rooted-forest exact mixed moments over 223729 forests;
PASS 70 independent graph exact mixed moments over 72193 unicyclic graphs; all covariance signs
```

The algebraic forest-count bijection, covariance inequality, and asymptotic expansion in `RESULT.md` are required for all parameter sizes; enumerations cover only the finite ranges printed in the verification. No independent scientific audit has been performed.
