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
# Verification

The independently executable `verify.py` recomputes three exact symbolic identities with arbitrary symbolic parameters and numerically checks Lyapunov monotonicity on 36 qualifying traces and numerical integration on 12 further subthreshold traces. The run returned `symbolic identities: 3/3` and `finite solution traces: 48/48`. All implementation source code is embedded beside this document, without external local dependencies other than the publicly specified Python packages.

The proof rather than finite simulation establishes: global-in-time existence; derivative estimates and sublevel compactness on the periodic quotient; LaSalle invariance and connected omega-limit selection; the lift back to real position; the exact critical energy barrier; and the strict-below-threshold stable-manifold nullity. All assumptions are explicitly stated in `RESULT.md`. Numerical checks do not certify theorems about all trajectories, nor do they assert independent mathematical validation.
