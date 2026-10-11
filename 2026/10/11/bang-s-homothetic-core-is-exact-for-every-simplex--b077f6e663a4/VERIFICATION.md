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

For \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\) with barycentric functions \(\lambda_i\) and gradients \(g_i\), direct substitution gives
\[
x\in S\div\{-Wu/2,Wu/2\}
\iff
\lambda_i(x)\ge\frac W2|\langle g_i,u\rangle|
\quad\text{for every }i.
\]
These lower barycentric bounds sum to \(A_u\), so the feasible set is exactly a translate of \((1-A_u)S\).

The key dual identity is checked symbolically in the proof:
\[
(S-S)^\circ=\operatorname{conv}\left\{\sum_{i\in I}g_i:I\subset\{0,\ldots,d\}\right\}.
\]
The forward inclusion follows from
\[
\left\langle\sum_{i\in I}g_i,v_j-v_k\right\rangle
=\mathbf1_{j\in I}-\mathbf1_{k\in I}.
\]
For the reverse inclusion, a vector in the polar has vertex evaluations contained in an interval of length one; subtracting the minimum makes those evaluations coefficients in \([0,1]\), and the differentiated barycentric identity reconstructs the vector as a cube combination of the \(g_i\).

Because \(w(S)=\min_{|u|=1}h_{S-S}(u)\), the circumradius of \((S-S)^\circ\) is exactly \(1/w(S)\). This gives the coefficient \(2/w(S)\) and hence the volume formula.

No computational certificate is needed: the result is proved for arbitrary dimension by exact barycentric identities and polar duality. The regular-simplex specialization is obtained by substituting the exact Gram relations \(\langle q_i,q_j\rangle=-1/d\) for distinct vertices.

Limits: the result concerns exact segment erosion and its directional minimum. It does not construct an optimal single plank for arbitrary higher-dimensional simplices and does not claim anything for total width above \(w(S)\).
