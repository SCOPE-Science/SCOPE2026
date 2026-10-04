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

The structural input is the published polygon theorem that characterizes homothetic illumination bodies by balanced \((k,l)\)-extensions. Its hypotheses are matched as follows:
\[
k,l\ge1,\qquad
k+l\ \text{even},\qquad
k+l+1<\frac m2.
\]
Writing
\[
q=k+l+1
\]
therefore gives exactly the odd indices
\[
3\le q<\frac m2.
\]

For a regular polygon of circumradius \(R\), the inradius is \(R\cos(\pi/m)\). Two sidelines whose outward normals differ by \(2q\pi/m\) intersect on their angular bisector at radius
\[
R\frac{\cos(\pi/m)}{\cos(q\pi/m)}.
\]
This verifies the homothety ratio and shows that every admissible balanced extension is a concentric regular polygon.

At one extension vertex, the two tangent vertices of the original polygon occur at angles
\[
\pm(q-1)\frac{\pi}{m}.
\]
Subtracting the intervening polygonal cap from the tangent triangle gives
\[
\delta
=
R^2
\left(
\mu\sin\!\left((q-1)\frac{\pi}{m}\right)
-
\frac{q-1}{2}\sin\!\left(\frac{2\pi}{m}\right)
\right).
\]
Substitution of
\[
\mu=\frac{\cos(\pi/m)}{\cos(q\pi/m)}
\]
reduces this exactly to
\[
\delta
=
R^2
\left(
\cos^2\!\left(\frac{\pi}{m}\right)
\tan\!\left(\frac{q\pi}{m}\right)
-
q\sin\!\left(\frac{\pi}{m}\right)
\cos\!\left(\frac{\pi}{m}\right)
\right).
\]

The embedded `verify.py` was replayed from its actual package path before packaging. It constructs convex hulls directly and checks all admissible indices for every \(3\le m\le60\), including five points on each predicted level edge. Its output was:

`VERIFY_OK regular polygon illumination spectrum m=3..60`

The finite replay is not used to prove completeness or the all-\(m\) formulas.
