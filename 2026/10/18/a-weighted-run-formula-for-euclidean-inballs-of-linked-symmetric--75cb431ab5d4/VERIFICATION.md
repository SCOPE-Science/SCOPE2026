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

The analytic certificate consists of the original facet normals, their exact Euclidean lengths, directed-path telescoping barriers, and the explicit attaining potential \(L_i\). These establish the theorem in every dimension without numerical extrapolation.

The included `verify.py` builds the source's original coordinate-and-suffix inequalities independently, solves the Chebyshev linear program using SciPy HiGHS, and checks containment of the constructive center. Execution of `python verify.py` passed 1,023 orientation words over dimensions 1–10, covering 36,868 shifted linear inequalities. It also checked 72 binary vertex transformations for the paired unimodular families in dimensions 4–9. Dependencies: Python 3, NumPy, SciPy. The numeric tolerances are \(10^{-7}\) for radii and \(10^{-8}\) for center containment.

The finite tests cannot certify the infinite family; the universal proof is in `RESULT.md`. No external audit, formal proof-assistant certification, or separate expert validation has been performed.
