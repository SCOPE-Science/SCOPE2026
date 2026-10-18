---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

On the bilateral lattice X=T+T^-1, I-rL4=(r/12)(X^2-16X+28+12/r)=(r/12)(s_+-X)(s_--X), s_±=8±sqrt(36-12/r). If r>=1/3, s_±>2 and each factor has positive summable geometric Green kernel q_s^|k|/sqrt(s²-4); convolution proves strictly positive kernel and constant function normalization proves mass 1. If 0<r<1/3, s_± are conjugates outside [-2,2], with two distinct conjugate interior roots q=rho exp(i theta); the nonzero residue coefficients form 2|C|rho^k cos(k theta+phi) and cannot remain nonnegative for every integer k. A point mass witnesses failure. Independent exact factorization and large periodic inverse sample reproduced r=1/10 negative g3=-0.000178311524445 and positive samples at r=1/3,1/2,4/3; those finite checks alone do NOT establish the universal theorem.

## originality

PASS

The threshold for the classical infinite-grid long stencil is an exact new boundary relative to inspected high-order maximum-principle schemes and general Toeplitz inverse literature. The standard stencil and the factorization method are prior knowledge. The strongest residual risk is an implicit identical threshold in older pentadiagonal inverse work, whose complete full text was unavailable. This is qualified best-of-knowledge originality, not an exhaustive priority claim.

## value

PASS

This is a mathematically motivated exact monotonicity/maximum-principle boundary for a widely used high-order finite difference stencil. It reverses the usual intuition that small implicit time steps restore positivity, gives a sharp time-step threshold, and separates infinite-lattice results from boundary-closure behavior; a precise invariant of direct use in numerical PDE stability/monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
