---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the D/ε occupation normalization the boundary regulator is L, giving the Robin condition f'(0)=θ(f(0)-1) for the transform at an exponential local-time budget. The bounded solution of Df''-(r+s)f+rf(a)=0, evaluated at a and at the Robin boundary, is Ĥ(s)θ/(θ+ψ(s)) with Ĥ=(r+s)e^(-a q)/(s+r e^(-a q)) and ψ=sq/(s+r e^(-a q)), q=sqrt((r+s)/D). Inverting the θ mixture gives the fixed-budget transform; extension from almost-everywhere in budget follows by right continuity of the inverse. The first-hit factor is also obtained by renewal at the earlier of a free boundary hit and a reset. After the first hit, each inverse-local-time stopping time starts the spatial motion at zero with a fresh Poisson clock, giving stationary independent increments without resetting the budget. Analyticity of the transforms near zero gives finite moments; an ordinary CLT for unit-budget increments plus the bounded-length remainder and independent first hit gives the fixed-z Gaussian limit. I differentiated the dimensionless log transform exactly and independently reproduced both cumulants, B'=e^z F/z⁴, F'=(2z-1)(2e^z-1), and z*=1.3309178942733854 (square 1.7713424412971023). Since F(0)=-3, F(1)<0, F(3/2)>0 and F is increasing beyond 1/2, the sign change is unique. Coercivity and uniqueness of the leading coefficient minima and nonnegative first-hit costs confine all exact global minimizers to the appropriate limits, without assuming uniqueness at finite budget. Finally C'(z) has sign e^(-z)(z²+z+1)-2<0. This last limit is pointwise in z, not a simultaneous infinite-rate/large-budget limit. The supplied verifier was inspected, not executed.

## originality

PASS

The supported distinct result is the global large-budget rate separation for absolute variance versus mean, convergence of all finite-budget global optimizers to the distinct limits, and the contrasting strict decrease of the large-budget relative-variance coefficient. The retained-local-time model, exact mean and transform are not distinct. The entire finite-threshold variance, including the coefficient B(z), is explicitly covered by indexed result b8afa7134304 and follows from a more general indexed transform as well. Those exact overlaps are credited. The compared statements give a throughput optimization or evaluate variance at the mean-optimal rate; neither determines the independent global minimizer of absolute variance. The distinct optimization requires a global critical-point and coercivity argument, not merely inserting the single-site law or changing units.

## value

PASS

For a natural deterministic accumulated-contact reaction budget, a practitioner optimizing rate for speed need not obtain the best absolute timing reliability. The strict global large-budget separation by the universal physical rate factor 1.771342441… and the opposite preference of the relative-variance coefficient make that distinction actionable in the model. The result is not an arbitrary parameter slice, and it does not promise a finite global optimum for the relative criterion or claim uniformity in a simultaneous large-rate limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
