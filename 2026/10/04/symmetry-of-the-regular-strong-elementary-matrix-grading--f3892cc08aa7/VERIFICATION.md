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

The arbitrary-field theorem is checked symbolically in the proof. Its critical steps are:

1. The neutral component is the diagonal algebra, so every component-permuting automorphism permutes the diagonal primitive idempotents.
2. Each matrix-unit corner is one-dimensional, forcing a monomial action on matrix units.
3. The scalar coefficients satisfy \(c_{x,y}c_{y,z}=c_{x,z}\), hence \(c_{x,y}=d_xd_y^{-1}\).
4. The degree equation forces \(\sigma(x)=a\alpha(x)\) with \(\alpha\in\operatorname{Aut}(G)\).
5. Every such diagonal-plus-affine transformation is realized, so the inclusions are equalities rather than upper bounds.

`verify.py` performs an independent finite sanity check of the combinatorial step for \(C_2\), \(C_3\), \(C_4\), \(C_2\times C_2\), and \(S_3\). It enumerates all coordinate permutations, checks whether each one maps every degree class to a single degree class, reconstructs the induced degree permutation, verifies that it is a group automorphism, and checks the affine formula. It also checks representative finite-field order formulas. The saved output ends with `CHECK_OK`.

The finite checks are not exhaustive evidence for arbitrary finite groups and are not used as such. The proof, not the computation, establishes the general statement. Independent audit has not been performed.
