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

Let
\[
K=\frac14 I_{\mathbb C^2},
\qquad
\Lambda_1 f=\Gamma_1 f=f_1,
\qquad
\Lambda_2 f=\Gamma_2 f=f_2.
\]
Then
\[
\sum_{i=1}^2\|\Lambda_i f\|^2
=
\|f\|^2
=
16\|K^*f\|^2,
\]
so
\[
C=16
\]
is a valid universal lower \(K\)-\(g\)-weaving bound, and
\[
D_\Gamma=1.
\]

Use
\[
U_1=I,
\qquad
U_2=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
Both are invertible and commute with \(K\). Direct spectral calculation gives
\[
\|U_2-U_1\|=2.
\]
Also
\[
\|U_1^\dagger\|=1
\]
and
\[
\|\widetilde{K^*}^{-1}\|=4.
\]
Hence the printed perturbation quantity equals
\[
1\cdot2\cdot4=8,
\]
which is strictly below
\[
\frac{C}{D_\Gamma}=16.
\]

For
\[
\sigma_1=\{1\},
\qquad
\sigma_2=\{2\},
\]
the selected transformed coefficient maps are both
\[
f\longmapsto f_1.
\]
Their energy vanishes at \(e_2\), but
\[
\|K^*e_2\|^2=\frac1{16}.
\]
Thus the selected weaving has no positive lower \(K\)-\(g\)-frame bound.

The corrected norm estimate is
\[
E(f)^{1/2}
\ge
\left(
\sqrt C\,\|U_1^\dagger\|^{-1}
-
\sqrt{D_\Gamma}\,\|U_2-U_1\|\,\|\widetilde{K^*}^{-1}\|
\right)
\|K^*f\|.
\]
Its positivity condition is
\[
\|U_1^\dagger\|\,\|U_2-U_1\|\,\|\widetilde{K^*}^{-1}\|
<
\sqrt{\frac{C}{D_\Gamma}}.
\]
The example fails this repaired condition because
\[
8\not<4.
\]

The complete source statement, defining frame inequalities, and proof were inspected in the open full text. All calculations above are exact.
