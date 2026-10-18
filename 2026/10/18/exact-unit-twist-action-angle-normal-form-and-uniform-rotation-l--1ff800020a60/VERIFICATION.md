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

# Reproduction
Execute `python verify.py` with Python 3, SymPy, and mpmath. The checker exactly simplifies the first-integral identity, the invariant logarithmic-area Jacobian, and the Lie/Hamiltonian correspondence. It independently integrates logarithmic vertical chord lengths over four elliptic regions and compares them at high precision with the derived canonical action area; six independent Riccati time integrals check the signed angular rotation.

The analytical proof of the global chart, its area law, and exact unit twist is in `RESULT.md`. Numerical integration and finite parameter checks do not constitute verification for all parameters. The 2015 full primary exposition supplies the Lie/Riccati conjugation; the 2004 original article's full text could not be inspected for historical-priority purposes.
