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
# Verification notes
The nontrivial checks are mathematical rather than computational. First, the source and target have exactly two shift-fixed points, and an injective equivariant map permutes these. Second, by the finite-window representation, the image of a finite defect in a constant input differs from the corresponding constant output on finitely many coordinates. Third, for a two-defect input at distance beyond the window radius and finite output support, the output is exactly the disjoint union of translated single-defect outputs. For swapped fixed points, varying the number of intermediate \(1\)'s by one gives impossible successive multiples of \(n\). For preserved fixed points, varying the zero-gap by \(m\) gives \(n\mid m\). Finally, the graph eigenvalue satisfies \(\lambda^j=\lambda^{j-1}+1\); monotonicity yields strict entropy separation.

This proof is not based on finite enumeration, numerical evidence, an external formal proof, or an independent validation. The public literature search cannot guarantee absence of a differently formulated earlier result.
