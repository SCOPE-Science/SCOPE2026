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
# Reproducibility and limits

Run `python verify.py` in the directory containing this document. The script uses only Python's standard library; its checked rational identities include the rank-one ADI residual Cayley factor, transformed scalar objective, derivative factor and a rational high-contrast witness. It also probes 3,204 positive shifts and checks the reported minimizers and sharp ratio against numerical evaluations. A successful run reports 3,722 exact-rational and numerical checks.

The universal results are established by the derivative sign proof in `RESULT.md`. Finite grid probes cannot verify global optimality, an exact parameter-uniform bifurcation or an infinite limit. Publication priority is not independently certified, and the result is restricted to the explicitly stated rank-one, balanced-two-mode, first-step, real-shift domain.
