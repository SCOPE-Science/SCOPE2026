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

The statement is proved analytically in `RESULT.md`. The companion executable `verification/check_gaussian_oblique.py` checks the displayed projector against a separately assembled orthogonal-block identity on seeded Gaussian draws, verifies the squared Frobenius decomposition, checks Gaussian gamma-moment formulas at finite moment orders, and compares finite-variance Monte Carlo expectations with the closed form. It passed 460 assertions when executed with Python and NumPy.

Run `python verification/check_gaussian_oblique.py` from the extracted package root. The random seed is fixed at 20261031; the simulation checks use a fixed three-and-a-half-percent tolerance only in regimes with finite higher moments. The infinite-moment statement is **not** inferred from Monte Carlo, and the verifier does not simulate sketch-dependent differential-equation trajectories or supply an independent scholarly audit. The required statistical and analytic conclusions are justified by the matrix-Wishart/Student integration in the proof.
