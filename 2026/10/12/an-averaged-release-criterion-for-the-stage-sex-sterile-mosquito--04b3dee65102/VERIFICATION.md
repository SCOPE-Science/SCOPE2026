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
The analytic proof uses the exact per-capita birth envelope
\[
Q(M)
=
\frac{A}
{C\left(\sqrt{D+BHM}+\sqrt{BHM}\right)^2}.
\]

The bundled checker reconstructs the source's displayed biological parameters as exact rational numbers and reconstructs the carrying capacity using the equilibrium identity printed in the numerical section.

For the periodic family
\[
M_s(t)
=
s\left(1.3+\sin\frac{\pi t}{8}\right),
\]
it evaluates
\[
\overline Q(s)
=
\frac1{16}\int_0^{16}Q(M_s(t))\,dt
\]
with 80-digit adaptive quadrature and independently with a composite Simpson rule.

The checker verifies
\[
\overline Q(120000)
\approx
0.0382217709502678042053
<
0.04
\]
and
\[
\overline Q(60000)
\approx
0.0737501718144166751096
>
0.04.
\]

It also numerically solves
\[
\overline Q(s)=0.04
\]
for the sufficient-envelope crossing and obtains
\[
s_{\rm env}
\approx
114458.94554370316814.
\]

The general extinction theorem is analytic. The numerical calculations are used only for the source-specific parameter application.
