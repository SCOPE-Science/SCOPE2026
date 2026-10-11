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

The proof uses no numerical experiment.

After translating the critical point to the origin and subtracting its value, define
\[
g(x)=f(x)-\frac a2|x|^2.
\]
The hypothesis \(D^2f\ge aI_2\) gives
\[
D^2g\ge0,
\]
and the critical-point condition gives
\[
g(0)=0,
\qquad
Dg(0)=0.
\]
Thus \(g\) is convex and nonnegative.

On each unit ray,
\[
\phi(r)=f(r\theta)
\]
satisfies
\[
\phi'(r)\ge ar.
\]
For a shell interval \([r_0,r_1]\),
\[
\frac{r_1^2-r_0^2}{2}
\le
\frac{\phi(r_1)-\phi(r_0)}a
\le
\frac{\delta}{a}.
\]
Polar integration is exactly the integral of the left-hand side over \(S^1\).

If the global area equals \(2\pi\delta/a\), the directional deficit, being nonnegative, is zero almost everywhere. Hence
\[
\phi'(r)=ar
\]
through the shell on almost every ray. The one-variable remainder
\[
h(r)=\phi(r)-\frac a2r^2
\]
is convex with \(h'(0)=0\). Since \(h'\) is nondecreasing and vanishes later, it vanishes from the origin through the shell endpoint. Therefore
\[
\phi(r)=\frac a2r^2
\]
up to that endpoint.

The endpoint condition \(\phi(r_1)=c+\delta-f(x_*)\) fixes the same outer radius in every equality direction:
\[
r_1=
\sqrt{\frac{2(c+\delta-f(x_*))}{a}}.
\]
Continuity then fills the exceptional angular set and gives the entire disk.

For the converse, if the function is quadratic on that disk, the shell is exactly the annulus with squared-radius difference
\[
\frac{2\delta}{a},
\]
so its area is \(2\pi\delta/a\). Convexity of the quadratic remainder excludes additional shell points outside the disk.

The proved limits are exactly those stated: dimension two, \(C^2\) regularity, an interior critical point, and one shell with \(c>f(x_*)\).
