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

The analytical proof in RESULT.md gives the all-parameter result; the reproducibility script `verify.py` is finite supporting evidence. Running `python3 verify.py` performs 3,263,634 assertions over exact fixed-point identities, full ring Fourier eigenmode traces and determinants, numerical eigenvalue/Jury agreement, parameter-specific parity examples, and independent finite-difference checks of the full Jacobian at fixed points. Uses Python 3 standard library only. No verified assertion is used to infer an untested universal statement; those follow from the proof. Unresolved: nonlinear dynamics at Schur boundaries, other attractors, basins outside a neighborhood, and literature priority beyond the examined sources.
