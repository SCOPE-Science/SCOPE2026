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

# Reproducible verification

Run `python verify.py` with Python 3 and SymPy. The program checks the full determinant polynomial identically in the symbolic entries; exact Routh–Hurwitz determinants; neutral spectral factorization identities; both exact integer witnesses; algebraic threshold roots; and 432 rational parameter cases. It executes without fetching any documents or using external credentials.

The all-positive-parameter and all-real-gain conclusions are proven by the algebraic positivity and quadratic discriminant arguments in `RESULT.md`, not by finite numerical tests. At the transition points only the linear spectrum is known; a nonlinear bifurcation or global conclusion has not been certified.

The classical forest argument is analytic. The exact scientific originality of the finite cycle phase diagram is subject to a residual comparison risk from inaccessible historical three-species loop literature. No independent validation has been performed.
