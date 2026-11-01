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

# Reproduction and scientific limits

Run `python3 CHECK.py` from a folder containing this report and the checker. It requires Python 3 with no third-party packages. The checker independently integrates the original pair-interaction energy and computes symmetric finite-difference Rayleigh quotients along first and alternating angular Fourier vectors; it evaluates the displayed exact endpoint formulas, checks a finite grid for the curvature-ratio trend, and builds rigorous rational intervals for \(\pi\) and \(\log 2\) that certify the signs at exponents two and three. The recorded execution returned `PASS: exact rational endpoint certificates, integral formulas, independent finite-difference Hessian and ratio monotonicity ( 32 modal checks)`.

The finite-difference and finite-grid tests are **supplementary** and do not establish statements about all exponents. Global existence, uniqueness of the crossing, positivity, and sharp local stability follow from the analytic integral, strict monotone-likelihood-ratio comparison, and Fourier diagonalization in `RESULT.md`. The decimal approximation of the crossing is not part of the exact certificate, and the absence of unindexed equivalent literature is not certified. Independent validation has not been performed.
