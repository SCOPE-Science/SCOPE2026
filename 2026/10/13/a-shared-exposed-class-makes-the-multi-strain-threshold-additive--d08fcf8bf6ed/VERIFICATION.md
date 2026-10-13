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

For the exact two-strain certificate, take
\[
\alpha=\frac45,
\quad
\beta=\frac32,
\quad
\mu=\frac1{10},
\quad
\varphi_1=\varphi_2=\frac9{20},
\]
\[
\mu_1=\mu_2=\frac15,
\quad
\gamma_1=\gamma_2=\frac7{10},
\quad
\delta_1=\frac15,
\quad
\gamma=\frac7{10}.
\]
Then
\[
\phi=\frac9{10},
\qquad
\mu+\phi=1,
\qquad
\mu_j+\gamma_j+\mu=1,
\qquad
\mu+\delta_1+\gamma=1.
\]
The source's common contribution is
\[
C_0=\frac{27}{100},
\]
and each strain contribution is
\[
A_j=\frac{54}{100}.
\]
Thus
\[
\mathcal R_{\mathrm{src}}^2
=C_0+A_j
=\frac{81}{100},
\qquad
\mathcal R_{\mathrm{src}}=\frac9{10},
\]
whereas
\[
\mathcal R_{\mathrm{pool}}
=C_0+A_1+A_2
=\frac{27}{20}.
\]

The infected Jacobian is
\[
M=
\begin{pmatrix}
-1&\frac32&\frac32&\frac32\\
\frac9{25}&-1&0&0\\
\frac9{25}&0&-1&0\\
\frac9{50}&0&0&-1
\end{pmatrix}.
\]
The bundled `verification/verify.py` checks with exact rational arithmetic that
\[
\det(\lambda I-M)
=(\lambda+1)^2
\left(\lambda^2+2\lambda-\frac7{20}\right).
\]
Its largest root is
\[
-1+\frac{3\sqrt{15}}{10}>0.
\]
Therefore this disease-free equilibrium is linearly unstable despite the published threshold being below one.

The general formula in `RESULT.md` is proved algebraically from the rank-one next-generation matrix; the finite checker is an exact replay certificate for the claimed threshold reversal.
