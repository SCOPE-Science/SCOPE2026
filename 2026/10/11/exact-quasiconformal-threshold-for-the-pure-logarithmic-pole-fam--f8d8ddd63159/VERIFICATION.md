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
w=\frac{z-p}{1-pz},
\qquad
c=(1-p^2)A,
\]
the pure logarithmic pole map is conformally equivalent to
\[
G_c(w)=\frac1w-c\log|w|.
\]

Direct differentiation gives
\[
(G_c)_w
=
-\frac1{w^2}-\frac{c}{2w},
\qquad
(G_c)_{\bar w}
=
-\frac{c}{2\bar w},
\]
and therefore
\[
J_{G_c}(w)
=
|w|^{-4}
(1+\operatorname{Re}(cw)).
\]
For
\[
|c|<1,
\]
this is strictly positive on the punctured disk.

For
\[
|w|=r,
\]
the image is the circle with center
\[
-c\log r
\]
and radius
\[
1/r.
\]
The strict nesting inequality
\[
|c|\log(r_2/r_1)
<
1/r_1-1/r_2
\]
for
\[
0<r_1<r_2\le1
\]
proves global injectivity and identifies the image as the exterior unit disk.

The Beltrami modulus is
\[
|\mu_{G_c}(w)|
=
\frac{|c||w|}
{2|1+(c/2)w|}.
\]
Its essential supremum is exactly
\[
\frac{|c|}{2-|c|}.
\]
No global extension can have a smaller coefficient because it must agree with
\[
G_c
\]
inside the disk.

The piecewise map
\[
\widehat G_c(w)
=
G_c(w)
\]
for
\[
|w|<1
\]
and
\[
\widehat G_c(w)=1/w
\]
for
\[
|w|\ge1
\]
is a sphere homeomorphism and is conformal outside. Hence the lower bound is attained.

Solving
\[
\frac{|c|}{2-|c|}
\le k
\]
gives
\[
|A|
\le
\frac{2k}
{(1+k)(1-p^2)}.
\]

All steps are exact. No numerical sampling, finite enumeration, or unproved certificate is used.
