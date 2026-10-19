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
# Reproducibility and evidence

Run `python verify_gated.py` using Python 3 and SymPy. The exact rational program rebuilds each full vacancy/gate generator and the killed process for the next successful bond crossing. It checks normalization and positivity of stationary probabilities, equality of stationary crossing current with inverse renewal mean, first and second killed-process moments, and two independently obtained Laplace-transform values. Its recorded run reported `PASS: 96 independent rational generator/current/moment/Laplace identities, 24 parameter instances` for \(3\le n\le8\).

The program verifies finitely many parameter choices only. The infinite family of finite ring lengths and all positive parameters are established analytically in RESULT.md by conditioning and the strong Markov property. No independent external audit or independent validation has been performed.
