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

For
\[
n\ge2,
\]
the principal boundary arc is
\[
\gamma(\theta)
=
r(\theta)e^{i\theta},
\qquad
r(\theta)
=
(2\cos(n\theta))^{1/n},
\qquad
0<\theta<\frac{\pi}{2n}.
\]

With
\[
\alpha=\frac{\pi}{2(n+1)},
\qquad
q=(2\sin\alpha)^{1/n},
\qquad
c=q\cos\alpha,
\]
set
\[
D(\theta)=|\gamma(\theta)-c|^2.
\]
Since
\[
r'/r=-\tan(n\theta),
\]
direct differentiation gives
\[
D'(\theta)
=
\frac{2r(\theta)}
{\cos(n\theta)}
\left[
c\sin((n+1)\theta)
-r(\theta)\sin(n\theta)
\right].
\]

Define
\[
J(\theta)
=
\frac{r(\theta)\sin(n\theta)}
{\sin((n+1)\theta)}.
\]
All factors used below are positive on the stated interval. Logarithmic differentiation and multiplication by positive denominators reduce the sign of
\[
J'
\]
to the sign of
\[
n\sin\theta\cos(n\theta)
-
\sin(n\theta)\cos\theta,
\]
which is the sign of
\[
n\tan\theta-\tan(n\theta).
\]
Strict increase of
\[
\tan x/x
\]
on
\[
(0,\pi/2)
\]
therefore gives
\[
J'(\theta)<0.
\]

At
\[
\theta=\alpha,
\]
one has
\[
n\alpha=\frac{\pi}{2}-\alpha,
\qquad
(n+1)\alpha=\frac{\pi}{2},
\qquad
r(\alpha)=q,
\]
and therefore
\[
J(\alpha)=q\cos\alpha=c.
\]
It follows that
\[
D'<0
\]
before
\[
\alpha
\]
and
\[
D'>0
\]
after it. Hence the nearest positive boundary point occurs at
\[
\alpha,
\]
with the symmetric point at
\[
-\alpha.
\]

The minimum squared distance is
\[
D(\alpha)
=
q^2\sin^2\alpha.
\]
Thus the disk centered at
\[
q\cos\alpha
\]
with radius
\[
q\sin\alpha
\]
lies inside the lobe. The cited source independently proves that no disk in any lobe can have larger radius, so equality follows.

For the asymptotic law,
\[
n\sin\alpha_n
=
\frac{\pi}{2}
\left(
1-\frac1n+O(n^{-2})
\right)
\]
and
\[
q_n
=
1+\frac{\log(\pi/n)}{n}
+
O\!\left(\frac{(\log n)^2}{n^2}\right).
\]
Their product gives the stated correction.

The proof uses exact continuum inequalities. Finite numerical checks are not used to establish either equality or asymptotics.
