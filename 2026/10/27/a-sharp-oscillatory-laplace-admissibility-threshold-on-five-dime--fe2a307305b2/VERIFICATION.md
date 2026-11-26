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

For curvature −1 the radial measure is |S⁴|sinh⁴(r)dr. With a>4 the convolution kernel is integrable, and spherical Plancherel diagonalizes it with continuous radial multiplier supported on the full principal spectrum. Positivity of the operator and finite-point PSD agree by integration and approximate point masses; a negative value at λ=0 also produces negative values at positive λ by continuity. Dimension raising of sin(λr)/(λ sinh r), integration by parts (with vanishing endpoints), and the Laplace-sine identity give 24z divided by the three quadratic factors before multiplying by |S⁴|. As an algebra cross-check, the conjugate denominator is (v²+X)³+8(X−v²)(v²+X)+16(v²+X), v=conj(z), and Re(zv^(2j))=(a²+W)Re(v^(2j−1)) for j≥1. This reproduces the sign polynomial with a positive squared denominator. Its constant-factor quadratic C changes sign before both a²/3 and a²−4 and is negative from the lower root to a²−4. Up to that lower root the coefficient of X is 3(a²+W)(a²−3W)+16>0, as are the higher coefficients, so equality has only the zero at X=0. Beyond the root, X=0 is a witness below a²−4, and X=W−a²+4 gives −8a(a²−4)(W+2)(W+4)<0 otherwise. At a=6 the lower root is 16/5. The proof establishes the global statement; the symbolic and quadrature checks in check_h5.py and VERIFICATION.md are recorded supporting diagnostics, not a fresh numerical run or a formal certificate.

## originality

PASS

The strongest catalogue entry gives a complete threshold for the identical family on H³, not H⁵. Neither restriction nor the prior analytic machinery supplies the five-dimensional sign result. The distinct content supported here is the fast-decay five-dimensional if-and-only-if condition, boundary spectrum and explicit obstructions, not the transform criterion or dimension shift themselves. This is a bounded, best-of-knowledge assessment.

## value

PASS

A practitioner choosing a geodesic oscillatory covariance gets an exact allowed region and, when inadmissible, an explicit spectral obstruction. H⁵ is the next odd dimension after the close H³ precedent but the cubic and the returning sign at λ=0 require a distinct necessity argument. The endpoint is a multiplier zero, not a claim about singularity of finite Gram matrices. The decay restriction is essential to the reviewed scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
