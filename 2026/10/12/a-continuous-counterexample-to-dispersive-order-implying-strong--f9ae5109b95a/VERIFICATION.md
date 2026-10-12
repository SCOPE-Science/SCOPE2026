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

The two quantile functions have slopes
\[
(13,43,2,1,5)
\]
and
\[
(13,43,10,1,5),
\]
so both are strictly increasing. Their knotwise difference is
\[
\left(0,0,0,\frac85,\frac85,\frac85\right),
\]
and the difference is linear on each knot interval, hence globally nondecreasing.

For \(3/5\le p\le4/5\), exact integration gives
\[
\tau_X(p)
=
\frac{25p^2+143}{2(25p^2-25p+86)}
\]
and
\[
\tau_Y(p)
=
\frac{25p^2+183}{2(25p^2-25p+106)}.
\]
The exact substitutions are
\[
\tau_Y(3/5)=\frac{24}{25},
\qquad
\tau_X(79/115)=\frac{24}{25},
\qquad
\tau_X(4/5)=\frac{159}{164}.
\]
For \(v=159/164\), the \(Y\)-quantile coordinate solves
\[
-1925p^2+3975p-1848=0
\]
and the relevant root is
\[
p=\frac{159}{154}-\frac{\sqrt{62841}}{770}.
\]

The final gap comparison reduces to
\[
23\sqrt{62841}>5657,
\]
which follows from
\[
62841\cdot23^2-5657^2=1241240>0.
\]

The standalone `verify.py` checks all rational identities, the quadratic root in the exact quadratic field, the monotone quantile difference, and the square certificate.

Expected terminal line:
`VERIFY_OK u=24/25 v=159/164 square_margin=1241240`.

No finite computation is used to establish a universal statement beyond these exact symbolic identities.
