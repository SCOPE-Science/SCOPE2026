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

The new claim was checked in exact arithmetic.

The calculation uses the affine pentagon model from `RESULT.md`, the exact difference body \(D=(C-C)/2\), and the six cyclic boundary parameters
\[
0,\quad \frac34,\quad \frac{15-\sqrt5}{8},\quad \frac52,\quad
\frac{25+\sqrt5}{8},\quad \frac{17}{4}.
\]
For every consecutive side vector \(Z_i\), `verify.py` checks symbolically that
\[
\frac{Z_i}{3(\sqrt5-1)/4}
\]
is exactly a listed vertex or convex combination of adjacent vertices of \(D\). Hence each normalized side lies on \(\partial D\), which proves the six equal relative distances.

The same checker verifies the exact simplification
\[
\frac{d}{2+d}=3-\frac{6\sqrt5}{5}.
\]

The universal statement over all relatively equilateral hexagons containing the prescribed vertex uses the primary source's common-vertex equal-length observation for \(k\ge4\); the source passage was materially inspected.

No finite sampling is used to establish an infinite or universal claim. The theorem does not determine the global value \(d_C(6)\).
