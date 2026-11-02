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

The analytic proof in `RESULT.md` supplies the full infinite-family argument. `verify.py` (standard-library Python) was run from the same package directory with `python verify.py`, producing:

`DIEHEDRAL_SCHUR_REPLAY_OK dimensions_m=3..20 orthogonality_entries 11460 max_err 3.17e-15 six_phase_checked_m=301..306`

The program separately assembles the sign mask, synthesizes the spectral-sign orthogonal test matrix, checks every orthogonality entry, compares the test's all-ones Rayleigh value with the sampled-cosine formula and trigonometric closed form, and checks each residue-class Taylor correction at a larger dimension. Finite and floating-point checks cannot establish the exact formula, the error estimate, or infinitely many monotonicity reversals; those follow from the four analytic proof steps. No independent validation has been performed.
