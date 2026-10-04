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

The source family satisfies
\[
F_s'(z)
=
s\frac{1+z}{1-z}
+
(1-s)\frac{1-iz}{1+iz}.
\]

On
\[
z=e^{it},
\qquad
0<t<\frac{\pi}{2},
\]
this becomes
\[
F_s'(e^{it})
=
i
\left[
s\cot\frac t2
-
(1-s)\tan\left(\frac t2+\frac{\pi}{4}\right)
\right].
\]
The bracket is strictly decreasing and therefore has one zero \(t_s\). Its zero condition simplifies to
\[
\cos t_s-\sin t_s=1-2s.
\]

For
\[
c=\cos t_s,
\qquad
q=\sin t_s,
\]
and
\[
0<r<1,
\]
the common numerator controlling
\[
\operatorname{Im}F_s'(re^{it_s})
\]
is
\[
sq(1-2rq+r^2)
-
(1-s)c(1-2rc+r^2).
\]
Using
\[
s=\frac{1-c+q}{2}
\]
and
\[
c^2+q^2=1,
\]
this is exactly
\[
\frac12
(q-c)(1+c+q)(1-r)^2.
\]
Therefore its sign is the sign of \(2s-1\).

The radial identity
\[
e^{-it_s}F_s(e^{it_s})
=
\int_0^1F_s'(re^{it_s})\,dr
\]
transfers that sign to the imaginary part of the boundary value. Since the real part of the same integral is positive, the boundary value is nonzero.

Finally,
\[
\operatorname{Re}
\frac{e^{it}F_s'(e^{it})}{F_s(e^{it})}
=
\frac{
Y_s(t)
\operatorname{Im}(e^{-it}F_s(e^{it}))
}{
|e^{-it}F_s(e^{it})|^2
}.
\]
The two factors in the numerator have opposite signs on one side of \(t_s\) whenever
\[
s\ne\frac12.
\]
Hence a strict negative value occurs and persists at nearby interior points.

The packaged symbolic checker verifies the algebraic identities. The sign and continuity argument is analytic.
