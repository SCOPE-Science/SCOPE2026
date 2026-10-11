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

The analytic reduction is
\[
d_K(u)w_K(u^\perp)
=
4\rho_{(K-K)/2}(u)
h_{(K-K)/2}(u^\perp).
\]
For a regular centrally symmetric \(N\)-gon of circumradius \(R\), put
\[
a=\frac{\pi}{N}.
\]
Within one edge-normal chamber,
\[
\rho(\theta)=\frac{R\cos a}{\cos\theta},
\qquad
0\le\theta\le a.
\]

If
\[
N\equiv2\pmod4,
\]
then
\[
h(\theta+\pi/2)=R\cos\theta
\]
and the chord-width product is exactly
\[
4R^2\cos a.
\]

If
\[
N\equiv0\pmod4,
\]
then
\[
h(\theta+\pi/2)=R\cos(a-\theta)
\]
and the product is
\[
4R^2\cos a\,
\frac{\cos(a-\theta)}{\cos\theta},
\]
which increases from
\[
4R^2\cos^2a
\]
to
\[
4R^2.
\]

For odd \(m\), the central symmetral is a regular \(2m\)-gon with
\[
R=\cos\frac{\pi}{2m},
\]
so the first branch applies.

`verify.py` independently constructs the polygons from vertices, computes the convex hull of all half-differences, derives radial values from hull edges, and samples the chord-width product. It compares the result with the closed forms for \(3\le m\le40\) and checks the three published small values.

The finite sweep is diagnostic only. No finite sampling is used to establish the all-\(m\) theorem.
