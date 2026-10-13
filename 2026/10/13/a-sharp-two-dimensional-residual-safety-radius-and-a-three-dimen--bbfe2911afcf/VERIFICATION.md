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
The universal statements are analytic. The checker replays exact rational instances.

For the two-dimensional sharpness family
\[
E=
\begin{pmatrix}
r&M\\
0&r
\end{pmatrix},
\]
the exact Frobenius squares are
\[
\|E\|_{\mathrm F}^2=2r^2+M^2
\]
and
\[
\|E^2\|_{\mathrm F}^2=2r^4+4r^2M^2.
\]
At
\[
r=\frac34,\qquad M=2,
\]
the checker verifies strict first-step growth while
\[
\rho(E)=\frac34<1.
\]

For
\[
N=
\begin{pmatrix}
0&M&0\\
0&0&M\\
0&0&0
\end{pmatrix},
\]
the checker verifies
\[
N^2=
\begin{pmatrix}
0&0&M^2\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
N^3=0.
\]
At \(M=10\),
\[
\frac{\|N^2\|_{\mathrm F}^2}{\|N\|_{\mathrm F}^2}=50.
\]
It also reconstructs the Newton–Schulz inverse iterates for
\[
A=I_3,\qquad X_0=I_3-N
\]
and checks
\[
X_2=I_3.
\]

Finite replay is corroborative only. The all-\(2\times2\) threshold follows from unitary Schur form, and minimality at zero spectral radius follows from Cayley–Hamilton.

Unproved limits include an all-\(2\times2\) spectral-norm safety radius, practical initialization families, and floating-point transient behavior.
