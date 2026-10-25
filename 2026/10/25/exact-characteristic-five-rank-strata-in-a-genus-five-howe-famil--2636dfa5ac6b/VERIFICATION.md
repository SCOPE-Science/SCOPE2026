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

## Reproducible checks

`python verify_symbolic.py` requires SymPy and performs exact characteristic-five polynomial expansion, checks every pairwise ideal saturated by the admissibility discriminant, checks each irreducible degree-two parameter equation, and verifies the saturated ideal is the unit ideal for every three-factor combination. Its observed result is `SYMBOLIC_VERIFY_OK`.

`python verify_f25.py` uses only the Python standard library and an independent arithmetic implementation of the quadratic field of twenty-five elements. It verifies the three sample ranks, all ten exceptional factor pairs, the twenty/one-hundred-eighty/three-hundred-six distribution of ranks three/four/five, and prints `F25_VERIFY_OK`.

The algebraic completeness assertion rests on the proven saturated-ideal identity, not the finite-field enumeration. The characteristic-five geometry, Riemann–Hurwitz, semilinear-Cartier argument and Jacobian decomposition are presented in RESULT.md. No independent audit has been performed, and Newton polygons and isomorphism-class counts are outside scope.
