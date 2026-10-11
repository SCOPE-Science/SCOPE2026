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

For width \(1\), put
\[
t=\frac{\pi}{2n},
\qquad
R=\frac1{2\cos t}.
\]
One Reuleaux circular segment is a unit sector of half-angle \(t\) minus the triangle joining the arc center to the two arc endpoints.

The verifier reconstructs exactly:
\[
\operatorname{area}(S)=t,
\qquad
\int_S\|y\|_2^2\,dy=\frac t2,
\qquad
\int_S y_1\,dy=\frac{2\sin t}{3},
\]
and the corresponding triangle moments used in `RESULT.md`.

After translating the segment to an arc center at \((-R,0)\), it adds the exact polar moment of one radial triangle of the generating regular polygon and simplifies the \(n\)-fold sum to
\[
\frac1{16}
\left[
2\pi(3+\tan^2t)
-
n\tan t(11+\tan^2t)
\right].
\]

The script separately checks the area formula, the covariance normalization, and the expansions of the raw moment and squared isotropic constant.

A numerical radial integration is included only as a regression test. It is not used as proof of the all-\(n\) statement.
