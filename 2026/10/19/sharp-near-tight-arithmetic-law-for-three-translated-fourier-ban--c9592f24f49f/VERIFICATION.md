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

# Reproducible checks and limits
Run `python verify.py` with Python 3 and NumPy. The script confirms exact tight cases for selected \(n\equiv2\pmod3\), evaluates the proposed asymptotically optimal shifts on both other congruence classes, checks the linearized Hermitian spectral diameter, and samples the convexity-based minimax bound. Its successful marker is `VERIFY_OK`. The mathematical limit for every integer \(n\) is proved in `RESULT.md`, not certified by finite tests. No independent audit has been performed.
