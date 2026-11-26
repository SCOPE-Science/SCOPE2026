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

The generator applied to x²+gq² gives −2(x−q)²−rx²+4, which is coercive at fixed g,r>0. With the elliptic diffusion and positive probability of no reset over any finite interval, the stationary law is unique with finite second moments. The stationary quadratic equations give H=1+K and the stated M,K. The linear mean drift A has distinct negative eigenvalues, with trace −(1+r+1/g) and determinant r/g, so the stationary projection of exp(tA) gives the two rates and amplitudes by matching C(0) and C′(0+). For Z=K/M one has 1/2<Z<1. With d=1+r−Z and the frozen quadratic p, p(d)=−gZd+Z−1<0, placing d strictly between the roots. The first row of (−A)^{-1} gives the integrated lag. At fixed g, λ_f=r+1+O_g(r^{-1}), λ_s=1/g+O_g(r^{-1}), a_f=2/r+O_g(r^{-2}) and a_s=1/r²+O_g(r^{-3}); in particular λ_f−d tends to 1/2. These expansions give the short-time and positive-lag limits, the stated crossover with its error, and the fixed-frequency constant 4 plus bath Lorentzian by transforming both modes before taking limits. The convergence is locally uniform on the stated domains; the fixed-positive-lag scaling fails at zero. Independent exact balance and bounded semigroup/asymptotic checks agreed.

## originality

PASS

Originality is supported for the positive-mode and singular two-scale stationary law, especially the explicit nonzero residual spectral Lorentzian for an unreset bath. The same model, moment equations, and one-time variance are known, and the matrix regression itself is a routine implication; neither is credited as new. The strongest examined same-model prior gives one-time and transient variances, not the modal-weight sign or strong-reset spectral coefficients. Inspected full-renewal spectral results use a materially different reset operator.

## value

PASS

The two leading measurements diagnose different effects: on reset-time lags the covariance is bath-independent to leading order, while at fixed positive lag its first surviving term measures the bath relaxation time. At fixed frequency that weak slow mode competes with the shrinking fast layer and adds an explicit Lorentzian to a constant background. This predicts a quantitative way to distinguish retained bath memory even when leading one-time statistics cannot, and supplies a clear benchmark for nonrenewing reset models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
