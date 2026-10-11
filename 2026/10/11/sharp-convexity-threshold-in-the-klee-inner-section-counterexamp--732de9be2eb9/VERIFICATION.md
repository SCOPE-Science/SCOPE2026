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

For
\[
r(\phi)
=
\left(1+\varepsilon\cos^3\phi\right)^{-1/3},
\]
symbolic differentiation gives
\[
r^2+2(r')^2-r r''
=
\frac{
1+2\varepsilon\cos\phi-\varepsilon\cos^3\phi
}{
\left(1+\varepsilon\cos^3\phi\right)^{8/3}
}.
\]
Because the denominator is positive for
\[
0\le\varepsilon<1,
\]
the sign is determined by
\[
1+\varepsilon(2c-c^3),
\qquad c\in[-1,1].
\]

The derivative of
\[
g(c)=2c-c^3
\]
is
\[
g'(c)=2-3c^2,
\]
so its unique minimum is attained at
\[
c=-\sqrt{\frac23}
\]
with value
\[
-\frac{4\sqrt6}{9}.
\]
Therefore the exact nonnegative-curvature condition is
\[
1-\frac{4\sqrt6}{9}\varepsilon\ge0,
\]
equivalently
\[
\varepsilon\le\frac{3\sqrt6}{8}.
\]

`verify.py` symbolically replays the curvature factorization and critical-point calculation and checks nearby decimal parameters. The decimal checks are diagnostic only and are not used as proof.

At the endpoint, convexity is obtained as a Hausdorff limit of strictly convex members from below. The verification does not claim that later, separate estimates in the original inner-section construction remain valid up to the same endpoint.
