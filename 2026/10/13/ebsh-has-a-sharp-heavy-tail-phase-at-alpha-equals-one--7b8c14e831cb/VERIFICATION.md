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
Let
\[
a=\frac{\pi}{2},
\qquad
u=e^{-x^\alpha}.
\]
The exact survival is
\[
1-F(x)
=
\frac{\sinh(a)-\sinh(a(1-u)^\theta)}{\sinh(a)}.
\]
Since
\[
(1-u)^\theta=1-\theta u+O(u^2),
\]
Taylor expansion at \(a\) gives
\[
1-F(x)
\sim
a\theta\coth(a)e^{-x^\alpha}.
\]

The exact density then gives
\[
f(x)
\sim
a\alpha\theta\coth(a)x^{\alpha-1}e^{-x^\alpha},
\]
hence
\[
h(x)\sim\alpha x^{\alpha-1}.
\]

The positive-MGF domain follows by comparing
\[
tx-x^\alpha.
\]
It tends to \(+\infty\) for \(0<\alpha<1\), equals \((t-1)x\) at \(\alpha=1\), and tends to \(-\infty\) for every fixed \(t>0\) when \(\alpha>1\).

The included checker evaluates the exact CDF and density for several parameter choices and verifies the normalized tail, density, hazard, and fixed-shift survival limits. Finite computation is not used as proof.
