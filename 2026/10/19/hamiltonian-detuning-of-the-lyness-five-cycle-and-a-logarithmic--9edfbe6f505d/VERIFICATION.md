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

The accompanying `verify.py` is executed from the same directory as this document and checks (using SymPy) the rational five-iterate identity at the resonant parameter, the exact parameter derivative and its equality to the invariant Hamiltonian vector field, preservation of the first integral and log-area form, the critical level value, the Hessian determinant and the tropical polygon area. The checker also checks the centered linear rotation derivative for three decreasing nonzero perturbations. The recorded result is `VERIFY_OK`.

The all-level rotation derivative follows from the proof's moving-oval conjugation and translation-number bound. The high-energy period result follows analytically from tropical comparison, concavity and coarea, not from the checker. Historical priority and independent audit have not been certified.
