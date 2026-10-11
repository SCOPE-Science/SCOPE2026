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
Put
\[
r=\frac{\sqrt5-1}{2}.
\]
The primal unit ball has ten vertices and the dual signed facet set has ten elements. For every ordered signed-facet pair \((f,g)\), the exact certificate checks
\[
\|f+rg\|_*+\|f-rg\|_*\le3-r.
\]
After cyclic reduction there are six possible values, and the maximum is attained at separations two and three.

The resulting chord envelope is
\[
0\le A,B\le2,
\qquad
A+rB\le3-r,
\qquad
rA+B\le3-r.
\]
Its six vertices are
\[
(0,0),\ (2,0),\ (2,r),\ (2\sqrt5-3,2\sqrt5-3),\ (r,2),\ (0,2).
\]
For
\[
Q(A,B)=A^2+B^2-\frac r2AB,
\]
the bundled checker verifies exact vertex values and the central value
\[
Q(2\sqrt5-3,2\sqrt5-3)=\frac{321-137\sqrt5}{4}<4.
\]
Thus \(Q\le4\) on the whole envelope by convexity. The explicit pair \(x=(1,0)\), \(y=(0,1)\) has chord pair \((2,r)\) and attains \(S_P=r/4\).

The bundled `verify.py` uses exact rational arithmetic in \(\mathbb Q(\sqrt5)\). It checks all one hundred ordered signed-facet pairs and all six envelope vertices; no numerical sampling is used for correctness.

No independent audit or independent validation has been performed.
