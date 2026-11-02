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

## Analytic checks

The finite cutoff matrix was derived from the canonical Hermite ladder identities, not inferred from numerical spectra. Positivity follows from the explicit invertible upper bidiagonal factor. The determinant at \(1\) follows by exact tridiagonal recurrence. The strict single-eigenvalue crossing follows from full-oscillator min--max comparison and strict interlacing. The reciprocal trace follows by an explicit triangular inverse and the binomial hockey-stick identity. The subcritical relative error is proved by Poisson concentration plus a harmonic bound on all other eigenvalues. The supercritical limit is proved by matching operator-norm and explicit sine-trial bounds.

## Reproducible supplemental checks

Run `python3 verify.py` using Python 3 and only the standard library. The checker was executed from this final file bundle and reported `PASS 250 checks: exact determinant, reciprocal trace, critical eigenvector and Poisson prefactor`. It compares determinant and inverse-trace expressions by exact rational arithmetic for twenty dimensions and five rational displacement parameters, checks a critical eigenvector for dimensions through thirty, and tests the convergence of Poisson prefactor expectations in four fixed-parameter regimes. These finite checks neither certify all dimensions nor prove either limit. The proof in `RESULT.md` handles the universal quantifiers.

## Scope limitations

The spectral floor is the lowest eigenvalue of the consecutive low-mode Hermite compression. The estimates do not cover arbitrary masks, higher-dimensional oscillators or the critical transition window where \(\rho\to1\) with \(N\). Comparison against potential equivalent results in older queueing and orthogonal-polynomial literature is not exhaustive. No independent audit or certification was conducted.
