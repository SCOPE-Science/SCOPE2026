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

For \(z\in S_{X_\omega}\), let
\[
M=\max\{|z_1|,|z_2|\},
\qquad
m=\min\{|z_1|,|z_2|\}.
\]
From
\[
M^2+\omega m^2=1
\]
and
\[
D(z)=M^2-m^2
\]
one gets
\[
\|z\|_2^2
=
\frac{2}{1+\omega}
-
\frac{1-\omega}{1+\omega}D(z).
\]

For every \(z\),
\[
N_\omega(z)^2
=
\|z\|_2^2-(1-\omega)m(z)^2.
\]
If
\[
p=\langle x,y\rangle
\]
and \(\sigma=1\) for \(p\ge0\), \(\sigma=-1\) otherwise, then
\[
\|x-\sigma y\|_2^2
=
\|x\|_2^2+\|y\|_2^2-2|p|.
\]
Since
\[
F_\omega(x,y)^2\le N_\omega(x-\sigma y)^2,
\]
direct substitution yields the claimed stability inequality.

For
\[
x=(a,b),\qquad y=(a,-b),
\qquad
a^2+\omega b^2=1,
\qquad
a\ge b\ge0,
\]
one has
\[
F_\omega(x,y)=2b,
\]
\[
D(x)=D(y)=\langle x,y\rangle=a^2-b^2,
\]
and
\[
m(x-y)=0.
\]
Both sides of the stability inequality reduce exactly to
\[
\frac{4}{1+\omega}\bigl(1-(1+\omega)b^2\bigr).
\]

The zero-defect conditions force both vectors onto diagonal rays and force Euclidean orthogonality, giving the diagonal James-extremal orbit. The near-extremizer estimates use only
\[
J^2-F^2=(J-F)(J+F)\le2J\varepsilon.
\]

No finite enumeration, numerical optimization, or external certificate is used as proof.
