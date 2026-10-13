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
The universal result is analytic.

For the standard L-stable ROS2 parameter
\[
\gamma=1+\frac1{\sqrt2},
\]
the stability function is
\[
R(z)=
\frac{1-(1+\sqrt2)z}
{\left(1-\left(1+\frac1{\sqrt2}\right)z\right)^2}.
\]
Its derivatives satisfy
\[
\operatorname{sgn}R^{(k)}(-h)
=
\operatorname{sgn}
\left(
1+\sqrt2-k+(3+2\sqrt2)h
\right)
\]
for every \(h\ge0\).

For
\[
J_n=-I+N_n,
\qquad N_n^n=0,
\]
the exact finite matrix-function identity is
\[
R(hJ_n)
=
\sum_{k=0}^{n-1}
\frac{h^k}{k!}R^{(k)}(-h)N_n^k.
\]
Distinct powers \(N_n^k\) occupy distinct subdiagonals. Thus the highest derivative \(k=n-1\) is the sharp positivity obstruction and gives
\[
n\le2+\sqrt2+(3+2\sqrt2)h.
\]

For \(n\ge4\), the positive recovery threshold simplifies exactly to
\[
h_n=3n-2-(2n-1)\sqrt2.
\]
The first one is
\[
h_4=10-7\sqrt2.
\]

The embedded `verify.py` checks these algebraic identities using rational arithmetic and exact comparisons against \(\sqrt2\). In particular, at \(n=4\) and \(h=1/20\), the critical sign factor is
\[
\frac{44-37\sqrt2}{40}<0.
\]

The finite checker corroborates the displayed formulas. It is not used as a substitute for the all-dimension proof.

Unproved limits include arbitrary Metzler matrices, nonlinear reaction systems, internal-stage positivity, approximate Jacobians, and the alternative L-stable ROS2 parameter.
