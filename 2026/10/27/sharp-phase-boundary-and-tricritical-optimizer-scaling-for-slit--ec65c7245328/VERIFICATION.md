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

# Verification and scope

The mathematical proof is in `RESULT.md`. The runnable file `verification/check.py` verifies the exact rational plateau identity, the derivative sign polynomial, the reciprocal-time expansion, and the exact finite plateau-tie identity in the discontinuous numerical example, using SymPy simplification. It prints the two critical prefactors and the finite coexistence quantities. All symbolic checks completed successfully in the supplied execution environment. The compactness/global-optimization arguments and asymptotic deductions are proved in text, not inferred from numerical sampling.

The exact result applies to the rational four-direction model with \(a>0,r>0,\eta\ge1,b\ge0\), not to a continuous-angle stochastic process. No independent audit or experimental validation has been performed.
