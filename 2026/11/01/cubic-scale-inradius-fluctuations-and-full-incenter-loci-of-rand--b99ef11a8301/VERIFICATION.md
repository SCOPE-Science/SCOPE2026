---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For all n>=2, support functional e_i restricted to u-perp has norm sqrt(1-u_i^2). Ball containment is exactly |z_i|+t sqrt(1-u_i^2)<=1; central reflection/convexity makes z=0 optimal, proving rho=(1-min_i u_i^2)^(-1/2) and every admissible maximal center. At a generic unique minimum nonzero |u_i|, precisely one coordinate center bound vanishes and the independent hyperplane condition leaves affine dimension n-2. Squared normalized independent Gaussians have Dirichlet(1/2)^n density, with x_i=a+(1-na)y_i yielding the claimed (n-1)-simplex survival formula, correct normalization Gamma(n/2)/pi^(n/2), support [1,sqrt(n/(n-1))] and no atoms. Single-coordinate and two-coordinate spherical small bands give the lower sqrt(epsilon) coefficient (with n=2 disjoint bands); a uniform simplex limit gives the stated upper (b-r)^(n-1) coefficient. n min|G_i| -> Exp(rate sqrt(2/pi)), sum G_i^2/n ->1, and a Taylor expansion give n^3(R-1) => (pi/4)Exp(1)^2. For x<=n, the bound P(n^(3/2)min|U_i|>x)<=exp(-n/16)+exp(-0.45x/sqrt2)<=2exp(-x/16), with the variable bounded by n, gives moment uniform integrability; moment constants follow. Inspected actual finite checker: literal 3D edge intersections, 2D quadrature and sampled scaling; these cannot substitute for the all-n proof.

## originality

PASS

A bounded comparison of precise mathematical statements and implications finds no identified earlier theorem covering the full new claim; known special cases and foundational tools are acknowledged; inaccessible source scopes and possible hidden prior art are explicitly residual risks.

## value

PASS

Central cube sections are a canonical convex-geometric random model. The exact free-center locus distinguishes inradius from circumscribed radius and establishes generic nonuniqueness; the cubic scale and squared-exponential law identify a previously undetermined natural random invariant beyond coarse diameter/volume estimates. Sharp support endpoints and all-moment convergence can be used for precise comparison with random-section asymptotics; the dimension and observable are mathematically motivated, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
