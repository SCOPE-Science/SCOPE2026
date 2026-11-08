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

The supplied `check.py` executes the exact-symbolic derivative identities for all formal dimensions; it verifies positivity of the five Bernstein-coefficient polynomials, one-sign-change transforms and exact rational root brackets. Separately, it uses a convex hull's boundary triangulation and exact rational determinants to integrate first and second moments of 12 clipped cubes in dimensions 2–5. Terminal check output from the actual program was `CORNER_CUBE_ISOTROPY_CHECKS_PASSED 12 1270` and `BERNSTEIN_POSITIVE_CERTIFICATE 5 LOW_DIMENSION_DESCARTES {2: '++------', 3: '-----++++++', 4: '----------+++'}`. Reproduce with Python 3, SymPy, NumPy and SciPy using `python check.py`.

This is a transparent reproducibility check, not a separate mathematical or institutional certification. The infinite family is justified by the displayed symbolic positivity proof rather than by finite enumeration. Floating-point convex-hull triangulation supplies a combinatorial decomposition, while all nonzero simplex integrals and comparisons are exact rationals. No independent audit has been performed.
