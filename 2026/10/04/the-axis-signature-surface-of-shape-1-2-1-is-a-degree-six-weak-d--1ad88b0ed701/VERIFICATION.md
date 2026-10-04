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

Run `python verify_axis_surface.py` with Python and SymPy. The script works over exact rational arithmetic and prints `VERIFY_OK` on success.

It verifies the following finite symbolic claims:

- the seven cubic parametrizing forms and their nine elimination relations;
- exact Gröbner elimination from the graph ideal;
- the local reduction on \(x_0=1\) to \(x_1x_4-x_2^2=0\);
- the local reduction on \(x_1=1\) to \(x_0x_3-(1+x_2)^3=0\);
- the smooth affine-plane description on \(x_6=1\) and the symmetry covering the \(x_4=1\) chart;
- Jacobian ranks at the two singular points;
- the self-intersections, mutual intersections, and anticanonical degrees of the three contracted \((-2)\)-curves.

The script does not prove a literature-negative statement. Originality is assessed separately from exact searches and source inspection. The geometric assertion that the three-step principalization of \((b,v^3)\) is the stated blow-up chain is also proved directly in `RESULT.md`; the script checks its intersection-theoretic consequences rather than using an external surface-classification package.
