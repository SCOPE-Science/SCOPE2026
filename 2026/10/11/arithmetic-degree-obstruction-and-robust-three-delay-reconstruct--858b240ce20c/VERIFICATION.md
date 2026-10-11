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

The provided `checks/check_delay_degree.py` executes in Python with SymPy. Execute `python checks/check_delay_degree.py` from the package root; it symbolically checks the exact determinant identity and Cayley–Hamilton recurrence, evaluates the integer Smith normal form of the optimal observation matrix for \(2\le m\le19\), and tests integer observation rows on a stated finite grid. It was executed successfully before this file was packaged.

The finite tests do **not** establish the theorem over all parameters. Its exact universal statements follow from the cohomological degree formula, the integral row reduction, the invariance-of-domain argument, and the inverse-function-plus-covering argument in `RESULT.md`. In particular, the nonlinear homotopy-class impossibility and the persistence of a diffeomorphic delay map are proved analytically, not by simulation.

Scientific limits: three consecutive delays only; topological degree does not bound every fiber for a general nonlinear degree-zero map; small smooth perturbations only for the positive stability assertion; no independent external audit has been performed.
