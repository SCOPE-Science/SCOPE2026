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

# Reproducibility and boundaries

Execute `python3 verify_runs_bridge.py` using a standard Python installation; no nonstandard dependencies or external papers are required to rerun finite checks.

Observed exact-arithmetic report: `PASS: 1587 exact assertions; 144392 conditional-enumeration word instances; 49 unbalanced/balanced profiles.`

The script tests the arbitrary fixed-count conditional regression across small finite configurations, balanced conditional and covariance identities, monotone powers, and strict empirical one-Wasserstein covariance for deterministic strictly increasing pooled point sets. Its finite enumeration is not an infinite proof. Equations (5), (6), and the fourth-moment calculation in RESULT.md justify all dimensions analytically. The Wasserstein statement assumes no ties and a finite first parent moment; the strict all-distribution sign is derived from conditioning, not from numerical experiments.

Independent audit and independent validation have not been performed.
