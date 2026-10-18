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

The full analytic proof is in RESULT.md. Run `python verify_discord.py` using the two named dependencies in `requirements.txt`. The verification program completed with `PASS 395 analytic and numerical assertions` on the provided code. It independently integrates the phase-state mixture at selected parameters, checks two-qubit state normalization and PPT, compares Pauli-correlation and geometric-discord expressions, and confirms exact symbolic factorization and sparse-limit optimization.

A finite set of parameters does not prove an all-parameter statement; the rank argument and exact spectral calculation are the proof. Ordinary entropic discord is established to be nonzero via the nonclassicality criterion but is not evaluated numerically or symbolically. All geometric-discord values use the unnormalized squared Hilbert--Schmidt convention in RESULT.md.
