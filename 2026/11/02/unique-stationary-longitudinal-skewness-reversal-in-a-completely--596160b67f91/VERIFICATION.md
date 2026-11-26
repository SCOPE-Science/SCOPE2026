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

Stationarity is regenerative with exponential age T of rate r. Conditionally on T the active convolution is bounded by 1 and the independent centered thermal term has variance 1-exp(-2T); this gives finite moments and strictly positive marginal variance. I reconstructed the first three longitudinal moments directly by expanding each cosine into two exponentials, ordering times and integrating the nonnegative time gaps. For n active factors the final residual age contributes 1/(r+n), and gap number j starting from j=0 contributes 1/(r+j+the squared tail-sign sum); there are n! orderings. Thermal terms in m2 and m3 are 2/(r+2) and 3p E[F_T(1-exp(-2T))]. Centering produces the two stated rational coefficients, including p(5-p^2)/80 at r=1. Replay `cd /workspace && python audit_checks.py 3` checks these identities, Q signs, the displayed derivative polynomial and the approximate upper endpoint 1.92291776319178567. The zero of Q is unique and simple by Descartes and the signs at 1 and 2. As a separate monotonicity proof, Q/r^2 is strictly increasing for all r>0 by differentiating its positive-power terms and the two negative inverse powers. In the competitive interval, H is 3 times the product of (r^2+2r-1)(r+1)^4(r+4)(r+9)/r^2 and -1/(Q/r^2). The first factor is a product of positive increasing factors: r+2-1/r, (r+1)^4/r (increasing for r>1/3), and (r+4)(r+9); the second factor is positive increasing because Q<0. Since sqrt(2)-1>1/3, H increases strictly from zero to infinity. Inside the interval the sign is that of H-p^2, and outside it the coefficients agree in sign (or one vanishes at an endpoint). This gives the unique crossover, the strict monotonicity and limiting rates as p varies, and the fixed-r positivity criterion.

## originality

PASS

The moment machinery and physical model are prior, and stationary longitudinal skewness with the same reset protocol has been calculated without a trap. The distinct result is the exact evaluated centered third moment at matched relaxation and its all-activity negative-to-positive single crossover in reset rate; the prior observable or model changes are material.

## value

PASS

The longitudinal sign distinguishes a directional asymmetry that radial kurtosis cannot measure. Matching the two physical relaxation scales makes a natural benchmark. A unique sign boundary over an entire two-parameter slice, with universal bounding rates and their monotone interpolation with activity, is more useful than an isolated skewness calculation or simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
