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

The claim was checked directly in the quotient algebra
\[
\mathfrak A(V^*)=\mathbb K\oplus V^*\oplus\mathbb K
\]
with the multiplication published in arXiv:2609.32334v1.

For a closed two-sided ideal \(I\), the following exhaustive checks were performed:

- If \(I\) has no nonzero diagonal coordinate, then \(I\subseteq0\oplus V^*\oplus0\), and scalar left/right actions show that \(I\) is exactly \(0\oplus W\oplus0\) for a closed linear subspace \(W\subseteq V^*\).
- If \(I\) contains an element with nonzero first diagonal coordinate, compression by \(e_0\) yields \(e_0\in I\), and \(re_0=r\) forces the entire radical into \(I\).
- If \(I\) contains an element with nonzero second diagonal coordinate, the symmetric argument yields \(e_1\in I\) and the entire radical.
- If both types of diagonal coordinate occur, \(e_0+e_1=1\in I\), so \(I\) is the whole algebra.
- Otherwise exactly one diagonal coordinate is allowed, giving one of the two codimension-one maximal ideals.

The quotient map \(q_V\) has kernel \(\mathcal K(X_V)\), so closed ideals containing the compacts correspond exactly to closed ideals of the Calkin algebra. The source explicitly identifies the preimage of the radical with \(\mathcal E(X_V)\).

No computational certificate is needed. The proof establishes only the ideal lattice above \(\mathcal K(X_V)\); it leaves the lattice below the compacts unclassified. The public-date check uses the first arXiv submission of arXiv:2609.32334v1 on 2026-09-26.
