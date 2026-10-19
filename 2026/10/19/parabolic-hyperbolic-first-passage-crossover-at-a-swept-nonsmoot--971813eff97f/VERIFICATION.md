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

# Verification of the first-passage crossover

The exact-algebra portion of `verify_crossover.py` uses rational arithmetic for four values of the contracting slope, three values of the repelling excess and trajectory indices from negative time through forty positive steps. It checks the prescribed switch and the finite geometric-sum equality.

The floating-point portion independently iterates the state, obtains the positive crossing without using a closed-form solution, and compares the first passage with numerical inversion of the explicit integral at five crossover parameters and five sweep rates. It also reports the normalized logarithmic error along two near-neutral hyperbolic parameter paths. Both portions completed without assertion failures.

Run `python verify_crossover.py` with Python 3. The exact recurrence and analytical bracketing in `RESULT.md` provide the mathematical proof. Finite trajectory tests do not prove an asymptotic limit, and the implementation does not validate perturbed nonlinear maps or other observation thresholds.
