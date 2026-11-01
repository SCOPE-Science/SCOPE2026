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

# Reproduction and limits

Run `python3 verify_cube_tail.py` with NumPy and SciPy installed. The program is standalone and requires no input data. It constructs all twelve cube edges, computes their intersections with generic central planes, and takes planar convex hull areas; this is separate from the convolution-based proof. It compares 1,958 nondegenerate orientations, checking areas and vertex counts; the maximum absolute discrepancy is below \(5\times10^{-15}\). It checks two limiting angular integrals and their exact formulas. It also independently integrates finite-tolerance Haar areas for six tolerances and confirms convergence of the joint quadratic constants and conditional polygon split. The script ends in `PASS: independent checks`.

The analytic proof supplies universal statements and \(O(\varepsilon^3)\) error; numerical tests alone could not. No independent mathematical audit is reported. Calculations are reproducible to usual floating-point tolerance, but quadrature roundoff is not a certified rational enclosure.
