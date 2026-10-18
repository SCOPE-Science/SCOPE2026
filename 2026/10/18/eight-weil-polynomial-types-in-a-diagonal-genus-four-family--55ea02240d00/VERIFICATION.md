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

The self-review uses `src/verify.py` with `data/expected.json`. The finite-field algorithm separately counts every affine cube-root fiber and all points over infinity; its arithmetical implementation is separate from the character-polynomial derivation. It checks all eighteen diagonal types over \(\mathbf F_{25}\), \(\mathbf F_{121}\), \(\mathbf F_{289}\), and the second extension \(\mathbf F_{625}\), with exact integer assertions.

The general proof is symbolic: the separable Fermat sextic quotient from a maximal Hermitian curve forces scalar Frobenius, and diagonal descent acts through eight explicitly computed tame characters. This proves all degree-eight zeta numerators. Finite test cases alone would not suffice for the uniform theorem. The literature priority comparison retains the risk of standard diagonal Jacobi-sum formulas and incompletely inspected final journal text.
