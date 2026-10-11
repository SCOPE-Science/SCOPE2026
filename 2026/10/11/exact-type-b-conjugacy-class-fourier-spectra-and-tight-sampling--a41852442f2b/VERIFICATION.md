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

The standalone checker `artifacts/verify.py` requires Python's standard library only. Run it with `python artifacts/verify.py`. It constructs every signed permutation matrix for ranks \(3,4,5\), groups them by complete signed cycle type, and computes each class-orbit operator on an explicit basis of all matrix directions. Every comparison uses integer or rational arithmetic, with no numerical tolerance. It also tests the stated tightness and injectivity criteria for each signed cycle type.

Actual replay:

```text
n=3: conjugacy_classes=10, tight=0, injective=0, all_9_basis_vectors=PASS
n=4: conjugacy_classes=20, tight=4, injective=4, all_16_basis_vectors=PASS
n=5: conjugacy_classes=36, tight=6, injective=10, all_25_basis_vectors=PASS
VERIFY_OK conjugacy_classes=66 exact_full_class_orbit_operators=PASS coefficient_orthogonality=PASS
```

The computation is exhaustive over these three ranks but cannot establish the theorem for unbounded ranks. The general argument in `RESULT.md` uses Schur orthogonality, a four-summand multiplicity-free conjugation representation, and exact signed cycle identities. An external audit has not been performed.
