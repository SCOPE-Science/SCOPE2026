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

The source harmonic extension is written as a radial first mode plus Bessel sidebands. On the inner boundary, the sideband term is
\[
R(\theta)
=
\sum_{j\ne0}
\frac{
2S J_j(t)|1+mj|
}{
s^{|1+mj|}-s^{-|1+mj|}
}
e^{imj\theta}.
\]

Under
\[
m s^{-m}/t\to\lambda,
\]
the
\[
j=\pm1
\]
terms give
\[
R(\theta)
=
S t m s^{-m}
\left(
s^{-1}e^{im\theta}
-
s e^{-im\theta}
\right)
+
o(t^2),
\]
while all higher sidebands are
\[
o(t^2).
\]
Therefore
\[
\max_\theta\operatorname{Re}R(\theta)
=
S(s-s^{-1})\lambda t^2+o(t^2).
\]

The first-mode quotient is
\[
\frac{
SJ_0(t)-s
}{
SJ_0(t)-s^{-1}
}
=
\kappa
-
\frac{
S(s-s^{-1})
}{
4(S-s^{-1})^2
}
t^2
+
O(t^4).
\]
The linear response of
\[
|2\beta+R|/|2a+R|
\]
at
\[
R=0
\]
is
\[
\operatorname{Re}R/(2a^2),
\]
with
\[
a(0)=
\frac{
S-s^{-1}
}{
s-s^{-1}
}.
\]
Combining the two contributions yields
\[
\lVert\omega\rVert_\infty
=
\kappa
+
\frac{
S(s-s^{-1})
}{
4(S-s^{-1})^2
}
\left(
2(s-s^{-1})^2\lambda-1
\right)t^2
+
o(t^2).
\]

The source's outer-boundary estimate remains
\[
o(1)
\]
under
\[
mt\to0,
\]
and its first-mode outer quotient tends to
\[
\kappa/s^2<\kappa.
\]
Hence the inner boundary controls the global norm for small
\[
t.
\]

If
\[
m\log s
=
\log(1/t)
+
\log\log(1/t)
+
C+o(1),
\]
then
\[
m s^{-m}/t
\to
e^{-C}/\log s.
\]
The critical phase follows by setting this limit equal to
\[
1/[2(s-s^{-1})^2].
\]

The proof is analytic. Numerical evaluation was used only as a secondary sign check and is not needed for the asymptotic classification.
