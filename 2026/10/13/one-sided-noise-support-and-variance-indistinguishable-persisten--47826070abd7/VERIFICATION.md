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

# Reproducible checks and boundaries

Run `python3 verify.py` with standard Python (no external packages). The script checks exact rational invariance for the positive Bernoulli-shock interval, its uniform contraction factor, the three signs of the quartic formal closure, and the explicit bound on trap-failure probabilities. Expected output: `VERIFY_OK`.

The assertion that every finite trajectory with unbounded-below finite-variance shocks tends to negative infinity is proved using an infinite union bound and martingale convergence, not by finite computation. The uniqueness assertion concerns invariant probability measures supported inside the compact positive invariant interval; uniqueness over the complete real state space is not claimed for bounded noise. No external audit or independent validation was performed.
