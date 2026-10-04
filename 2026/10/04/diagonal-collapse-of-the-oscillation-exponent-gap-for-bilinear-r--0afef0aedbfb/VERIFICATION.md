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

The verification is analytic.

For
\[
\|b\|_{\mathrm{BMO}_r}
=
\sup_Q
\left(
|Q|^{-1}\int_Q|b-\langle b\rangle_Q|^r
\right)^{1/r},
\]
direct substitution into the source definitions gives
\[
S_{r,r}(b,b)=\|b\|_{\mathrm{BMO}_r}^2
\]
and
\[
T_u(b,b)=\|b\|_{\mathrm{BMO}_{2u}}^2.
\]

The mixed lower bound becomes
\[
2\|b\|_{\mathrm{BMO}_2}^2
\lesssim
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|.
\]
With the fixed choice \(\varepsilon=1\), the mixed upper bound becomes
\[
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|
\lesssim
\|\Omega\|_\infty
\left(
\|b\|_{\mathrm{BMO}_3}^2+
\|b\|_{\mathrm{BMO}_4}^2
\right).
\]

The repeated-position lower bound contains
\[
\|b\|_{\mathrm{BMO}_2}^2+\|b\|_{\mathrm{BMO}_4}^2,
\]
while the fixed-\(\varepsilon\) upper bound contains
\[
\|b\|_{\mathrm{BMO}_3}^2+\|b\|_{\mathrm{BMO}_6}^2.
\]

John--Nirenberg identifies every finite \(\mathrm{BMO}_r\) seminorm up to constants depending only on \(d\) and \(r\). Therefore all displayed commutator norms are comparable to
\[
\|b\|_{\mathrm{BMO}}^2.
\]

The lower theorem's repeated-position requirement
\[
b^2\in L^2_{\mathrm{loc}}
\]
is guaranteed by
\[
b\in L^4_{\mathrm{loc}}.
\]

No finite numerical computation, limiting extrapolation in the bump parameter, or unproved endpoint passage is used.
