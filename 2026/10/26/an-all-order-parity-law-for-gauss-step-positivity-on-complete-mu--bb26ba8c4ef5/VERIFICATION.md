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

# Reproducibility and limits

The standalone `verify.py` recomputes polynomial coefficients using factorial-based exact fractions, checks coefficient-ratio monotonicity across stage counts \(1\) through \(40\), and computes direct rational matrix functions \(Q_s(-hL)Q_s(hL)^{-1}\). It independently compares these matrices with the projected spectral formulas on \(11\) graph configurations, \(7\) stage counts, and \(3\) rational positive step sizes. It verifies conservation, all off-diagonal strict signs, all even-stage strict diagonal signs, and five large-step odd-stage sign obstructions. All tests passed; the exact output is recorded in `verification_output.txt`.

Run with `python verify.py` and Python 3 plus SymPy. Recomputed checks are finite and do not establish the universal theorem; the coefficient-ratio proof and the exact Laplacian projectors in `RESULT.md` establish its unrestricted quantifiers. No external independent mathematical audit or certification has occurred.
