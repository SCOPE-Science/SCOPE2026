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

The verification consists of an exact normalization check and two theorem substitutions.

First,
\[
\|w^{-1}g\|_{L^2(w)}^2
=
\int |g|^2w^{-1},
\]
so
\[
\|S_{w^{-1}}\|_{L^2(w^{-1})\to L^{2,\infty}(w)}
=
\|S\|_{L^2(w)\to L^{2,\infty}(w)}.
\]

Second, the 2026 full weak theorem gives, for arbitrarily large dyadic \(A_2\) characteristic,
\[
C_{\mathrm{full}}(w)
>
\frac{e^{-2}}{48}
\sqrt{
[w]_{A_2^d}\log(1+[w]_{A_2^d})
}.
\]

Third, the 2018 restricted weak theorem gives for every dyadic \(A_2\) weight
\[
C_{\mathrm{res}}(w)
\le
C_0\sqrt{[w]_{A_2^d}}.
\]

Therefore
\[
\frac{C_{\mathrm{full}}(w)}
{C_{\mathrm{res}}(w)}
>
\frac{e^{-2}}{48C_0}
\sqrt{\log(1+[w]_{A_2^d})}.
\]

Choosing the source lower-characteristic threshold to tend to infinity gives the required sequence and makes the ratio diverge.

No numerical computation, extrapolation, or assumption about the restricted constant from below is used.
