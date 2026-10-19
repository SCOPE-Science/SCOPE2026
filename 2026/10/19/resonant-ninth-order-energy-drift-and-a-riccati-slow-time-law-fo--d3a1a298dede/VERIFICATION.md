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

# Reproducibility and limitations

Run `python verify.py` with Python 3 and SymPy installed. The script constructs the precise nonlinear RK325 normalized stages, expands the exact squared-radius polynomial, checks the four leading even coefficients, tests the exceptional order-ten coefficient, verifies the Riccati-layer coefficient by a symbolic limit, and checks twelve exact rational Cartesian steps. The underlying proof derives these identities algebraically and proves the uniform slow-time limit by local consistency and discrete Gronwall. Numerical spot checks are not used to certify uniform-in-time asymptotics. No independent scientific audit has been performed.
