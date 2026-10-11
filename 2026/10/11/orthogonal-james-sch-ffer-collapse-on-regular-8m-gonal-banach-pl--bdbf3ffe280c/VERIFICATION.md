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
N=8m,
\qquad
\alpha=\frac{\pi}{N},
\qquad
c=\cos\alpha,
\qquad
s=\sin\alpha,
\]
one has
\[
\frac{\pi}{4}=2m\alpha,
\]
so the directions \(\pm\pi/4\) are facet-normal directions.

For a smooth reference-edge point
\[
x=(c,t),
\qquad
-s<t<s,
\]
Birkhoff--James orthogonality forces
\[
y=(0,\pm c),
\]
and
\[
\|x+y\|
=
\sqrt2+\frac{t}{\sqrt2c},
\qquad
\|x-y\|
=
\sqrt2-\frac{t}{\sqrt2c}
\]
after choosing the positive perpendicular representative.

At the endpoint vertex
\[
x=(c,s),
\]
the first half of the Birkhoff sector is
\[
y=(-r,c),
\qquad
0\le r\le s,
\]
and
\[
\|x+y\|
=
\sqrt2+\frac{s-r}{\sqrt2c},
\qquad
\|x-y\|
=
\sqrt2-\frac{s-r}{\sqrt2c}.
\]
The second half-edge is the reflected formula with the two terms interchanged.

The bundled `verify.py` reconstructs regular \(8m\)-gons for \(1\le m\le12\), samples these complete analytic branches, and checks the quarter-turn equality pairs. The proof of the continuum statement is the exact support-functional analysis in `RESULT.md`, not the sampling.

No independent audit or independent validation has been performed.
