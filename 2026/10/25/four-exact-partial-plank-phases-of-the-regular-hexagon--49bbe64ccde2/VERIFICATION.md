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

# Verification and reproducibility

Run `python verify_hexagon.py` from the directory containing the six research documents. It uses only Python 3's standard library, a fixed random seed and independently written Sutherland--Hodgman-style halfplane clipping, then computes shoelace area of the resulting polygons. It compares the geometric areas of \(12{,}050\) sampled competitor planks at \(1{,}205\) widths to the derived analytic cap formulas and piecewise exact optimum, and checks joining values at the three transition widths. A successful run prints three PASS/NOTE statements. This validation ran successfully in the preparation environment.

The **continuum proof** is in `RESULT.md`. Numerical sampling does not rule out an exceptional width or orientation and is not used to certify the theorem. Critical inequalities are explicitly factored in the proof, including derivative signs and the triangular stationary-point regime test. No independent external audit or machine-formal proof has been conducted.
