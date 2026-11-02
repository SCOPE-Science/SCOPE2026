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

# Verification and reproducibility

Run `python verify.py` with Python 3 and NumPy/SciPy installed. The independently computed summary is in `verification_output.json`.

The numerical checks test the complete transition matrix against Fourier eigenvalues for integer \(m\) from 3 through 18, compare the closed-form optimum with a separately built linear program for integer \(m\) from 3 through 100, and check the explicit three-mode dual weights and all eigenvalue bounds over the latter range. They also test 1,200 asymmetrically assigned feasible transition matrices (seed 20261025). The initial script run had an overly tight numerical tolerance on a finite-size asymptotic check; that check's tolerance was corrected and the delivered script was rerun successfully. This was a numerical tolerance in a non-proof cross-check, not a failed theorem instance.

The analytic proof, not the finite test range, establishes optimality for every integer \(m\ge3\). The verification does not test global uniqueness beyond the rotation-invariant class and does not independently certify priority or any external review channel.
