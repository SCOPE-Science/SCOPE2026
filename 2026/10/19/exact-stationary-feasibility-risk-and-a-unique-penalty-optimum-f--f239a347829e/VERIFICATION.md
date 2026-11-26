---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the stationary feasibility theorem

Reproduce with Python 3 standard library using `python verify.py`. The program forms the affine state matrix and solves the six symmetric discrete Lyapunov equations by rational Gaussian elimination; it compares the exact feasibility risk, momentum variance and primal–dual covariance identity. It tests log-convexity and optimal-ratio brackets and runs four seeded second-moment simulations. The frozen record reports 1716 checks.

The analytical proof covers all \(0<\alpha<1\) and \(0<\beta/\eta<4/3\), with iid finite-variance zero-mean noise independent of the finite-second-moment initial state. The boundary and divergent side use the Schur polynomial and nondegeneracy of the noise/input and feasibility/output projections. The finite checks do not establish the parameter-wide theorem or priority.
