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

For \(k=1,2,3,4\) and several positive widths, the standalone Python checker forms Fock localization matrices from direct incomplete-gamma polar quadrature over an eccentric annulus. The computation independently checks the analytic tie, isolation of the two top monomials, directional perturbation and off-diagonal derivative. The checker passed 92 deterministic assertions as run with Python 3, NumPy and SciPy.

The computation uses finite matrices and finite angular grids; it does not certify the full spectrum, prove the infinite-dimensional perturbation remainder, or rule out prior publication. Those steps are supplied analytically in RESULT.md or identified as historical-priority limitations. Independent mathematical validation has not been performed.
