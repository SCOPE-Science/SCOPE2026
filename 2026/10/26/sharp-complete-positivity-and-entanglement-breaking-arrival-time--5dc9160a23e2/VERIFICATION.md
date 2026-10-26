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

# Reproducible verification and limits

Run `python verification.py` after installing the three libraries listed in `requirements.txt`. The supplied program uses no downloaded datasets, network requests, or external files. It derives the Choi matrix independently by applying the time-dependent affine map to all four complex matrix units, then compares the resulting \(4\times4\) matrix to the formula in the proof. It separately computes the partial transpose, all eigenvalues, and the CP and EB inequalities over a finite multi-parameter grid, checking normalization and determinant implications indirectly through the eigenvalues.

The program solves arrival-time equations numerically for multiple exponents and translations and checks the monotone threshold assertions on another finite grid. A high-precision mpmath bisection additionally compares the fixed-\(\alpha\) fractional-power gap and the critical \(\alpha=1+u/L\) layer against their stated asymptotic constants. A direct execution of this program passed **2,230** assertions. The example \(\alpha=3\), \(\beta=0.6\) produced \(t_{\mathrm{CP}}\simeq0.6449379916078235\), \(t_{\mathrm{EB}}\simeq0.8989625707590763\).

Ten conditional eigenvalue-sign comparisons were intentionally not asserted because the eigenvalue magnitude lay within the stated floating-point tolerance; the analytic proof covers these boundary values. All calculations are finite consistency checks, not certificates for all real parameters, continuous time, or asymptotic limits. The proof in `RESULT.md` provides those analytic arguments. No independent external validation was performed.
