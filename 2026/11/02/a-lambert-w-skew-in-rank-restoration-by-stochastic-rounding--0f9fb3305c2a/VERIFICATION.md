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

# Reproducibility and verification

The analytical proof in `RESULT.md` establishes the all-width fixed-column asymptotic theorem. `verify.py` requires only the Python 3 standard library and can be run with `python verify.py`. It checks finite hypercube hyperplanes, exact real ranks of enumerated binary matrices, the closed two-column law, finite three-column cases, and numerical diagnostics on the optimizers and Lambert-W approximation.

Exact computations use rational arithmetic. Floating-point tests are diagnostics only and do not establish infinite-dimensional, large-sample or global-optimality claims; those rely on the written analytic proof. No independent validation has been performed.
