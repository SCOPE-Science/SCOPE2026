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

The proof was reconstructed from the stated hypotheses and checked without numerical approximation.

For a regular even \(n\)-gon of circumradius \(R\), set
\[
a=R\cos\!\left(\frac{\pi}{n}\right),\qquad
b=R\sin\!\left(\frac{\pi}{n}\right).
\]
A half-perimeter boundary chain starting at \((t,a)\) ends at its antipode and contains the two left endpoints \((-b,a)\) and \((-b,-a)\). Its diameter is therefore at least
\[
\sqrt{4a^2+(b+|t|)^2},
\]
so any covering disk has radius at least
\[
\sqrt{a^2+\frac{b^2}{4}}.
\]
Equality in this lower bound forces \(t=0\).

For the midpoint cut, the proposed left center is \((-b/2,0)\). Every original left-side vertex \((u,v)\) satisfies
\[
u^2+v^2=R^2,\qquad u\le-b,
\]
and hence
\[
\left(u+\frac b2\right)^2+v^2
=R^2+bu+\frac{b^2}{4}
\le
R^2-\frac{3b^2}{4}.
\]
Thus the proposed disk contains all vertices of the half-polygon and, by convexity, the whole half-polygon.

The two endpoint-crossing pairs in an optimal half-chain each have distance twice the claimed radius and the same midpoint, forcing the disk center. If an assigned boundary chain were longer than half the perimeter, it would contain half-perimeter windows with non-midpoint starts and would violate the strict lower bound. This verifies the equality classification.

Sanity checks give \(\sqrt5/4\) for a unit square and \(\sqrt{13}\,R/4\) for a regular hexagon of circumradius \(R\).

The proof does not establish any corresponding formula for regular odd polygons or for more than two disks.
