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

Run `python verify.py` in a Python 3 environment with NumPy and SymPy. The complete test prints `VERIFY_OK 1198`. It checks finite-step stochasticity exactly for several rational step sizes, all path/star limiting cycle distances and Fourier coefficients for sizes two through eight, first-order stiffness derivatives symbolically on small trees, and numerical large-step slopes on seeded random weighted trees and edge orders. These finite-dimensional checks support the analytical argument but do not independently certify the infinite set of graph sizes, rates, orders or step sizes.

The all-parameter proof is given in `RESULT.md`; exact structural reasoning is necessary for the assertions beyond tested sizes. The result is self-reviewed, not independently audited.
