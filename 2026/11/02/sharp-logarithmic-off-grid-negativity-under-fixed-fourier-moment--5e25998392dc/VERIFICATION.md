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

At the 2N+1 equally spaced nodes, exact cardinal trigonometric interpolation expresses any normalized nodal-nonnegative p as a convex combination of translates of D_N. Convexity and translation invariance give negative mass at most (||D_N||_{L1(mu)}-1)/2=(2/pi^2)log N+O(1). For fixed K choose q=2K+1 grid phases near distinct q-th roots of unity; invertibility of the real Fourier moment matrix and small perturbation produce positive mass-one quadrature weights killing the first K complex moments. Their separated Dirichlet mixtures satisfy all nodal/moment constraints and retain the full L1 logarithmic contribution because overlaps are uniformly bounded away from singular neighborhoods. Strictly positive analytic Poisson mixtures have identical low moments, project to polynomials converging in L2 to those extremizers as the Poisson parameter tends to 1, and nonexpansiveness of convex Hilbert projection plus L1 Lipschitz of negative-part mass realizes the lower bound. All quantifiers fix K and allow f depending on N. The limiting coefficient follows from analysis, not finite numerical slopes.

## originality

PASS

Qualified best-of-knowledge priority based on direct mathematical statement/implication comparison, with explicit named residual risks; none of the inspected prior statements dominates the final claim. The final claim requires simultaneous positive moment quadrature, equal-mass nodal interpolation, separated peaks, and realization under constrained projection. Neither the approximation accuracy theorem nor the classical Dirichlet norm alone implies the joint fixed-K extremal law.

## value

PASS

The result quantifies the sharp worst-case failure of grid-only positivity in a natural moment-constrained Fourier spectral method. It shows that preserving any fixed number of low Fourier moments cannot reduce the leading logarithmic off-grid negative mass, even for strictly positive analytic inputs selected at each resolution. This is a substantive conservation-versus-positivity limitation, rather than a restatement of classical Dirichlet L1 growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
