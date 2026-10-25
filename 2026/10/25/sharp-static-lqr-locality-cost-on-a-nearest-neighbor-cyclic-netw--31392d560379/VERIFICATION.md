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
# Reproducible checks

Execute `python check.py` with Python 3 and NumPy installed. The program recomputes the real Fourier/Riccati symbol, compares its coefficients to the transfer-law asymptotic, verifies stationary Lyapunov cost identities, checks stable truncated feedback, and compares discarded Fourier-tail energies on finite cyclic systems.

The following parts of the proof require analytical verification rather than finite computation: the exact completion-of-squares identity for arbitrary nonsymmetric matrices; the singularity-transfer statement for all integer Fourier coefficients; the uniform lower bound over all static feedbacks; and the fixed-radius thermodynamic limit. No independent audit was performed.
