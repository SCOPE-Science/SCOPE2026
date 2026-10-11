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

The accompanying `verify.py` is a self-contained Python/SymPy script; `requirements.txt` records its external mathematical dependency. Run `python verify.py` in a clean directory containing both files after installing the stated dependency.

The checker tests the equilibrium-elimination identity and all four stationary equations, exact quadratic and linear coefficient expansions, the delicate positive-factor polynomial identity, the derivative formula for the scalar equation, and the two independent-feedback derivative factorizations. It additionally checks 80 exact-rational parameter choices using 110 rational bisection steps each, covering \(\sigma=0\) and \(\sigma=1\), zero feedback, unequal feedback, and relatively high feedback. Expected terminal lines are:

```
EXACT_SYMBOLIC_IDENTITIES=11
EXACT_RATIONAL_CASES= 80
ALL_CHECKS_PASS
```

The machine checks verify exact symbolic identities and finite parameter examples, not independently that every term is positive over every allowed parameter value. The universal inequalities are proved algebraically in RESULT.md by (2)–(4). The global dynamical stability or numerical forecasting performance of the ODE is not covered. Independent audit and independent experimental validation have not been performed.
