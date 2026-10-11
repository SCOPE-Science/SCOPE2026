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
p(z)=az^2+bz+c
\]
with
\[
a\ne0,
\]
an ambient translation and a unitary rotation reduce the graph to
\[
F(z)=(z,Az^2),
\qquad
A=|a|.
\]

For distinct
\[
z,w,
\]
the chord is
\[
\Delta
=
(w-z)
\left(
1,A(w+z)
\right).
\]
The tangent vector at
\[
z
\]
is
\[
(1,2Az),
\]
and
\[
(-2A\bar z,1)
\]
is an exact Hermitian normal vector. Therefore
\[
\left|
P_{N_z}\Delta
\right|
=
\frac{
A|w-z|^2
}{
\sqrt{1+4A^2|z|^2}
}.
\]

If an ambient point has
\[
F(z)
\]
and
\[
F(w)
\]
as two nearest points at distance
\[
r,
\]
orthogonality of the nearest-point displacement and equality of squared distances imply
\[
\|\Delta\|^2
\le
2r
\left|
P_{N_z}\Delta
\right|.
\]
Substitution yields
\[
r
\ge
\frac{
\sqrt{1+4A^2|z|^2}
\left(
1+A^2|w+z|^2
\right)
}{
2A
}
\ge
\frac1{2A}.
\]
Hence nearest-point projection is unique at every smaller distance.

For sharpness, use
\[
y_v=(0,v),
\qquad
v>\frac1{2A}.
\]
After angular minimization, squared distance to the graph is minimized by
\[
u+(Au-v)^2,
\qquad
u=|z|^2.
\]
Its unique positive radial minimizer is
\[
u_v
=
\frac{2Av-1}{2A^2}.
\]
The two phases
\[
z=\pm\sqrt{u_v}
\]
give distinct global nearest points, at common distance
\[
r_v
=
\sqrt{
\frac{4Av-1}{4A^2}
}.
\]
As
\[
v\downarrow1/(2A),
\]
\[
r_v\downarrow1/(2A).
\]
Thus the lower uniqueness radius is sharp.

The affine case
\[
a=0
\]
is an affine complex line and has global orthogonal projection, hence infinite reach.

All proof steps are exact. No numerical sampling or finite experiment establishes any continuum assertion.
