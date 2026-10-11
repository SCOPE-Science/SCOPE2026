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

For \(t\) outside the finite exceptional set, let
\[
g_\pm
=
\frac{-\varphi\pm\sqrt{\varphi^2+4}}2.
\]
The source gives
\[
g_+g_-=-1
\]
and
\[
\alpha_\pm
=
\frac{g_\pm^2}{1+g_\pm^2}.
\]
Hence
\[
\alpha_++\alpha_-=1,
\]
so
\[
\kappa_t
=
\alpha_+\delta_{g_+}
+
\alpha_-\delta_{g_-}
\]
is a probability measure and the source structure formula is
\[
\mu(dt,dy)
=
\pi\,dt\,\kappa_t(dy).
\]

The support identity is
\[
Y^2+\varphi Y-1=0.
\]
The source weights give
\[
\mathbb EY=-\varphi.
\]
Therefore
\[
\mathbb EY^2
=
1-\varphi\mathbb EY
=
1+\varphi^2
\]
and
\[
\operatorname{Var}(Y)=1.
\]

Multiplication of the support identity by \(Y^{k-2}\) gives
\[
m_k=-\varphi m_{k-1}+m_{k-2}.
\]
The first values yield
\[
\mathbb E[(Y+\varphi)^3]=\varphi.
\]

For the Cauchy transform,
\[
\frac{\alpha_+}{g_+-w}
+
\frac{\alpha_-}{g_--w}
=
-\frac{w}{w^2+\varphi w-1}
=
-\frac{1}{\varphi+w-\frac1w}.
\]
This is exactly the real boundary slice of the source function.

All identities are symbolic consequences of the source support and weight formulas. No finite experiment or numerical approximation is used.
