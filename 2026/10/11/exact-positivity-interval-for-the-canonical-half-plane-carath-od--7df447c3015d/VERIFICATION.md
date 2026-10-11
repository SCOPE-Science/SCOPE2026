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

With
\[
w=\lambda z
\]
and
\[
\beta=1-\alpha,
\]
the source formula is
\[
H_\alpha(w)
=
\frac{
1-(1-\beta)w-\beta^2w^2
}{
(1+w)(1-\beta w)
}.
\]

For
\[
0<\beta<1
\]
and
\[
|w|=1,
\]
write
\[
x=\operatorname{Re}w.
\]
Direct algebra gives
\[
\operatorname{Re}H_\alpha(w)
=
\frac{
\beta(\beta^2+3-2(\beta+1)x)
}{
2(\beta^2+1-2\beta x)
}.
\]
Its derivative in
\[
x
\]
is exactly
\[
-\frac{
\beta(1-\beta)^2
}{
(\beta^2+1-2\beta x)^2
}.
\]
Therefore the finite boundary minimum is approached at
\[
w=1
\]
and equals
\[
\beta/2.
\]

The partial-fraction identity
\[
H_\alpha(w)
=
\beta
+
\frac{(1-\beta)(\beta+2)}
{(\beta+1)(1+w)}
-
\frac{1-\beta}
{(\beta+1)(1-\beta w)}
\]
shows that the exceptional boundary point
\[
w=-1
\]
has limiting real part strictly above
\[
\beta/2
\]
from inside the disk. The harmonic minimum principle therefore gives
\[
\operatorname{Re}H_\alpha(w)>\beta/2
\]
in the disk, and radial convergence to
\[
w=1
\]
proves sharpness.

At
\[
\alpha=0,
\]
the function is identically
\[
1.
\]
At
\[
\alpha=1,
\]
it is
\[
(1-w)/(1+w),
\]
which has positive real part in the disk and infimum zero.

For
\[
\alpha<0
\]
or
\[
\alpha>2,
\]
the continued formula has an interior pole. For
\[
1<\alpha\le2,
\]
its boundary real part at
\[
w=i
\]
is negative, so nearby interior points also have negative real part.

All displayed identities were replayed symbolically. Numerical evaluations were used only as consistency checks.
