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

The analytic proof is in `RESULT.md`. Run `python check.py` with Python 3.10+ and SymPy to reconstruct exact rational identities, discriminant, root intervals and stability-coefficient inequalities. This checker uses symbolic rather than floating-point algebra for the stated certificates and separately prints descriptive approximations. Its run passed with `PASS: algebraic reduction, two rational root brackets, derivative signs, exact Jacobian identities, Routh bounds`.

The universal at-most-two bound follows from an explicit quadratic obtained by multiplying the endemic behavioral equilibrium equation by a strictly positive factor. The selected witness has two strictly positive-infection roots in disjoint rational intervals, with one-dimensional root-derivative signs that distinguish the mixed saddle from the mixed sink. Independent proof of full three-dimensional local stability uses strict cubic Routh–Hurwitz inequalities and an exact Jacobian identity. Hyperbolicity implies robustness only in a parameter neighborhood.

The computation does not verify empirical intervention performance or stochastic outcomes, and it does not provide an independent audit of originality, correctness, or value. Bibliographic overlap checks compared mathematical implications, but equivalence in unindexed literature remains possible.
