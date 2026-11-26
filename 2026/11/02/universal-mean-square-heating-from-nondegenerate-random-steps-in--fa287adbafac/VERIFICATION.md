---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stated velocity-Verlet map is unimodular and strictly elliptic for 0<s<2. At a fixed step the preserved form diag(kappa_s,1) is positive definite and unique up to scale, by rotation conjugacy. On trace-one PSD matrices the normalization of the covariance map is continuous with nonzero denominator, hence has a Brouwer fixed point. A rank-one fixed point would give a real invariant line for almost every sampled step (test the expectation against the orthogonal direction), impossible at any step in scope. The transpose argument gives a definite adjoint eigenmatrix. Strict log-det Jensen on the definite covariance eigenmatrix gives lambda>=1 and equality forces a single form preserved by almost every step; the strict variation of kappa_s rules this out for a nonconstant law. Pairing the eigenmatrices equates the eigenvalues. The adjoint identity and IID assumption give the exact expectation, and the resulting bounds on powers on PSD matrices extend by differences to all symmetric matrices, proving the spectral radius claim. Independent symbolic factorization gives the stated negative two-point determinant. For the perturbation, the deterministic eigenvalue 1 is simple because the other two quadratic-lift eigenvalues are exp(+-2i theta), with 0<theta<pi. Its real analytic branch retains a definite eigenmatrix, hence is the spectral radius for small noise. Independently, ell^T M(s) r=2+s^2(kappa_s-kappa_h)^2/kappa_h with the fixed base eigenvectors; the second derivative is 2h^4/(4-h^2). Centering and ell^T r=2 give the claimed coefficient; symmetry makes the analytic branch even, giving the fourth-order remainder.

## originality

PASS

There is real indexed overlap in the qualitative instability classification for precisely the same oscillator and step matrix. Credit that overlap; a positive almost-sure exponent also implies a qualitative exponential second-moment lower bound on the expected squared product norm. The supported distinct content is the exact mean-square eigenmatrix law in all initial directions with its particular spectral rate, and especially the method-specific two-point determinant and small-noise coefficient. The inspected comparisons do not give those quantitative results. This is not a claim to the qualitative classification independently of related results or a priority certification.

## value

PASS

Per-step deterministic stability does not protect expected energy under independent changing steps. The law exactly singles out the constant-step case and identifies an observable growing at a single second-moment rate for every nonzero deterministic initial state. The determinant gives an immediate two-point certificate, and the coefficient predicts the rate scale even when heating is too slow for short trials to detect. These quantitative method-specific facts remain useful when the related pathwise instability classification is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
