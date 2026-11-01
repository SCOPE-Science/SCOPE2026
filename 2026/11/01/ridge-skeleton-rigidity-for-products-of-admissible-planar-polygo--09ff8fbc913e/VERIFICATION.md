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

# Verification details

A complete analytic proof, with all quantifiers, appears in `RESULT.md`. Direct product-face enumeration gives the relevant codimension-two coefficient. The planar area and perimeter lower bounds are explicitly attributed to published theorems, and the tangent-triangle bound follows from a separate Jensen argument. A triangle times the unit interval gives an exact sharpness witness for the uniform triangular penalty.

The standalone `verify.py` (Python 3 standard library) was executed and reported `PASS: 884 Cartesian products of regular tangent triangles, squares and unit intervals`. Its exact geometric inputs are an inradius-one equilateral triangle (area \(3\sqrt3\), perimeter \(6\sqrt3\), three vertices), a centered square (area \(4\), perimeter \(8\), four vertices), and the centered length-two interval. It compares the product-face polynomial's ridge coefficient to the claimed lower bound. The resulting sharp triangular-prism edge-length excess was \(2.784609690826528\) to displayed floating-point accuracy, agreeing with \(12\sqrt3-18\).

The numerical test does not exhaust all polygons or dimensions and is not presented as a proof of the universal claim. The full proof uses positive coefficient expansion and Jensen's strict convexity. Independent audit and independent validation have not been performed.
