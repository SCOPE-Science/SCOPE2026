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

The public `RESULT.md` gives the equations, parameter ranges, the positive replacement root, exact algebra for the derivative, and the full comparison proof. `check.py` verifies the derivative symbolically after the positive root relation is substituted, evaluates a nontrivial equilibrium in exact rational arithmetic, and runs 1,000 deterministic exact rational assertions over 500 configurations. Run `python check.py` with Python 3 and SymPy installed. Tests are finite corroboration, not proof for arbitrary real parameters.

The strict averaged threshold only holds for strictly positive periodic solutions or compactly supported positive invariant probability measures. The global extinction theorem assumes a strict ceiling inequality and makes no assertion about the equality case. The source model adopts the fast-flower approximation. Earlier literature and supplemental technical material remain possible historical-priority limitations; no independent audit has yet been performed.
