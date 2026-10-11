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

# Verification and limits

The complete proof is analytic and is contained in `RESULT.md`. It relies on (i) the exact Fourier–Bessel inversion formula for a ball, (ii) the fixed-order Bessel asymptotic uniformly on compact ranges of the radius parameter, (iii) two integrations by parts controlling the smoothed boundary profile, (iv) a uniform periodic-averaging estimate with bounded primitives, and (v) integrable radial error and cutoff tails.

The file `verify_crossover.py` uses Python with `mpmath` for supplemental calculations. Run `python verify_crossover.py`. It independently checks the two- and three-dimensional coefficients to high precision, the dimension-two beta-function identity with the known endpoint constant, the integral expression for the crossover curve at several parameters, and the exact three-dimensional trapezoidal Fourier kernel via a separate quadrature. A successful execution confirms arithmetic consistency only; finite-parameter tests are not an infinite asymptotic proof.

The theorem does not identify the Fourier-multiplier operator norm, does not assert a profile-uniform limit without a uniform \(W^{2,1}\) bound, and does not allow dimension to vary with \(\delta\). The initial public motivating manuscript predates October 2026; its 2026-09-26 original arXiv upload provides the recorded first-public date.
