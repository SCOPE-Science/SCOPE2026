---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The stationary Poisson convolution gives conditional Gaussian variance as a sum of geometrically damped exponential holding times, hence an exact positive product for the MGF on |theta|<1. A Riemann sum gives the Li2 cumulant limit with steep derivative and exponential tightness; exponential tilting proves the full LDP, not just weak convergence. The stated Itô diffusion has stationary power-law density giving J by Laplace bounds. Strict I>J follows from the positive function z^2-2z+2(1-e^-z), whose derivative is positive, and series inversion yields the sixth-order gap. An independent SymPy series inversion and rate expansion matched coefficients. No path-space or finite-s error statement is inferred.

## originality

PASS

The exact stationary transform of proportionally reset Brownian diffusion is in Tal-Friedman–Roichman–Reuveni; Galla gives the weak-reset Itô diffusion and stationary law. The joint fast/weak-reset stationary LDP and strict global rate comparison were not identified in the inspected primary results. Classical Gärtner–Ellis/tilting tools are not novel, so priority pertains to the exact comparison law.

## value

PASS

A quantitative failure of Gaussian diffusion approximation for stationary rare events, despite central agreement, is a motivated diagnostic for weak-reset models. The strict all-w separation and sixth-order onset are stronger than an isolated asymptotic example and identify the approximation limit clearly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
