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

# Verification of mathematical identities

The package's `verify.py` (Python with SymPy) was executed. Output:

```
VERIFY_OK: three universal integer polynomial identities
VERIFY_OK: eight distinct boundary permutations and invariant J
```

The checks use symbolic identities over \(\mathbb Z\), so the defining coordinate equalities remain true upon reduction to any characteristic. The boundary permutation computation verifies that the **visible subgroup** has eight elements, not that it is the entire automorphism group. Completeness rests on the independent projective-extension and cyclic-four-torsion argument in `RESULT.md` and on the classical classification of origin-fixed automorphisms of elliptic curves, including exceptional characteristics two and three. The Laurent-invariant-ring proof is algebraic and independent of finite tests. No machine formalization or independent mathematical audit has been performed.
