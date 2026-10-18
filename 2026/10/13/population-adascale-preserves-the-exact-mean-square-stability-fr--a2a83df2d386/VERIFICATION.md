---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For scalar i.i.d. nonnegative curvature A with mu>0 and finite v, single-step batch mean curvature has mean mu and second moment d=mu^2+v/S. The exact AdaScale population-gain definition from the original algorithm gives r_S=q/d with q=mu^2+v, a constant after cancellation of the common state second-moment factor. Conditioning on x_t, E[(1-alpha r_S Abar)^2]=1+[q/d](alpha^2 q-2alpha mu), independent of x_t. Fresh batches yield E[x_t^2]=Q^t x0^2. Therefore the sharp base-rate MSE contraction interval is 0<alpha<2mu/q independent of S; minimizing Q gives alpha*=mu/q, Q*=v/(S mu^2+v). Plain S-fold linear scaling has the strictly smaller bound 2mu/(S mu^2+v) for S>1. Handles v=0 and zero-iterate continuation.

## originality

PASS

The AdaScale original Johnson–Agrawal–Gu–Guestrin 2020 Algorithm 2 defines precisely the gain ratio, and Theorem 2 supplies a bounded-variance PL convergence upper bound. Its Assumption 3 globally bounds variance and fails for scalar multiplicative noise v>0. The exact random-curvature multiplier, sharp all-S stability frontier, and optimizer are not given in the inspected full source; generic mean-square multiplicative-noise theory contains the recursion method but not the gain cancellation. The contribution is a sharp algorithm-specific benchmark, not a broad new stochastic-stability lemma.

## value

PASS

The mathematically motivated question is whether scale changes the precise safe base-rate interval in variance-adaptive parallel stochastic-gradient descent. On a natural random-curvature quadratic the answer has an exact all-scale boundary and contraction-rate formula, distinguishing AdaScale from conventional S-linear learning rates. Although scalar and algebraically compact, it provides a useful normalization/stability benchmark beyond general asymptotic loss bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
