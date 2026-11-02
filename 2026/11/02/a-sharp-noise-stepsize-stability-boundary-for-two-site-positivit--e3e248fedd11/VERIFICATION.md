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

`python3 verify.py` executes standard-library rational, deterministic numerical and seeded simulation checks of the theorem. The exact witness uses integer/rational second-moment matrix arithmetic; simulations are ancillary and cannot substitute for the proof of statements holding for all real model parameters and all times.

Bundled check output:

```
VERIFY_OK rational_witness=1 threshold_levels=9 curvature_factors=300 monte_carlo=120000
```

The independent review channel has no evidence. The numerical implementation has not been validated across floating-point platforms, and literature coverage is qualified by the stated specialist-priority risk.
