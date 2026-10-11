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

The source formulas used are
\[
\|f\|_{\mathfrak B_\lambda}
=
\sup_{z\in\mathbb D}
(1-|z|^2)|D_z(zf(z))|,
\]
\[
|\phi_n^\lambda(z)|
\le
\epsilon_n^{-1}|z|^n,
\]
and
\[
D_z(z\phi_n^\lambda)
=
(n+\lambda+1)\phi_n^\lambda.
\]

For positive real
\[
z=r,
\]
the defining finite sum satisfies
\[
\phi_n^\lambda(r)
=
\epsilon_n r^n
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}.
\]
Coefficient extraction from
\[
(1-t)^{-\lambda}(1-t)^{-(\lambda+1)}
=
(1-t)^{-(2\lambda+1)}
\]
gives
\[
\sum_{j=0}^n
\frac{(\lambda)_j(\lambda+1)_{n-j}}
{j!(n-j)!}
=
\frac{(2\lambda+1)_n}{n!}
=
\epsilon_n^{-2}.
\]
Thus the source upper bound is attained at every positive real radius.

The norm therefore reduces exactly to
\[
(n+\lambda+1)\epsilon_n^{-1}
\max_{0\le r<1}(1-r^2)r^n.
\]
For
\[
n\ge1,
\]
\[
\frac{d}{dr}\bigl((1-r^2)r^n\bigr)
=
r^{n-1}\bigl(n-(n+2)r^2\bigr),
\]
so the maximizing radius is
\[
r_n=\sqrt{\frac{n}{n+2}},
\]
and the maximum is
\[
\frac{2}{n+2}
\left(\frac{n}{n+2}\right)^{n/2}.
\]

Finally,
\[
\epsilon_n^{-1}
=
\sqrt{
\frac{\Gamma(n+2\lambda+1)}
{\Gamma(2\lambda+1)\Gamma(n+1)}
}
\sim
\frac{n^\lambda}{\sqrt{\Gamma(2\lambda+1)}},
\]
and
\[
\left(\frac{n}{n+2}\right)^{n/2}\to e^{-1}.
\]
This yields the stated asymptotic constant.

Direct finite-sum evaluations at several positive parameter values were used only as consistency checks. The proof itself is exact and symbolic.
