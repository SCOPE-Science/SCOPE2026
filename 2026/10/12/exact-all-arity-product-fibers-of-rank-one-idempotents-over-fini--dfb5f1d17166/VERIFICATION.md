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

Represent each nonzero rank-one target B=u beta and each factor by u alpha with alpha(u)=1. The count of idempotents causing transition alpha->beta is H if equal, 0 if distinct proportional, and q^{n-2} otherwise. The exact matrix T=q^{n-2}(J-E)+H I has projections J/N, E/g-J/N, I-E/g and eigenvalues q^{2n-2},q^{n-2},q^{n-1}; summing T^{r-1} over H first forms gives every trace-class fiber, while row sum gives zero fiber. Handles q=2 (third projector zero), n=2, r=1, and zero target. Independently enumerated all targets for q=2,n=2,r<=4; q=3,n=2,r<=3; q=2,n=3,r<=3.

## originality

PASS

The exact all-dimension, all-arity, prescribed-target idempotent-product distribution is distinct from real nonnegative idempotent factor existence and finite semigroup spectral theory under R-trivial assumptions (inapplicable here). General Barnes–Cerrito–Levi paper unread; record residual coverage risk.

## value

PASS

An exact natural finite-field matrix factorization census with trace-stratified fibers, exact survival probability and mixing rates, rather than an isolated small matrix calculation. Useful for semigroup random walks and constrained matrix products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
