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

The primary source gives the regularized equation
\[
F(q,\rho)=0
\]
with
\[
F(q,0)
=
q\operatorname{Si}(\pi)-\pi.
\]
Hence
\[
\kappa
=
\frac{\pi}{\operatorname{Si}(\pi)}
\]
and
\[
F_q(\kappa,0)
=
\operatorname{Si}(\pi)>0.
\]

The endpoint parameter derivatives are
\[
\partial_\nu S_0(0,\pi)
=
\int_0^1
\frac{\log t\,\sin(\pi t)}{t}\,dt
=
A,
\]
\[
\partial_a S_0(0,\pi)
=
0,
\]
and
\[
C_0(0,\pi)
=
\int_0^1
\frac{\cos(\pi t)-1}{t}\,dt
=
B.
\]
The first derivatives at zero of
\[
\cos(\pi\rho)
\]
and
\[
\operatorname{sinc}(\pi\rho)
\]
are zero. Therefore
\[
F_\rho(\kappa,0)
=
\kappa^2A-\pi\kappa B.
\]

Implicit differentiation gives
\[
q'(0)
=
-\frac{F_\rho(\kappa,0)}{F_q(\kappa,0)}
=
\frac{\kappa^2}{S}(SB-A).
\]
Thus
\[
q(\rho)
=
\kappa+\beta\rho+O(\rho^2),
\]
and
\[
\nu(\rho)
=
\kappa\rho+\beta\rho^2+O(\rho^3).
\]

All integrals defining the derivatives are absolutely convergent. The decimal value of
\[
\beta
\]
is only a numerical evaluation of the exact integral expression and is not used to prove the asymptotic.
