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
The finite-exponent premise was checked against Proposition 8.10 of arXiv:2609.39031v1. The source's groupoid endpoint calculation gives \(\|f\|_{\infty,\mathrm{red}}=\|f^*\|_{1,\mathrm{red}}\), and the canonical Steinberg map respects involution.

For the new endpoint step, each semigroup generator acts by a partial permutation on coordinates. For every finite algebraic combination, the matrix of the involution is the conjugate transpose, so the exact \(\ell^\infty\) row-sum norm equals the exact \(\ell^1\) column-sum norm of the involuted element. This avoids the false use of density of finitely supported vectors in \(\ell^\infty\).

The completion step uses the published fact that the Steinberg algebra is \(I\)-norm dense in \(C_c(G(S))\) for Hausdorff ample \(G(S)\), together with the published bound of every reduced exponent norm by the \(I\)-norm. No computation or finite enumeration is used as evidence for an infinite statement.

The proof does not verify a non-Hausdorff extension, a zero-semigroup contracted version, or equivalence with every alternative convention for reduced inverse-semigroup Banach algebras.
