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

The standalone checker `artifacts/verify.py` reconstructs the exact complex from the three published facet-orbit representatives and the four published generators of the action \(12^{13}\). It verifies that the generated group has order \(24\), that the facet orbits have sizes \(24,12,12\), and that the resulting face vector is \((12,60,96,48)\).

Over \(\mathbf F_2\), it verifies rank \(48\) for the triangle cocycle equations and rank \(11\) for vertex coboundaries, giving one-dimensional first cohomology. It then enumerates all \(2048\) representatives of the unique nonzero class. The verified support-weight distribution is

\[
60t^{21}+132t^{23}+144t^{25}+240t^{27}+360t^{29}+408t^{31}+400t^{33}+240t^{35}+60t^{37}+4t^{39}.
\]

The checker verifies exactly \(60\) weight-\(21\) representatives and automorphism-orbit sizes \(12,24,24\). For every minimum cocycle it constructs the canonical local normal disk in each tetrahedron, checks face compatibility, checks connectedness, and computes Euler characteristic \(1\). The normal-disk profiles are \(18\) triangles with \(11\) quadrilaterals for \(24\) minima, and \(20\) triangles with \(10\) quadrilaterals for \(36\) minima.

The finite checker establishes the exhaustive statements about binary cocycles and their canonical normal representatives. The separate proof in `RESULT.md` is needed for the lower bound on an arbitrary embedded normal projective plane, since such a surface may meet an edge more than once.
