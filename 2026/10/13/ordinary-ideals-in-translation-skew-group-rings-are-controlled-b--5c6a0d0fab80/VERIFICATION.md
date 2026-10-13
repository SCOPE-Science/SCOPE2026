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

The universal argument is symbolic and was reconstructed from the displayed skew-group relation.

1. For every finite-support element, \(\operatorname{ad}_X\) acts on the \(g\)-component by the scalar \(c(g)\). Because the support is finite, ordinary Lagrange interpolation isolates each scalar fiber without any diagonalizability assumption beyond this explicit decomposition.
2. After shifting an isolated fiber by a group unit, it lies in \(C[X]\), where \(C=k\ker c\).
3. Conjugation by an element \(q\) with \(c(q)\ne0\) sends \(F(X)\) to \(F(X-c(q))\). For positive degree \(n\), the difference has degree \(n-1\) and leading coefficient \(-n c(q)\) times the original leading coefficient. Characteristic zero ensures this scalar is invertible.
4. Induction therefore gives \(I\cap C[X]=(I\cap C)[X]\), and the isolated-fiber decomposition gives \(I=A(I\cap C)\).
5. The direct decomposition by cosets of \(\ker c\) verifies \(AJ\cap C=J\); centrality verifies product transfer.
6. Central elements first lose all non-kernel group components by commuting with \(X\), then lose positive \(X\)-degree by commuting with a nontrivial translation, so \(Z(A)=C\).
7. In characteristic \(p\), \((X-1)^p-(X-1)=X^p-X\), confirming the stated boundary example.

No finite enumeration, numerical approximation, or external certificate is needed. The remaining limitation is literature access, not proof verification: one older crossed-product paper was available only through its abstract and is recorded as a residual originality risk.
