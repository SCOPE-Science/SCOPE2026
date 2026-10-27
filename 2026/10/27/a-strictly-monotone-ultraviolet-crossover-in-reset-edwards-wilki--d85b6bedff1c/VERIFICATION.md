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
# Reproduction and scope

The manuscript proves the exact integral, strict monotonicity, and endpoint asymptotics analytically. Execute `python3 checker.py` (Python standard library only) to reproduce six deterministic quadrature values and the exact-rational nonmonotonic two-mode control. Quadrature does not prove monotonicity at untested parameter values; the likelihood-ratio argument in RESULT.md does. Boundary conditions are infinite-line with a sharp finite Fourier noise bandwidth and global resets. No independent audit has been performed.
