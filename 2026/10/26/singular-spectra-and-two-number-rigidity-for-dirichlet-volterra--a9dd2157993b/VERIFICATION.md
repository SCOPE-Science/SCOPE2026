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

# Reproducibility

Run `python3 verify.py` from the package directory using Python 3 standard library. The script constructs the two original monomial Volterra operators on finitely supported Dirichlet coefficient vectors, composes them in both orders and compares their difference with the proposed formula; it also iterates commutator powers, checks strictly decreasing finite singular coefficients, checks the exact power-norm expression, and numerically reconstructs both monomial logarithms from the first two singular values. On preparation it passed 5,370 deterministic finite assertions.

The infinite-dimensional correctness rests on exact basis calculations, injective support maps, strict scalar monotonicity and asymptotic estimates in RESULT.md. Finite tests cannot prove membership or nonmembership in infinite Schatten ideals, spectral quasinilpotence or global inverse uniqueness; these are proved analytically. No external audit or human validation has been performed.
