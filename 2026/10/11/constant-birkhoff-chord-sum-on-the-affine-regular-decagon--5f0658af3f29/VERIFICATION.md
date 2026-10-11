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
Let
\[
r=\frac{\sqrt5-1}{2},
\qquad
\phi=\frac{1+\sqrt5}{2},
\qquad
c=\frac{3\sqrt5-1}{4}.
\]
The algebraic identities used in the proof are
\[
r\phi=1,
\qquad
r^2=1-r,
\qquad
2r+\phi=2c.
\]

After dihedral reduction, an edge-interior Birkhoff pair is
\[
x=(a,1-a),
\qquad
y=(\phi,-\phi),
\qquad
0<a<1,
\]
and its two chord norms are
\[
2r+r^2a
\quad\text{and}\quad
\phi-r^2a.
\]

At the reference vertex, every admissible Birkhoff direction is
\[
x=(1,0),
\qquad
y=(1+r\theta,-\phi),
\qquad
0\le\theta\le1,
\]
up to sign, and the two chord norms are
\[
2r+r^2\theta
\quad\text{and}\quad
\phi-r^2\theta.
\]

Thus every admissible chord pair has sum \(2c\), and the balanced parameter \(1/2\) attains both coordinates at \(c\).

The bundled `verify.py` checks these identities in exact arithmetic in \(\mathbb Q(\sqrt5)\), verifies the decagon vertices and symmetry generators, and replays both formula families on exact rational grids. The grids are supplementary; the analytic edge/vertex dichotomy proves exhaustiveness.

No independent audit or independent validation has been performed.
