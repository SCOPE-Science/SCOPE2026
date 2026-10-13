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

The bundled script performs symbolic and exact-rational checks.

For the disease-free exposed-infectious block
\[
A_0=
\begin{pmatrix}
-(\omega+\mu)&n\Lambda/\mu\\
\omega&-(\tau+\mu)
\end{pmatrix},
\]
it verifies
\[
\det(\lambda I-A_0)
=
\lambda^2+(\omega+\tau+2\mu)\lambda
+(\omega+\mu)(\tau+\mu)-\frac{n\Lambda\omega}{\mu}.
\]
It also checks that the source's displayed plus-eigenvalue condition produces the same threshold denominator
\[
\mu(\omega+\mu)(\tau+\mu).
\]

For the endemic state it symbolically obtains
\[
p(\lambda)
=
\lambda^3+
(\mu+c+a+b)\lambda^2+
(\mu+c)(a+b)\lambda+
abc.
\]
The general strict Routh-Hurwitz inequality is proved in `RESULT.md`.

The exact witness
\[
\mu=1,\quad\omega=2,\quad\tau=3,\quad n=1,\quad\Lambda=4
\]
gives
\[
\mathcal R_*=\frac23,\qquad
\mathcal R_{\mathrm{src}}=\frac43.
\]

No simulation or finite enumeration is used to infer the general theorem.
