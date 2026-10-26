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

# Reproducibility

Run `python verify_ssh.py` after installing `requirements.txt`. The script independently solves continuous-time Lyapunov equations for the true generator, computes numerical residuals, performs exact symbolic independent matrix solutions for chains of lengths 2, 4 and 6, and tests the weak-coupling spectral ratio. Recorded: PASS 276 checks; worst relative numerical discrepancy 4.26e-10. The analytical proof extends to all positive parameters and integers and is not based on finite enumeration.

The strong-loss Schur-complement expansion is justified for fixed finite size with simple eigenvalues; no uniform asymptotic in chain length is asserted. Published-literature comparison remains subject to normal historical priority uncertainty.
