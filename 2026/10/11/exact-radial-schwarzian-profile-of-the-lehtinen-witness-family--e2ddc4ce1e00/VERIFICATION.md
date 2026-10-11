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

The cited source gives
\[
S_{f_\alpha}(z)
=
\frac{1-\alpha^2}{2(1-z)^2}
+
\frac{(1-\alpha)\overline z}
{(1-|z|^2)(1-z)}
-
\frac{3\overline z^2}
{2(1-|z|^2)^2}.
\]

For
\[
A=(\alpha^2-1)/2,
\qquad
b=\alpha-1,
\qquad
w=(1-|z|^2)/(1-z),
\]
this becomes
\[
(1-|z|^2)^2S_{f_\alpha}(z)
=
-\left(
Aw^2+b\overline zw+\frac32\overline z^2
\right).
\]

On
\[
|z|=r,
\]
\[
|w|
=
\frac{1-r^2}{|1-z|}
\le1+r.
\]
Hence
\[
(1-r^2)^2|S_{f_\alpha}(z)|
\le
A(1+r)^2
+
br(1+r)
+
\frac32r^2.
\]
At
\[
z=r
\]
all terms align and equality holds. For
\[
r>0,
\]
the equality condition in
\[
|1-z|\ge1-r
\]
makes this point unique.

The profile is strictly increasing, so its limit at
\[
r=1
\]
is
\[
4A+2b+\frac32
=
2\alpha^2+2\alpha-\frac52.
\]

The difference from the boundary value factors exactly as
\[
(1-r)
\left[
A(3+r)+b(2+r)+\frac32(1+r)
\right].
\]

If a sequence is norm-extremizing, the profile forces
\[
|z_j|\to1
\]
and the positive
\[
A|w_j|^2
\]
term forces
\[
|w_j|\to2.
\]
Therefore
\[
\frac{1-|z_j|}{|1-z_j|}\to1,
\]
which implies
\[
z_j\to1.
\]

Representative numerical evaluations agree with the symbolic profile. No numerical search is used to establish the maximum, the norm, or the localization statement.
