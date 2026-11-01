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

# Reproduction

Run `python3 checker.py` with Python 3 and the standard library; compare output to `checker_output.txt`. The recorded run returned 233 finite checks passed. Tests include eigenpair evaluation, normalization and orthogonality, direct two-step kernel checks, detailed balance, spectral regression, and numerical approximations to both exact total-variation constants.

# Limits of verification

The infinite spectral completeness follows analytically from the complete mixed Dirichlet–Neumann basis and unitary Doob conjugation. The TV asymptotics use the square-integrable transition density and Cauchy–Schwarz. A finite checker is not an exhaustive proof of those functional-analytic statements, and no independent audit is represented.
