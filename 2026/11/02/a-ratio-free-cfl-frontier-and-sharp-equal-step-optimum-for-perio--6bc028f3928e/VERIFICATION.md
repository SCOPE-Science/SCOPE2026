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

# Reproducible checks

With `sympy>=1.12` installed, run `python verify_ab2.py` from the package directory. The script executed successfully on the packaged source and reported:

`VERIFY_OK symbolic=7 phase_matrix_limit=1 rational_checks=182 sharp_penalty=1.666666640`

Exact symbolic checks cover the transfer trace/determinant, the Schur identity, the equal-split discriminant factorization, the sharp penalty inequality, the special scalar identity, and the reversed-product phase limit. The rational cases independently match the AB2 recurrence and matrix product. Floating-point roots test representative stable, critical and unstable parameters and verify the optimizer ordering. The proof in `RESULT.md` establishes all infinite-domain inequalities; a finite test does not certify them. No tests cover nonperiodic grids, nonnormal matrices or nonlinear equations.
