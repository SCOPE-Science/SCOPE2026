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

The source proves, in dimension four,
\[
\det A\le U_1(\alpha),
\qquad
\det A\le U_2(\alpha),
\]
with
\[
U_1(\alpha)=
\alpha\left(\frac{4-f_1(\alpha)}{3}\right)^6,
\qquad
U_2(\alpha)=
\alpha\left(\frac{4-f_2(\alpha)}{3}\right)^{12}.
\]

The crossing condition \(U_1=U_2\) is equivalent to
\[
(4-f_2)^2=3(4-f_1).
\]
Eliminating the radicals gives the degree-eight polynomial \(P\) printed in RESULT.md. The checker uses an exact rational Sturm sequence and verifies that \(P\) has one root in \((0,1)\), with
\[
0.523194<\alpha_*<0.523195.
\]

The source proves that \(f_j(e^x)\) is convex. Therefore \(\log U_j(e^x)\) is concave on the feasible positive-base domain.

For the first branch,
\[
D_1(\alpha)>0
\iff
49\alpha^3+224\alpha^2+192\alpha-256<0.
\]
The checker verifies the right-hand side is negative at \(0.523195\), hence at the crossing.

For the second branch, every zero of its logarithmic derivative in \((0,1)\) is a zero of the degree-nine polynomial \(Q\) printed in RESULT.md. The checker proves by Sturm's theorem that \(Q\) has exactly one root in \((0,1)\), lying in
\[
(0.5165,0.5166).
\]
The exact endpoint signs
\[
D_2(1/2)=\frac{3}{175}>0
\]
and \(D_2(1)<0\) show that this is the unique derivative zero. Since it lies below \(\alpha_*\), the second branch is decreasing at and after the crossing.

These facts prove
\[
\max_{0<\alpha\le1}\min\{U_1(\alpha),U_2(\alpha)\}
=
U_1(\alpha_*)=U_2(\alpha_*).
\]

High-precision bisection of the original unsquared crossing equation gives the display values
\[
\alpha_*=0.5231942870027930993\ldots,
\qquad
C_4=0.8162394033204106090\ldots .
\]
The decimal computation is not used for the proof.

The lower bound
\[
4\sqrt3/9
\]
comes directly from the source's explicit dimension-four circular-cone ellipsoid. The theorem does not certify that the lower or upper endpoint is the true value of the four-dimensional extremal constant.
