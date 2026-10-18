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

Execute the three bundled Python 3 source files in the same directory:

```
python3 verify_complex.py
python3 verify_characters.py
python3 verify_matrix_char.py
```

`verify_complex.py` enumerates 3,462 augmented faces, checks cardinality counts and the seven exact binary boundary ranks, and verifies rational homology via the characteristic-zero rank bound and Euler characteristic. `verify_characters.py` enumerates the 168 Fano point collineations and polarity, computes all 336 signed simplex Lefschetz numbers, checks the 24 perfect matchings and eight edge one-factorizations, and verifies the orthogonality and norm identities for the 1+7+8 representation. `verify_matrix_char.py` independently enumerates all invertible three-by-three binary matrices, builds their contragredient line actions and polarity, and reproduces the complete character table with a different face enumerator and edge ordering.

All three programs were run successfully from the exact included source files before this report. They prove finite exhaustive integer identities, not infinite generalizations. The rational representation theorem then follows from the ordinary Hopf trace formula, Maschke semisimplicity, character orthogonality, and rational transfer. These checks are not an independent audit, and no external certification is claimed.
