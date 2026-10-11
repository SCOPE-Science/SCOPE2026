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

For the equal-degree family, the cited source reduces the radial problem to
\[
x^2-Ax+|a|^2=0,
\qquad
x=|z|^{2n},
\qquad
A=|b|^2-2\operatorname{Re}a.
\]

In the zero-existence region,
\[
A\ge2|a|.
\]
Set
\[
A=2|a|\cosh\eta.
\]
Then
\[
\Delta=A^2-4|a|^2
=
4|a|^2\sinh^2\eta,
\]
and hence
\[
x_\pm
=
\frac{A\pm\sqrt{\Delta}}2
=
|a|e^{\pm\eta}.
\]

Therefore
\[
\rho_\pm
=
x_\pm^{1/(2n)}
=
|a|^{1/(2n)}
e^{\pm\eta/(2n)}.
\]
This immediately verifies
\[
\rho_+\rho_-=|a|^{1/n}
\]
and
\[
\log(\rho_+/\rho_-)
=
\eta/n.
\]

Also,
\[
\sinh\eta
=
\frac{\sqrt{\Delta}}{2|a|},
\]
so
\[
\eta
=
\operatorname{arsinh}
\left(
\frac{\sqrt{\Delta}}{2|a|}
\right).
\]

For a fixed admissible radius, the source phase equation expresses
\[
e^{in\varphi}
\]
as a unimodular constant. Its \(n\) solutions are equally spaced, so each radius supports a regular \(n\)-gon.

Finally,
\[
\operatorname{arsinh}s=s+O(s^3)
\]
and
\[
\sinh y=y+O(y^3)
\]
give the displayed square-root splitting as \(\Delta\downarrow0\) with \(a\ne0\) fixed.

The verification uses the exact source quadratic and elementary identities only. Numerical examples are not used as proof.
