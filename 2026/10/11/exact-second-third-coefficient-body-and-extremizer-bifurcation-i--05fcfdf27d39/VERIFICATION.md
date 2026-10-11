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
A=k-\frac1k,
\qquad
\mu=4k-\frac5k.
\]
The source coefficient identities are
\[
a_2=-Ac_1,
\qquad
a_3=-\frac A4(c_2-\mu c_1^2).
\]
The exact Schwarz coefficient body
\[
|c_2|\le1-|c_1|^2
\]
therefore becomes
\[
|a_2|\le A
\]
and
\[
\left|
a_3-\frac{\mu}{4A}a_2^2
\right|
\le
\frac A4
\left(
1-\frac{|a_2|^2}{A^2}
\right).
\]

Conversely, any point of this disk gives
\[
c_1=-a_2/A
\]
and an admissible
\[
c_2.
\]
If
\[
|c_1|<1,
\]
the Schur function
\[
w(\zeta)
=
\zeta
\frac{c_1+\eta\zeta}
{1+\overline{c_1}\eta\zeta},
\qquad
\eta=\frac{c_2}{1-|c_1|^2},
\]
has the prescribed first two coefficients. The boundary case
\[
|c_1|=1
\]
reduces to a disk rotation.

The source differential relation reconstructs
\[
q=g/(zg')
\]
from this
\[
w.
\]
Its positive-real dominant for
\[
1<k<k_0
\]
makes
\[
q
\]
zero-free, so the integral formula for
\[
g
\]
is analytic and realizes the desired coefficient pair in the original class.

For the marginal problem, at fixed
\[
r=|c_1|,
\]
the disk permits exactly
\[
\max|c_2-\mu c_1^2|
=
1+(|\mu|-1)r^2.
\]
Thus the optimizer is
\[
r=0
\]
for
\[
|\mu|<1
\]
and
\[
r=1
\]
for
\[
|\mu|>1.
\]
Since
\[
\mu(k)
\]
is strictly increasing and
\[
\mu(5/4)=1,
\]
the transition occurs exactly at
\[
k=5/4.
\]

At the transition, the displayed degree-two Blaschke products have
\[
c_1=re^{i\theta},
\qquad
c_2=-(1-r^2)e^{2i\theta},
\]
so they attain equality for every
\[
0\le r\le1.
\]

Symbolic substitutions and randomized points in the coefficient disk were used to check the transformations and equality family. These checks are supplementary; exactness follows from the analytic reconstruction above.
