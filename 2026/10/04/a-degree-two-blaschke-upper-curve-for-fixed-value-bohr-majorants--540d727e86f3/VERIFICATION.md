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

Set
\[
s=\sqrt{\rho}
\]
and
\[
B_\rho(z)
=
\left(
\frac{z-s}{1-sz}
\right)^2.
\]
The coefficient expansion is
\[
B_\rho(z)
=
\rho
+
\sum_{n\ge1}
s^{n-2}(1-\rho)
\left(
n(1-\rho)-(1+\rho)
\right)z^n.
\]

For
\[
0<\rho\le1/3,
\]
the coefficient of \(z\) is negative and every coefficient from degree two onward is nonnegative. Hence
\[
M B_\rho(r)
=
\left(
\frac{r-s}{1-sr}
\right)^2
+
4s(1-s^2)r.
\]

Subtracting
\[
P_\rho(r)
=
s^2+\frac{(1-s^4)r}{1-s^2r}
\]
gives
\[
M B_\rho(r)-P_\rho(r)
=
-
\frac{
r(1-s^2)Q_s(r)
}{
(1-rs)^2(1-rs^2)
},
\]
where
\[
Q_s(r)
=
4s^5r^3
+
(-6s^4-4s^3+2s^2)r^2
+
(7s^2-2s-1)r
+
(1-s)^2.
\]

The endpoint values satisfy
\[
Q_s(1/3)>0,
\qquad
Q_s(1)<0.
\]
Moreover, \(Q_s'\) is convex in \(r\), and its two endpoint values are strictly negative throughout
\[
0<s\le1/\sqrt3.
\]
Therefore \(Q_s\) is strictly decreasing on \([1/3,1]\) and has exactly one zero there.

For every radius above that zero, the explicit admissible Blaschke product violates the comparison. This proves the upper bound without numerical experimentation.

At
\[
\rho=1/3,
\]
the zero equation reduces exactly to
\[
2\sqrt3\,r^3
-
6\sqrt3\,r^2
+
(18-9\sqrt3)(r+1)
=
0.
\]
Its unique root in \((1/3,1)\) evaluates to
\[
0.727436801449824\ldots .
\]

The decimal is not used as a certificate; the exact cubic and monotonicity proof are the certificate.
