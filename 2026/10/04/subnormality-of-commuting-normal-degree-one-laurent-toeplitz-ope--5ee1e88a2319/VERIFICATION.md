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

The proof was replayed algebraically from the displayed representation \(T_\Phi=S\otimes A+S^*\otimes B\). The cross terms cancel because commuting normal coefficients doubly commute, and the shift identities give \([T_\Phi^*,T_\Phi]=P_0\otimes(A^*A-B^*B)\).

For the subnormal necessity, the normal-extension identity \(\langle[T^*,T]x,xangle=\|(I-P)N^*x\|^2\) was derived directly; it implies invariance of \(\ker[T^*,T]\). Testing this invariant kernel on \(z\otimes h\) yields the exact condition \((A^*A-B^*B)B=0\).

For sufficiency, the spectral subspaces \(\ker D\) and \((\ker D)^\perp\) were checked to reduce both coefficients, \(DB=0\) forces \(B\) to vanish on the second subspace, and the analytic summand has the explicit normal extension \(U\otimes A\). Boundary cases \(D=0\), \(B=0\), singular \(D\), and infinite-dimensional coefficient space are included. No computation or search result is used as a proof.

Literature comparison was statement-level. The inspected classical matrix-valued theorem requires coprimeness/invertibility conditions, so it does not imply the mixed singular-sector conclusion. A residual risk remains that an equivalent degree-one statement occurs in older block-Toeplitz literature under different notation.
