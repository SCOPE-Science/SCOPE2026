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
S=
\begin{pmatrix}
1&1&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
1&1&0\\
0&0&0\\
0&1&0
\end{pmatrix}.
\]
Exact multiplication gives
\[
S^2=S,
\qquad
SK=KS=S,
\qquad
K^2=S.
\]
Thus
\[
SKS=S
\]
and
\[
KSK^2=K^2,
\]
so \(S\) is a Drazin inverse of \(K\) under the target definition.

For the one-component family with \(W=H\), weight \(1\), and \(\Lambda=K^*\),
\[
E(f)=\|K^*f\|^2.
\]
Also
\[
SS^*=
\begin{pmatrix}
2&0&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\]
so
\[
\|S\|=\sqrt2.
\]
At
\[
f=(1,0,-1),
\]
\[
\|K^*f\|^2=1,
\qquad
\|S^*f\|^2=2.
\]
Hence the printed lower constant \(1/\|S\|\) fails.

Since
\[
KS=S,
\]
taking adjoints gives
\[
S^*=S^*K^*.
\]
Therefore
\[
\|S^*f\|\le\|S\|\,\|K^*f\|,
\]
which yields the valid lower constant
\[
A/\|S\|^2.
\]

For
\[
f=(x,y,z),
\]
the exact ratio is
\[
\frac{\|K^*f\|^2}{\|S^*f\|^2}
=
\frac{|x|^2+|x+z|^2}{2|x|^2}.
\]
Its minimum is \(1/2\), attained at \(z=-x\), proving sharpness.

The target full text was inspected at its Drazin definition and the complete theorem/corollary statements. No numerical approximation or finite experimental search is used as mathematical evidence.
