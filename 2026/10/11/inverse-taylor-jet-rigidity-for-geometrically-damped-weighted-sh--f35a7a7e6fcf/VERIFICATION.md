---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

With weights 1,c_j q^j and bounded nonnegative coefficients, diagonal phase rotation makes numerical radius the norm of selfadjoint Jacobi J=(T+T*)/2; bipartite parity symmetry makes it the largest positive eigenvalue. At q=0 it is the simple isolated value 1/2. The holomorphic symmetric tridiagonal extension has analytic rank-one Riesz projector uniformly for interpolating bounded coefficients, by a resolvent Neumann bound on a 1/4 contour. Any Neumann path reaching coordinate j from initial support e0,e1 must cross edges 1,...,j-1, giving eigenvector coordinate order S_j=j(j-1)/2; tridiagonal recurrence yields leading coefficient (product_{l<j}h_l)/sqrt(2). Differentiating eigenvalue along the interpolation c->d by Hellmann-Feynman gives sum_{j>=k}(d_j-c_j)q^j x_j x_{j+1}. The first differing edge contributes (d_k-c_k)h_k(prod_{j<k}c_j²)/2 *q^{k(k+1)}; uniform Cauchy estimates bound all later-edge terms by o(q^{k(k+1)}). Integrating h_k yields (d_k²-c_k²)(prod_{j<k}c_j²)/4. Positivity of shared prefix makes this nonzero and allows recursive exact Taylor recovery; zeros destroy injectivity after the first disconnected component. Independently checked k=1..4 Jacobi finite examples numerically with normalized ratios converging to the coefficient, but this is not an infinite proof.

## originality

PASS

The nearest 2026 Ghosh-Birbonshi-Ojha public abstract and detailed secondary synopsis describe numerical-radius bounds and an entire-function root for a special four-periodic modulation, not an explicitly stated inverse-germ injectivity for all bounded positive coefficient sequences. Full 2009 Chien-Nakazato primary supplies a radius expansion for the single unmodulated geometric sequence; full 2022 Chakraborty-Ojha-Birbonshi primary treats finite-prefix/eventually periodic weighted shifts by determinants. Those sources offer upstream determinant machinery but not the sharp first-difference valuation k(k+1) or arbitrary-sequence triangular inverse reconstruction. Original full 2026 full text remains unread and could hide an equivalent deduction.

## value

PASS

The scalar numerical-radius germ is shown to encode the entire infinite bounded positive weight sequence with precisely predictable first-difference orders and a triangular reconstruction. That is a nontrivial inverse spectral uniqueness mechanism, naturally suggested by recent parameter-dependent shift families; its uniform analytic contour and tail estimates are not a routine single-number computation. It answers a structural question rather than merely improving a bound for a fixed numerical radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
