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

The executable `verify.py` reconstructs the energy matrices by symbolic differentiation/integration, and checks the two exact rational threshold identities including the explicit positive polynomial certificate. It additionally checks 40 exact rational cut/weight pairs for the strict spectral matrix inequality at the uniform threshold. The symbolic identities and sign positivity prove the continuum statement; finite samples only guard transcription and implementation. Python with SymPy is required. No independent review was carried out.
