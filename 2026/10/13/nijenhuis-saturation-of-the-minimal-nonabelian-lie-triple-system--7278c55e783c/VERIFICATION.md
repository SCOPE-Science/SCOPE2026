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
The bundled checker reconstructs the product
\[
[e_1,e_2,e_2]=e_1
\]
and the two-order Nijenhuis identity.

For a symbolic matrix \(N=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), every coefficient of the universal Nijenhuis defect simplifies to zero. The checker also derives
\[
[x,y,z]_N=\det(x,y)(cz_1+dz_2)(de_1-ce_2).
\]

It exhaustively checks all endomorphisms over \(\mathbf F_3,\mathbf F_5,\mathbf F_7,\mathbf F_{11}\). Every matrix is Nijenhuis; exactly \(q^2\) induce the zero bracket; every remaining bracket is explicitly normalized to \([w,v,v]_N=w\); and the rank distributions match the stated formula.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The universal theorem is symbolic.
