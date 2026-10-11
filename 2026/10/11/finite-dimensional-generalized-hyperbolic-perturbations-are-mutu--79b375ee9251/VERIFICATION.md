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
The source theorem was checked directly in arXiv:2610.04179v1 at Definition 2.2, Theorem 2.3, Remark 2.5, and the future-research discussion.

The finite-dimensional proof was replayed symbolically. If \(H(x)=x+h(x)\) with \(\|h\|_\infty=M\), then for every compact \(C\), the set \(H^{-1}(C)\) is closed and bounded, hence compact. For any \(y\), choosing \(R>\|y\|+M\) makes the homotopy \(x+t h(x)-y\) zero-free on \(\|x\|=R\), so its Brouwer degree equals \(1\). Therefore \(H\) is surjective. The same applies to \(K\).

For a compact forward-invariant \(g\)-set \(C\), properness makes \(H^{-1}(C)\) compact, semiconjugacy makes it forward invariant under \(f\), and surjectivity makes the restricted map onto \(C\). The compact factor inequality yields one entropy inequality; \(K\) yields the reverse.

Limits: no injectivity or mutual inverse identity is proved. No claim is made about entropy notions defined directly on the whole noncompact phase space. No numerical computation or finite experiment is used.
