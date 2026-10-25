---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For W_t=x+mu*t+B_t under the exact hard event integral_0^T W_t^2 dt <= theta*T (x,mu fixed, theta>0, S>0 fixed), the Cameron-Martin terminal weighting is e^(mu W_T). The harmonic oscillator Laplace transform L_T(u)=exp[-sqrt(2u)*x^2*tanh(T sqrt(2u))/2]/sqrt(cosh(T sqrt(2u))) has Dirichlet initial/Neumann free-terminal Green kernel. For Re(u)>0 its two disjoint S-windows converge to covariance (e^-omega|s-t| - e^-omega(s+t))/(2omega) initially and (e^-omega|r-v| + e^-omega(r+v))/(2omega) finally; cross-covariance ->0. The hard-inequality Bromwich inversion has unique saddle u*=1/(8theta^2) and f''=4theta^3, giving omega=1/(2theta). Exponential terminal tilt shifts only reversed endpoint mean to 2theta mu and leaves variance 2theta. Initial-window tightness uses the cited initial-limit theorem and terminal fourth-moment contour increment estimates give tightness via Kolmogorov. The 569 finite kernel/resolvent assertions do not establish the infinite-horizon inversion or independence; those depend on the displayed analytic estimates.

## originality

PASS

Best-of-knowledge comparison of the exact claim against named closely related published results, semantic Resultary search and inspected primary scientific material; unsuccessful retrieval is not treated as evidence of absence.

## value

PASS

Sharp two-boundary path-law classification under a hard quadratic Brownian confinement, including the nonstationary free-end covariance and asymptotic independence, isolates a genuine structural distinction missed by initial-window limits and stationary bulk heuristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
