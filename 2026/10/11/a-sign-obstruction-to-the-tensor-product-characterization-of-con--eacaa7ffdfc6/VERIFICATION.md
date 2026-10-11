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

Use
\[
H=K=\mathbb R,
\qquad
V_1=H,
\qquad
W_1=K,
\qquad
\Lambda_1=\Gamma_1=I,
\qquad
v_1=w_1=1.
\]
Let
\[
T=T_1=I,
\qquad
U=U_1=-I.
\]

For the first factor,
\[
\langle \Lambda_1U f,\Lambda_1T f\rangle
=
\langle -f,f\rangle
=
-|f|^2.
\]
The second factor is identical. Hence neither factor satisfies a positive lower controlled-frame inequality.

For the tensor family,
\[
U\otimes U_1=I,
\qquad
T\otimes T_1=I.
\]
Therefore
\[
\left\langle
(\Lambda_1\otimes\Gamma_1)(U\otimes U_1)(f\otimes g),
(\Lambda_1\otimes\Gamma_1)(T\otimes T_1)(f\otimes g)
\right\rangle
=
\|f\otimes g\|^2.
\]
Thus the tensor family has exact bounds \(1,1\).

For the repair, suppose
\[
q_H(f)\ge0,\qquad q_K(g)\ge0
\]
and
\[
A\|f\|^2\|g\|^2
\le
q_H(f)q_K(g)
\le
B\|f\|^2\|g\|^2.
\]
Fixing \(g_0\ne0\) gives \(q_K(g_0)>0\) and hence
\[
\frac{A\|g_0\|^2}{q_K(g_0)}\|f\|^2
\le q_H(f)\le
\frac{B\|g_0\|^2}{q_K(g_0)}\|f\|^2.
\]
Interchanging the factors gives the corresponding bounds for \(q_K\).

The publisher PDF was inspected as both extracted text and page images at the factor definition, tensor definition, theorem statement, and reverse proof. The counterexample is exact and finite-dimensional.
