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
Run `python verify.py` with NumPy and SciPy. The script reconstructs the two-class Gram matrices, recomputes the closed-form allocation, compares its smallest eigenvalue to independently optimized scalar allocations on 4,800 parameter cases, and tests numerous nonsymmetric random allocations. It also prints the exact rational demonstration for two and ten rows. This finite sampling is a diagnostic rather than an exhaustive certificate for infinitely many parameters; the matrix decomposition and calculus proof in RESULT.md establish the general claim.
