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

After a unitary change of coordinates, write
\[
z=(z',z_n),
\qquad
s=\|z'\|^2,
\qquad
t=|z_n|^2.
\]
The proposed envelope is
\[
u_q(z)=-(1-s)^q.
\]

For
\[
0<q\le1,
\]
\[
g_q'(s)=q(1-s)^{q-1}>0,
\qquad
g_q''(s)=q(1-q)(1-s)^{q-2}\ge0.
\]
Hence the Levi matrix
\[
g_q'(s)I
+
g_q''(s)\overline{z'}(z')^{\mathsf T}
\]
is positive semidefinite.

There is no \(z_n\)-dependence, so the Levi rank is at most
\[
n-1
\]
and
\[
(dd^cu_q)^n=0.
\]

On the unit sphere,
\[
t=1-s,
\]
and therefore
\[
u_q=-t^q=-|z_n|^{2q}.
\]
Inside the ball,
\[
t<1-s,
\]
which gives
\[
u_q<-t^q.
\]
Thus \(u_q\) is an admissible maximal minorant with the exact boundary trace. Maximal comparison against any other plurisubharmonic obstacle minorant proves equality with the envelope.

The minimum condition
\[
u_q=-1
\]
is equivalent to
\[
s=0,
\]
so the minimum set is exactly the complex diameter.

For
\[
q>1,
\]
the radial Levi eigenvalue is
\[
q(1-s)^{q-2}(1-qs),
\]
which is negative when
\[
s>1/q.
\]
Thus the same closed formula cannot be a plurisubharmonic envelope above the threshold.

No numerical computation or finite experiment is used.
