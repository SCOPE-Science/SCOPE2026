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
# Verification record

The embedded `check.py` is a standalone, locally executable diagnostic. Running `python check.py` with NumPy and SciPy performed 2,000 vector-field cross-checks, 12 direct-ODE trajectory checks of invariant quantities, three parameter-pair critical coefficient/scaling checks, and five finite midpoint-quadrature tests of the conditional Haar period tail. All of these completed successfully on the preserved source code. The derived algebraic formulas, Morse classification, and coarea integrability argument are mathematical proofs and do not depend on sampling.

No numerical experiment was used to assert that all parameter values or all initial phases were exhaustively enumerated. No independent external mathematical audit has been performed. The 2018 SIAM article was inspected through a lawful institutional text copy of the relevant sections, but this does not establish universal historical priority against every earlier paper.
