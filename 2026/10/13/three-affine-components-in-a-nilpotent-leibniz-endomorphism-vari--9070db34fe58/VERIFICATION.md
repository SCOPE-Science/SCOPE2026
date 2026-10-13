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
The accompanying `artifacts/verify.py` is self-contained Python and directly implements the left Leibniz bracket
\[
[x,y]=x_1(y_1+y_2)z.
\]
For each of the \(2^9=512\) matrices over \(\mathbf F_2\) and the \(3^9=19683\) matrices over \(\mathbf F_3\), it checks every basis product before comparing to the proposed union of three components. The classification is thereby exhaustively tested for these two finite fields.

It computes ranks from minors, squares for idempotency, and cubes for nilpotency. For \(\mathbf F_5\) it constructs the complete union of all three parametrized affine spaces (rather than exhaustively traversing matrices outside that union) and checks its cardinality, all ranks, idempotents and nilpotents. This separate check does **not** establish completeness outside the union over \(\mathbf F_5\); the symbolic proof provides that conclusion over every field.

Observed totals (total, ranks zero through three, idempotents, nilpotents):

\[
\begin{array}{c|c|c|c|c}
q&\text{total}&\text{rank counts}&\text{idempotents}&\text{nilpotents}\\\hline
2&32&(1,15,12,4)&10&12\\
3&189&(1,56,96,36)&20&45\\
5&1625&(1,264,960,400)&52&225
\end{array}
\]

The checker terminates with `VERIFY_OK`. Characteristic two is included; the unreduced homomorphism scheme has not been investigated.
