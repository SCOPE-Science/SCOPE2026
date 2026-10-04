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

For
\[
f_p(x)=\prod_i\left(\frac{x_i}{\sqrt{p_i}}\right)^{p_i},
\]
the exact gradient is
\[
\nabla f_p(x)=f_p(x)\left(\frac{p_1}{x_1},\ldots,\frac{p_d}{x_d}\right).
\]
If \(V=\{a\cdot x=0\}\), orthogonality of the antisphere tangent to \(V\) is therefore equivalent to
\[
\sum_i\frac{a_ip_i}{x_i}=0
\]
for every positive \(x\) on \(V\).

Writing
\[
y_i=a_ix_i\quad(a_i>0),
\qquad
z_j=-a_jx_j\quad(a_j<0)
\]
turns the seam equation into equality of two positive total masses and the orthogonality equation into equality of two reciprocal sums. A reciprocal sum with at least two positive variables is not constant on a fixed-sum simplex. Thus each sign class of the normal has exactly one coordinate. The remaining identity gives
\[
a_i^2p_i=a_j^2p_j,
\]
which is equivalent to the claimed weighted coordinate-pair seam.

The embedded `verify.py` was replayed from its actual package path. For dimensions \(2\) through \(9\) it samples positive weight vectors, checks every coordinate-pair seam at multiple positive antisphere points, and verifies the vanishing normal-gradient inner product. It separately tests representative non-admissible mixed-sign normals and confirms the reciprocal-balance defect changes when positive masses are redistributed at fixed total mass.

The replay output was:

`VERIFY_OK weighted geometric-mean seam rigidity`

The numerical checks are consistency tests only. The exhaustive statement is established by the analytic reciprocal-simplex argument.
