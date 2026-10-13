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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and its standard library. The file enumerates the entire space of the pertinent endomorphism matrices, scalar center actions, and linear functionals for Heisenberg Lie algebras with parameter pairs `(m,q)=(1,2),(1,3),(1,4),(2,2)`, directly checks the derivation identity and idempotence, computes their linear ranks, and compares the resulting distributions with the theorem. It constructs the field of four elements explicitly. Additionally, it constructs and acts with every relevant automorphism in the dimension-three instances over the fields with 2 and 3 elements, and checks the predicted automorphism orbits.

Recorded output from the packaged program:
```
H_3(F_2): rank_counts={0: 1, 2: 16}; central_multiplier_matrix_counts={0: 2, 1: 6}; total=17
H_3(F_3): rank_counts={0: 1, 2: 36}; central_multiplier_matrix_counts={0: 1, 1: 12}; total=37
H_3(F_4): rank_counts={0: 1, 2: 96}; central_multiplier_matrix_counts={0: 2, 1: 20}; total=97
H_5(F_2): rank_counts={0: 1, 2: 80, 3: 480, 4: 16}; central_multiplier_matrix_counts={0: 22, 1: 120}; total=577
VERIFY_OK
H_3(F_2) automorphism-orbit sizes: [1, 12, 4]
H_3(F_3) automorphism-orbit sizes: [1, 36]
ORBIT_OK
```

These finite checks are exhaustive only in the stated cases; they do not constitute proof over unbounded dimensions, arbitrary fields, or other extension degrees. The general results follow instead from the written symplectic linear-algebra argument. Literature comparisons have a residual risk of equivalences under alternate terminology. No independent mathematical audit has been performed.
