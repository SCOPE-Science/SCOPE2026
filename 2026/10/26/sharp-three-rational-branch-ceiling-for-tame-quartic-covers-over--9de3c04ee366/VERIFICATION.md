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

# Verification instructions

Use Python 3 for the standard-library checks and install SymPy for the independent symbolic check. From the directory containing this file run:

```
python verify_fibers.py
python verify_orbits.py
python verify_symbolic.py
```

The first checker factors binary quartic forms using a direct finite-field polynomial-division routine, enumerates the 17,496 normalized coprime pairs, bounds possible rational ramification by Riemann–Hurwitz, and checks the nonrational cubic Wronskian residual. The orbit checker substitutes all 24 source and 24 target projective transformations, verifies five disjoint orbits of sizes 288, 288, 72, 24, 192, and verifies their union against the accepted equality set. The symbolic checker independently uses SymPy's finite-field factorization and Wronskian factorization; the outputs match. `checks.txt` records the actual replay output.

All enumerations are exact finite computations. Monodromy uses the standard tame-inertia generation theorem, not a monodromy package. No independent external validation has been performed. The result does not concern degree-four covers over fields other than the specified field.
