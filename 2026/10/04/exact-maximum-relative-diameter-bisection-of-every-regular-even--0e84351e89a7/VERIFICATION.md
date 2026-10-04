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

The proof was checked from the stated hypotheses without numerical approximation.

Let
\[
\alpha=\frac{\pi}{n},\qquad
a=R\cos\alpha,\qquad
b=R\sin\alpha.
\]
For a center-passing line, take one boundary endpoint as \(x=(a,t)\) with \(-b\le t\le b\). The opposite endpoint is \(-x\).

The published centrally symmetric-body reduction ensures that minimizing over such center-passing lines gives the same infimum as minimizing over all bisection curves.

For any polygon vertex \(v\) on the circumcircle,
\[
\|x-v\|^2=\|x\|^2+R^2-2x\cdot v.
\]
The vertices minimizing \(x\cdot v\) are the two vertices that bracket the antipodal direction \(-x\), namely \((-a,b)\) and \((-a,-b)\). Their squared distances are
\[
4a^2+(t-b)^2
\quad\text{and}\quad
4a^2+(t+b)^2.
\]
Therefore
\[
d_M^2=4a^2+(b+|t|)^2,
\]
which is strictly minimized at \(t=0\). This yields
\[
d_M^2=4R^2\cos^2\alpha+R^2\sin^2\alpha
=R^2\left(4-3\sin^2\alpha\right).
\]

For \(n=6\), the result is \(\sqrt{13}\,R/2\), matching the published regular-hexagon computation. For \(n=4\), it equals \(\sqrt5/2\) times the square side length.

The verification does not claim uniqueness among arbitrary curved minimizing bisections; it proves uniqueness only within the center-passing straight-line class, which is enough for the exact global minimum value.
