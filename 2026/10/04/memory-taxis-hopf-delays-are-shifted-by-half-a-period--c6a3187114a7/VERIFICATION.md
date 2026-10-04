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

The proof was checked directly from the modal determinant of the source linearized system. For a Neumann mode \(\Delta\phi_k=-\mu_k\phi_k\), the retained taxis term \(-\chi v_*\Delta\widetilde u(t-\tau)\) becomes \(+\chi v_*\mu_k\widetilde u_k(t-\tau)\). Expanding the two-by-two determinant gives delayed coefficient \(-a_{12}\chi v_*\mu_k\).

The packaged `verify.py` repeats this determinant bookkeeping with exact rational test coefficients and checks a phase instance numerically. It verifies that the corrected characteristic residual vanishes at the corrected phase, that the printed-sign branch does not, and that the two delay branches differ by \(\pi/\omega\).

The squared frequency equation is not used as evidence for the sign because squaring removes it. No finite computation is treated as proof of the general statement; the general proof is the determinant and phase algebra in `RESULT.md`. The computation is only a replay check for sign and branch bookkeeping.

The verification does not recompute the article's nonlinear simulations, global dynamics, or Hopf normal-form coefficients.
