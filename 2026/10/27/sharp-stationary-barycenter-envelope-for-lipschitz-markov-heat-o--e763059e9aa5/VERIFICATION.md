---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n>=3 ordered positions x_0<...<x_(n-1), positive stationary masses pi and reversible nearest-neighbor generator with conductances c_i>0, the real Lipschitz seminorm operator norm is computed on functions modulo constants. Stochastically monotone row distributions satisfy one-dimensional W1 duality: ||K||_Lip=max_i (E[X1|X0=i+1]-E[X1|X0=i])/(x_(i+1)-x_i), and f(i)=x_i attains it simultaneously. Stationarity piK=pi and rearrangement of a fixed marginal with split mass R_k bound each adjacent mean jump by b_k-a_k where a,b are conditional left/right stationary means; hence C(pi,x)=max_k (b_k-a_k)/edgegap. Conditional averaging on the two sides of each cut gives a stationary monotone idempotent kernel exactly saturating that cut. Birth-death edge differences obey a Metzler linear system, so e^{tQ} is stochastically monotone. Its strictly positive entries at finite t>0 make the rearrangement strict (t=0 norm=1<C), while one edge c_k=epsilon, all others one and t=epsilon^-1/2 yields the cut kernel limit: Duhamel O(sqrt epsilon) plus mixing of both irreducible blocks. Uniform masses and unit gaps give C=n/2. Exact conditional-kernel checks for varying rational masses and lengths and independent numerical heat checks corroborate examples. Full universal conclusion follows from transport, rearrangement, and semigroup limits.

## originality

PASS

Statement/implication comparison of actually read primary theorems and direct published mathematical-finding search supports best-of-knowledge originality for the final narrow claim, with precisely documented broader prior formulas and residual historical risks. Neither a failed search nor literature inaccessibility is treated as a proof of novelty.

## value

PASS

This identifies a sharp stationary-law-and-metric invariant for amplification across all positive reversible path conductances, with a simple slow-bottleneck extremal mechanism and universal order-preserving Markov extension. Exact n/2 scaling and strict nonattainment explain a natural heat-flow stability boundary, and the nonmonotone counterexample shows hypotheses matter. It is not just a routine fixed-chain contraction estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
