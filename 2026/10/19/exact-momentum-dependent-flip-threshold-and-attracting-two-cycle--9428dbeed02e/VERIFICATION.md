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

# Reproduction and limits

Execute `python3 artifacts/verify_scalar_soft_muesterov.py` from the package root, requiring only the standard Python library. The program checks the dimensional threshold, existence and exact sign-reversal identity of the period-two branch, the derivative and its Schur inequalities, a grid of zero-momentum magnitude contractions, boundary asymptotics and finite-difference Jacobians. Successful replay returned `PASS: 9140 deterministic identities, stability checks, interval contractions and critical limits`.

These tests are finite. The universal local stability assertions are proved analytically with strict Jury inequalities; period-two uniqueness uses strict monotonicity of the explicit smooth-sign map; global zero-momentum attraction uses a deterministic interval and strict distance-contraction proof. No claim of global attraction for positive momentum, spectral matrix extension or independent validation is made.
