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

The proof was checked at four levels.

First, the product in \(L_8(\lambda)\) was written in coordinates and the universal candidate matrix
\[
\begin{pmatrix}
1&0&0\\
b&u&0\\
c&bu&u^2
\end{pmatrix}
\]
was substituted into every ordered pair of basis elements. Symbolic reduction in characteristic \(2\) modulo \(b^2-\lambda(u^2-1)\) makes every preservation identity vanish.

Second, exhaustiveness was checked algebraically from a general invertible matrix: the relations from \([a_1,a_2]=a_2\) and \([a_2,a_2]=a_3\) force triangular form, and invertibility forces the remaining diagonal parameter to be a unit, so no extra nilpotent-ring solutions are lost.

Third, the dual-number tangent family was checked directly against the derivation identity. Its three free parameters match the derivation matrix listed in arXiv:2609.24323v1.

Fourth, the split substitution \(v=b+s(u-1)\), with \(s^2=\lambda\), was checked symbolically to transform the relation into \(v^2=0\). This proves geometric nonreducedness; the scheme dimension is the hypersurface dimension \(3-1=2\), while the identity tangent dimension is \(3\).

The accompanying finite check over \(\mathbb F_2\) at \(\lambda=0\) enumerates every invertible \(3\)-by-\(3\) matrix and finds exactly \(2\) ordinary automorphisms, agreeing with the field-point specialization. This finite enumeration is not used to prove the arbitrary-field theorem.

Running `verify.py` produces `CHECK_OK`.
