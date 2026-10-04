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
The package verifies the exact deterministic quadratic stability law for source Positive-Negative Momentum.

`verify.py` reconstructs the source three-state modal matrix, compares its numerical characteristic roots with the closed cubic, tests both sides of the Schur boundary over randomized parameters, verifies the boundary root \(r=-1\), and checks the equivalent noise-amplification formula and default \(\beta_0=1\) value.

The numerical tests are transcription guards. The exact stability region is proved algebraically in `RESULT.md`.
