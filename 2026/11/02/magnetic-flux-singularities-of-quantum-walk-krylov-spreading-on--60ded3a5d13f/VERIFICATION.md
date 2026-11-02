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

# Verification and scope

The exact argument is in `RESULT.md`. For every integer \(N\ge3\), the Fourier spectrum has one simple eigenvalue for every mode except at integer half-flux multiples, and the degeneracy classification follows directly from the cosine equality condition. The projected spectral density yields \(\overline p_j\) after dephasing; no stochastic approximation, time-grid truncation or floating-point interpolation is needed to prove the theorem.

For reproducibility, run `python3 verify_flux_cycle.py` with Python 3. The standalone script reports `PASS: 1300 independent finite checks; all-cycle proof remains analytic`. It reconstructs the orthogonal polynomials on distinct Fourier energies from scratch rather than inserting the asserted Krylov populations. It compares the resulting expectations against the full population and mean formulas on \(N=3,\ldots,27\), checks exact rational identities up to \(N=149\), and estimates finite-time Cesàro integrals on small cycles as an additional independent check.

The finite checks do not replace the exact all-size proof or establish convergence rates uniform in flux. The result treats a single localized seed in a unitary nearest-neighbor finite ring; no independent external audit or certification is asserted.
