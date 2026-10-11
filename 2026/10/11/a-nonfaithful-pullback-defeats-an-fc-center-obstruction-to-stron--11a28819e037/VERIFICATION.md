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

The focal source was checked in its actual arXiv:2609.26479v1 PDF. The first page gives primary MSC \(37B05\) and the version date 2026-09-22. Definition 5.1 states that two-fold sTMSJ tests distinct pairs lying on different \(Z(G)\)-orbits. Remark 5.3 then asserts that \(\operatorname{{FC}}(G)\setminus Z(G)\ne\varnothing\) prevents any strong doubly minimal system. Proposition 5.15 later proves pullback preservation under an epimorphism carrying \(Z(G)\) onto \(Z(H)\), and the following sentence explicitly notes that the resulting actions are nonfaithful.

For \(G=\mathbb Z\times S_3\), direct group calculation gives
\[
Z(G)=\mathbb Z\times\{e\},
\qquad
\pi(Z(G))=\mathbb Z.
\]
Therefore Proposition 5.15 applies to projection \(\pi:G\to\mathbb Z\). A strong doubly minimal \(\mathbb Z\)-system exists by the classical theory recalled in the source, so its pullback is strong doubly minimal for \(G\).

The element \(g=(0,(12))\) lies in \(\ker\pi\), is noncentral, and has finite conjugacy class. Thus \(g\in\operatorname{{FC}}(G)\setminus Z(G)\). Since \(S^g=\operatorname{{id}}\), the graph used in Remark 5.3 is the diagonal. The diagonal consists of pairs on the same central orbit and hence does not violate Definition 5.1. This establishes the counterexample without numerical approximation.

No statement is verified beyond this scope: in particular, a faithful-action repair is neither proved nor refuted.
