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

The source quantity is
\[
r_p=\frac1{1+2C_q},
\]
where
\[
C_q
=
\left(
\frac1{2\pi}
\int_0^{2\pi}
|\cos t|^q\,dt
\right)^{1/q}.
\]

The beta integral gives
\[
C_q^q
=
\frac{
\Gamma((q+1)/2)
}{
\sqrt\pi\,\Gamma((q+2)/2)
}.
\]

Because
\[
|\cos t|
\]
is nonconstant on the normalized circle, its
\[
L^q
\]
norm is strictly increasing with
\[
q.
\]
Since
\[
q=p/(p-1)
\]
decreases with
\[
p,
\]
the radius is strictly increasing.

At
\[
q=2,
\]
\[
C_2=1/\sqrt2,
\]
so
\[
r_2=\sqrt2-1.
\]

For
\[
q\to\infty,
\]
the gamma ratio gives
\[
C_q
=
1
-
\frac{
\log q+\log(\pi/2)
}{
2q
}
+
O\!\left(
\frac{(\log q)^2}{q^2}
\right).
\]
Substitution yields
\[
r_p
=
\frac13
+
\frac{
\log q+\log(\pi/2)
}{
9q
}
+
O\!\left(
\frac{(\log q)^2}{q^2}
\right),
\]
and therefore the stated
\[
p\downarrow1
\]
law.

For
\[
q=1+\delta,
\]
the derivative of
\[
\log C_q
\]
at
\[
q=1
\]
is
\[
\log\pi-1.
\]
Using
\[
\delta=1/(p-1)
\]
gives
\[
r_p
=
\frac{\pi}{\pi+4}
-
\frac{
4\pi(\log\pi-1)
}{
(\pi+4)^2
}
\frac1{p-1}
+
O((p-1)^{-2}).
\]

Independent numerical evaluations of the exact gamma formula agree with the asymptotic constants, but no numerical computation is used as proof.
