---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For Pareto scale a>0, shape alpha>2, mu=alpha a/(alpha-1), sigma=a sqrt(alpha)/((alpha-1)sqrt(alpha-2)), so mu-sigma<a since sqrt(alpha/(alpha-2))>1. Therefore the standardized one-sigma central mass equals 1-A_alpha^-alpha, where A_alpha=alpha/(alpha-1)*(1+1/sqrt(alpha(alpha-2))). For x>0 log(1+x)>x/(1+x); applied to 1/(alpha-1) and 1/sqrt(alpha(alpha-2)), each contributes >1/alpha to log A, giving alpha log A>2. As alpha->infinity, log A=2/alpha+1/alpha^2+7/(6alpha^3)+..., hence central mass=1-e^-2+e^-2/alpha+O(alpha^-2). Strict inequality and convergence establish sharp unattained infimum for all scales/shapes, not a generic Chebyshev bound. Independently evaluated 7 shapes including alpha=10000; finite checks corroborate.

## originality

PASS

The source studying fixed multiples of mean optimizes P(X<=k E X), a different functional; 2024 Pareto anti-concentration source proves inf over shape of outside-one-sigma mass is zero, which bounds supremum of central mass, not its infimum. No matched exact shape infimum found within material actually inspected.

## value

PASS

The exact worst-case one-standard-deviation coverage is a natural shape-uniform concentration guarantee for a canonical heavy-tailed law, with a sharp attainable-status and first asymptotic correction. It fills the Pareto analogue of documented family-specific central-mass optimization questions; the exact value is not implied by the previously established complementary infimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
