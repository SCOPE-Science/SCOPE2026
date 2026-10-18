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

# Reproducibility
Run `python verify_entropy.py` from this self-contained package with Python, SymPy, and NumPy installed. The script checks the algebraic Perron eigenvector, negative drift, stationary-mass entropy simplification, monotonicity and endpoint limits; the numerical finite-state truncations are reported separately. The proof of the countable-state Perron growth rate is the explicit Doob-chain recurrence argument in `RESULT.md`, not the finite numerical check. Published transition data were taken from Ji and Ma (2023), Section 5.1, pp. 8423--8425. This package provides no independent audit.
