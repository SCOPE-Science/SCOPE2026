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

The boundary-condition derivation, secular determinant, zero-energy scattering nullity, and local series expansion were checked algebraically.

`verify_robin_interval.py` uses only the Python standard library. It works in a truncated formal power-series ring over exact Gaussian rationals, reconstructs the two Robin reflection factors and the propagation exponential, and confirms exact secular order one at nonresonant points and order three at representative resonant points with both same-sign and mixed-sign endpoint parameters. It also checks the affine zero mode and the invariant value \(g_0-N/2=-1/2\).

The finite replay is supplementary. The all-parameter statement follows from the exact determinant and the strict positivity of the resonant cubic coefficient proved in `RESULT.md`. Literature search incompleteness remains a novelty risk; this is not an independent audit.
