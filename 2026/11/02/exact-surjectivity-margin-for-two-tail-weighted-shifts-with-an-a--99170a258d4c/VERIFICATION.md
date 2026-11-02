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

# Verification record

The direct proof in `RESULT.md` contains the exact adjoint identity, the lower spectral bound, strict nonattainment, a matching sequence of two tail blocks, closed-range surjectivity, the explicit one-dimensional eigenspace, and matching stability-radius perturbations.

The included standard-library Python checker `verify_gap.py` verifies 3,100 exact rational finite assertions: 700 finitely supported complex-vector cases, each with two telescoping identities plus a sharp lower inequality, and 500 pairs of exact tail-block quotients. Run `python verify_gap.py`. It makes no claim of exhaustive verification of infinite vectors, all parameters, or historical priority.

No external or independent validation has been performed. Potential coverage by more general older Jacobi or Toeplitz spectral estimates remains a priority risk.
