---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For fixed H∈(1/2,1), σ,a>0 and fractional Brownian increments of variance h^{2H}, the stable causal filter gives V=σ²h^{2H} x Li_{-2H}(r)/(ABC), x=ah,r=B/A. Verified summing the second-difference fractional Gaussian covariances gives (1-r)^2 Li_{-2H}(r)/r, and independent 1000-term high-precision covariance sums match the polylog. Jonquière expansion plus θ_h=1/2+cx yields relative variance (1-H)(1/6-2c)x² + ζ(-2H)x^{2H+1}/Γ(2H+1)+O_H(x^{2H+2}). c=1/12 uniquely kills x² within this family, with negative nonzero ζ(-2H) for H∈(1/2,1) giving sharp fractional rate. Padé denominator/numerator positivity gives 0<r<1 all x>0. Independent high-precision asymptotic checks H=0.6,0.8 corroborate only, not prove universal H.

## originality

PASS

Closest primary stochastic numerics source studies finite-horizon pathwise convergence; earlier stationary fBM discretization gives qualitative convergence but full text was unavailable; continuous fractional OU limit theorems do not calculate discrete theta invariant variance. PASS as bounded best-of-knowledge, with 2009 full text priority risk.

## value

PASS

Sharp invariant-variance accuracy for long-memory fractional OU numerical sampling is independently motivated. Exact bias correction separates deterministic Padé order from fractional correlated-noise barrier and gives a nontrivial fractional-power stationary benchmark, with clear restriction to one-time variance and specified theta family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
