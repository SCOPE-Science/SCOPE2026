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

Run `python checker.py` with Python 3.9+ (standard library only). It checks nine finite graph common-kernel calculations using rational incidence nullspaces, centered energy cancellation and bipartite edge-average cancellation, followed by the exact periodic 4-by-6 checkerboard negative-Laplacian eigenvalue 208 for spacing 1/4 by 1/6. Passing verifies the algebraic test fixtures only. The cycle-space, parity and Cauchy–Schwarz steps in RESULT.md establish the infinite families. No third-party numerical package or external solver is needed. Floating-point stability, smooth velocity-realizability of every circulation and physical mixing-rate predictions are unproved.
