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
The verified claim has two layers.

First, for a symmetric Minkowski plane, the full definition
\[
H_2(X)=
\sup
\frac{\sqrt{1+\lambda^2}}{\|x+\lambda y\|}
\]
is reduced using the inspected classification of unit isosceles-orthogonal pairs:
\[
y=\pm Rx.
\]
The inspected parameter-reduction proposition permits \(0<\lambda\le1\). Writing \(\lambda=\tan\theta\) gives
\[
x+\lambda Rx=\sec\theta\,Q_\theta x,
\]
so the quotient is exactly \(1/\|Q_\theta x\|\), and its unit-sphere supremum is the norm of the inverse rotation. Axis reflection conjugates positive and negative rotations, giving the stated operator-norm identity.

Second, for an affine regular \(4n\)-gon, linear isometry reduces to the Euclidean regular model with inradius \(1\). Its vertices have Euclidean radius
\[
\sec\left(\frac{\pi}{4n}\right)
\]
and lie halfway between adjacent support-normal directions. A convex function reaches its maximum on a polygon at a vertex; rotational symmetry makes all vertices equivalent. Rotating a vertex changes its norm by the factor
\[
\frac{\cos d}{\cos(\pi/(4n))}
\]
with \(0\le d\le\pi/(4n)\). This is at most the claimed secant and is equal to it when the rotated vertex lies on a support-normal direction.

No numerical sampling, finite enumeration, or external computation is used to prove the all-\(n\) result. The checks \(n=1\) and \(n=2\) are consistency specializations only, not proof of the general statement.

No independent audit or independent validation has been performed.
