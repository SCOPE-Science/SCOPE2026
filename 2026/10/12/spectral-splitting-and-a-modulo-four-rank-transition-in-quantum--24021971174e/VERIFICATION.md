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

Execute `python verify.py` using Python 3 and NumPy. The script computes the average mixing matrix independently by diagonalizing the actual sunlet adjacency matrix and grouping equal adjacency eigenvalues, then compares it against the block formula derived from the base cycle spectrum. It also checks exact rational Fourier coefficients (not floating-point approximations) at orders \(4,6,8,12\).

A local replay from the accompanying `verify.py` produced:

`VERIFY_OK exact_cycle_orders=4,6,8,12 independent_matrix_orders=3..24 fourier_modes=30 max_matrix_error=9.645e-16 mod4_boundary_8=7/16`

All computed ranks agree with the unrestricted theorem for the 22 explicitly checked orders. Exact rational tests check 30 Fourier-mode coefficients across four orders. Floating-point matrix comparisons showed maximal elementwise discrepancy below \(10^{-15}\), for these finite tests. The proof for arbitrarily large graph order is the Fourier-projector argument in `RESULT.md`; numerical tests do not certify a universally quantified statement.

The two spectral branches of the \(2\times2\) fibre matrix are monotone and of opposite signs, so projector collisions between different base eigenvalues cannot occur. The Schur-square identity and Fourier coefficient formulas are the critical symbolic proof steps. No external validation or independent audit has been performed.
