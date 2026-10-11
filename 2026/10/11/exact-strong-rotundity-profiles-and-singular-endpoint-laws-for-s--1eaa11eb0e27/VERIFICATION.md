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
The local index is the distance between the affine support hyperplane \(H=f^{-1}(\{1\})\) and the ball points separated from \(x\) by at least \(\epsilon\). For \(z=(t,y)\in B_{X_p}\), the exact hyperplane distance is \(1-t\), attained by the comparison point \((1,y)\in H\).

For finite \(p\), the sharp slice bound is
\[
\sup_{\substack{z\in B_{X_p}\\f(z)\ge1-d}}\|z-x\|_p^p
=d^p+1-|1-d|^p,
\quad0\le d\le2.
\]
It follows by bounding the transverse coordinate norm with the unit-ball constraint and noting monotonicity in the scalar coordinate. The explicit contact vector is
\[
z_d=\left(1-d,\bigl(1-|1-d|^p\bigr)^{1/p}u\right),
\qquad\|u\|_Y=1.
\]
For finite \(p>1\), strict increase of the scalar envelope proves unique inversion. At \(p=1\), the envelope flattens for \(d\ge1\); at \(p=\infty\), it equals \(\max\{d,1\}\), accounting for different endpoint laws.

The packaged `verify.py` implements exact-rational and supplementary numerical checks. Its output certifies only its finite test coverage; the continuum theorem follows from the explicit analytic inequalities and attainment vectors in `RESULT.md`.

No independent audit or independent validation has been performed.
