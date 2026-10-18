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

# Reproduction and analytic limits

Run `python verify.py` with NumPy and SymPy installed. Its seeded execution passed **7,146 checks**: three exact symbolic identities at unit parameters, 420 randomly chosen spectral intervals, comparisons with 12 trial shifts per interval, full three-by-three dense matrices with orthogonal eigenvector rotations, endpoint-curvature equality and finite large-range checks. The companion result supplies the exact eigenvalue reduction, derivative, three-mode attaining example, strict minimax uniqueness proof and limiting calculation. Finite tests are corroboration, not proofs of universal inequalities or asymptotic statements.

The benchmark is the exact reduced Hessian in the feedback variable, not an inexact linear solver; no floating-point conditioning or computational-speed certification is claimed. Independent validation has not been performed.
