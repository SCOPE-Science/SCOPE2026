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

# Reproducible mathematical checks

Execute `python3 verify.py` in the same directory. This uses only the Python standard library, and it recomputes binary finite-field arithmetic, the separability predicate, all smooth marked coefficient counts, and iterated semilinear Cartier ranks over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\).

Observed (total smooth, supersingular, rank-two) are `(8,4,4)`, `(192,48,144)`, `(3584,448,3136)`, `(61440,3840,57600)`. The program also enumerates two illustrative point counts over the first two fields and prints `VERIFY_OK` upon success. No randomized step is used.

The proof is the symbolic Cartier calculation plus the elliptic quotient argument in `RESULT.md`. These finite computations do not establish all-field algebraic statements and do not separately validate claims of originality or significance. No external independent verification or audit has been performed.
