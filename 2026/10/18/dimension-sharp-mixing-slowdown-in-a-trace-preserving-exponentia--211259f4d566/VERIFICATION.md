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

# Reproducibility and scope

Run `python checker.py` with SymPy, NumPy and SciPy. It performs 341 exact symbolic identities and numerical consistency assertions for direct finite-dimensional Lindblad superoperators, exact matrix exponentials, threshold factorization, long-step asymptotics, and the sharp density-state trace-distance witnesses. Tests cover finitely many dimensions and step values; arbitrary dimensions and positive step sizes are proved analytically in `RESULT.md`. No outside certification or independent audit was performed.
