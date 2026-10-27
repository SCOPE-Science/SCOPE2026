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

# Reproducible numerical and symbolic checks

Run `python verify_pupil.py` in a Python environment with NumPy and SymPy. Observed result: `PASS: symbolic 2x2 identity, exact-rational two-mode witness, 480 seeded Fourier cases`. The checker independently forms the saddle and preconditioner matrices, verifies the block identity, idempotence, strict two-frequency rational witness, right-preconditioned residual formula, retained-mode reconstruction, and full-range lower bound for 480 seeded real symmetric circulant examples in dimensions 2, 4, 6 and 8. The 480 numerical cases do not prove the universal statements, which follow from the exact algebra in `RESULT.md`. Independent review, external certification and experimental optical-hardware verification have not been performed.
