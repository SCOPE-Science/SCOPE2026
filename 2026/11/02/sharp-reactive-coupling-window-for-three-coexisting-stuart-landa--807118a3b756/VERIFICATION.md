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

# Reproducibility

Run `python check.py` with Python 3, SymPy and NumPy installed. The program builds the full real six-by-six co-rotating splay Jacobians directly for both chiralities and checks the exact characteristic polynomial; builds the independently derived synchronous Jacobian; checks the complex crossing and growth-interval algebra; and tests eight representative full-Jacobian spectral signatures.

The analytical proof in `RESULT.md` supplies the global quantifiers, orbital normal-hyperbolicity inference, uniqueness of imaginary-axis crossing, strict inequalities and exclusion of marginal boundaries. The numerical eigenspectra are consistency tests only. They are not used as proof of stability for every parameter value. A separate independent audit has not been performed.
