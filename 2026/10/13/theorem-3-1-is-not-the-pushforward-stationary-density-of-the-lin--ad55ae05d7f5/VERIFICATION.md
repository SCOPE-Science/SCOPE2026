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
The bundled checker reconstructs the corrected local stationary approximation.

It verifies the Itô logarithm identity
\[
d\log x
=
\left(
\frac{mS}{a+S}-D-\frac{\sigma^2}{2}
\right)dt+\sigma\,dB.
\]

For
\[
A=
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&0
\end{pmatrix},
\]
it verifies that the stated mean solves the affine stationary equation and that the stated covariance solves
\[
A\Sigma+\Sigma A^T+
\begin{pmatrix}
0&0\\
0&\sigma^2
\end{pmatrix}
=0.
\]

It verifies
\[
\left|
\frac{\partial(\log(S/S^*),\log(x/x^*))}{\partial(S,x)}
\right|
=
\frac{1}{Sx}.
\]

For the source parameters
\[
S^0=4,\quad D=2,\quad m=3,\quad a=1,
\]
the checker obtains
\[
a_{11}=-\frac83,\quad
a_{12}=-2,\quad
a_{21}=\frac23,
\]
\[
\mu_Z=-\sigma^2,
\qquad
\Sigma_{22}=\frac{19\sigma^2}{16}.
\]

At \(\sigma=0.15\), it returns the corrected linearized microorganism mode and mean reported in the finding.

No nonlinear stationary-distribution claim is inferred from this replay.
