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

# Verification of the mathematical result

The analytic argument in `RESULT.md` proves the parameter-space statement for all interior positive relaxation pairs. The supplementary checker `verify_frontier.py` requires Python 3 and only the standard library; run `python verify_frontier.py` in the extracted file directory.

Its actual completed checks include 720 exact-Fraction identities for the transformed stability polynomial, 9,801 high-precision comparisons with the published radical stability boundary, 19,220 exact-Fraction relaxation-box grid cases (17,826 satisfying the stability inequality), and 103 extremal designs checked with 75-digit Decimal arithmetic. The crossover identity and the limiting dispersion constant are checked. An additional independently constructed three-population Fourier amplification matrix was evaluated at small wavenumbers for three relaxation settings; the observed cubic logarithmic coefficients approached the analytic coefficient derived from the published physical branch. These finite computations do not prove the infinite-domain or continuum asymptotic assertions; the proof and the cited stability theorem do.

The sharp limit \(p\downarrow1/8\) requires a relaxation parameter approaching a singular endpoint. Uniform convergence in this limit, behavior at nonzero wavenumber under the kinetic cap, nonlinear stability, and end-to-end error are not claimed. The prior-work comparison has a specific unresolved older-paper access limitation. Independent mathematical validation has not been performed.
