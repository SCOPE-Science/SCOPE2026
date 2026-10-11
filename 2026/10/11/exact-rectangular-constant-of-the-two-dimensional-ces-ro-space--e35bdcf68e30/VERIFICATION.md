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

After normalization,
\[
M(s,t)^2=s^2+t^2+\frac{2}{\sqrt5}|st|.
\]
Smooth points reduce to \(x_z=(1,z)/\sqrt{A(z)}\), with Birkhoff tangent \(w_z=(-(z+1/\sqrt5),1+z/\sqrt5)\). The same-sign ratio is
\[
\frac{1+t\sqrt{B(z)/A(z)}}{\sqrt{1+4t^2/5}}.
\]
Every feasible interior stationary point has \(z<1/5\) and is strictly suboptimal. At the first coordinate crossing the profile is
\[
R(z)=\frac{z+1/\sqrt5}{\sqrt{A(z)}}+\frac{\sqrt{B(z)}}{A(z)},
\]
and the ratio decreases after that crossing.

The exact derivative equation for \(R\) yields
\[
25z^6+60\sqrt5\,z^5+260z^4+96\sqrt5\,z^3+45z^2-12\sqrt5\,z-10=0.
\]
There is one positive root by Descartes' rule; exact signs place it in \((1/3,1/\sqrt5)\). Axis-originating Birkhoff pairs have ratio at most \(\sqrt3\), strictly below the boundary maximum. Hence the root gives the global rectangular constant.

The numerical values
\[
z_*=0.35016603386984658446\ldots,\qquad
\mu=1.83053734256591701739\ldots
\]
are evaluations only, not proof.
