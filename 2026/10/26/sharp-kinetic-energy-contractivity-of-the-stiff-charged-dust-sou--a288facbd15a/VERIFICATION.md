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

The attached `check.py` reproduces an exact rational physical source-mode amplification witness below the cutoff; checks the ordered noncommutative matrix identity using dissipative complex matrices; and checks mass-weighted full-space contraction for random positive-density, positive-drag multispecies models with arbitrary signed gyrofrequencies and resolved three-dimensional Lorentz rotation. Execution requires Python 3 and NumPy. The checked data are finite and do not establish the universal theorem: its proof is the sum-of-squares matrix factorization and orthogonal star-incidence decomposition in `RESULT.md`.

All checks are for constant source parameters and exact matrix function evaluation up to floating-point numerical error. A small finite-precision tolerance is used for numerical singular values. No formal or independent verification has been performed.
