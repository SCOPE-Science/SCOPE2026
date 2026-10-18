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

The accompanying `verification.py` uses SymPy to reconstruct three exact symbolic identities: the potential-gradient map, the weighted Hessian, and the diagonal half-integer Jacobian spectrum. It then runs 7,656 reproducible finite diagnostics with a fixed numerical seed, checking interior ascent, critical-boundary ascent, analytically constructed additional equilibria, and parameter-exterior potential descent.

The symbolic identities were checked successfully and the script printed `symbolic identities: 3; finite diagnostics: 7656 PASS`.

Universal orbit convergence, the complete finite fixed-point count, and strict potential ascent at the critical boundary are established analytically in `RESULT.md`. Numerical runs do not certify infinite-time behavior or exhaustive parameter coverage. The exact all-orbit convergence result is not independently audited.
