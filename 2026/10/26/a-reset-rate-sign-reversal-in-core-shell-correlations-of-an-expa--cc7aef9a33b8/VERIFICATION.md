---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Integrating the normalized parabola over the symmetric windows gives the displayed fractions. The stationary age of the common Poisson clock is Exp(r), so the covariance is over one shared scalar, not over separate reset ages. Integrating the scale equation yields lambda'^2=2 omega^2(1-1/lambda), with the increasing branch lambda(t) asymptotic to sqrt(2) omega t. A and B are bounded with O(1/t) tails, and B is zero through t_c and positive afterward. AB is integrable and positive on a set of positive measure. Dominated convergence gives E[AB]/r -> C0; splitting each marginal mean at t=1/r gives O(r log(1/r)), so their product is negligible at order r. For strong resetting, shift the entire covariance integral to t_c, writing its integrand as B(t)(A(t)-E[A]) times the exponential-age density. For t just above t_c, let z=c/lambda(t); then B=(1-z)^2(z+2)/2, so it starts as (3/2)(lambda'(t_c)/c)^2(t-t_c)^2. The factor A(t)-E[A] tends locally to A(t_c)-A(0), strictly negative because A decreases and t_c>0. Scaling t-t_c by 1/r gives the factor 2 from the exponential second moment; the rest of the age integral is exponentially negligible. This yields the negative coefficient and its independence of fixed v>c. The Laplace integrals are real analytic for r>0, so opposite endpoint signs ensure a sign-changing zero, without implying uniqueness. The benchmark prefactor is 89/486 for omega=1; a separate high-precision quadrature in the scaled edge-speed variable reproduces the benchmark C0 and signs, as corroboration only.

## originality

PASS

The supported distinct claim is the integrated core–exterior-shell covariance, with weak-to-strong reset sign reversal for every stated geometry and both sharp asymptotics. The common-age mechanism and one-window mass fractions are established inputs. Neither the inspected one-window FCS nor the closest indexed spatial covariance result gives these disjoint-window rate limits. Searches and source access are bounded, not a historical priority guarantee.

## value

PASS

Disjoint windows in a reset condensate probe joint spatial behavior that single-window counting does not reveal. The theorem shows opposite signs for every admissible core/exterior-shell geometry and identifies a sharp activated decay at strong resetting, with the onset set by the inner radius but not the outer radius. This distinguishes late-age overlap from rare shell entrance, rather than just supplying a numerical example or a new name for the common-age representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
