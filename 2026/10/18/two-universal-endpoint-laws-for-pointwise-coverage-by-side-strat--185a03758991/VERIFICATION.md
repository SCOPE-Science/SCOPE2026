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

# Verification information

Run `python3 checker.py` with a Python 3 interpreter. The file has no third-party software dependencies, uses a fixed pseudorandom seed, and separately computes geometric containment by oriented-edge determinants, the closed corner expression, the wedge expression, and numerical integrations of depth-level sets.

On the reviewed source package the checks passed: 3000 wedge/corner depth comparisons; 330000 four-side convex-hull containment trials including affine transformation equivalence; boundary/center tests; and three finite quadrature levels for each endpoint. The observed normalized lower-end ratios were approximately 2.8546, 3.0708, 3.2149 for \(\varepsilon=\exp(-8),\exp(-12),\exp(-16)\), approaching the proved limit 4 slowly. The upper-end ratios were approximately 0.82378, 0.80759, 0.79533 for \(\varepsilon=0.015,0.005,0.001\), approaching the proved \(\pi/4\). These checks are numerical approximations and sampling experiments; the exact inequalities and limiting coefficients depend on the symbolic proof in `RESULT.md`.

Independent mathematical audit: not performed. No mechanized infinite proof or external certificate is asserted.
