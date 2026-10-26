# Self-review

## Correctness — PASS
The exact conditional increment identity yields a correctly normalized martingale. The deterministic product has exponent \(-1/2\) and a bounded periodic factor; the omitted discrete-to-continuum terms are summable because \(h\) is continuously differentiable. Martingale second moments are \(O(\log n)\), implying an almost-sure finite total predictable-variance correction. The normalized bracket converges uniformly, and bounded jumps give the functional martingale CLT. The physical-time variance ODE and clock inverse are derived, not assumed. The proof specifies the full real sequence, all subsequences and finite time horizons; finite computations serve only as checks.

## Originality — PASS (with residual risk)
Fan–Qi (arXiv:2610.16065v1) handles arbitrary time-dependent repetition probabilities but states *scalar* limit theorems, rather than the phase-indexed functional limit. Its scalar CLT already implies a marginal Gaussian conclusion once its variance normalization is computed. Tokumitsu (arXiv:2603.13690v1) and Baur–Bertoin (arXiv:1608.01305) give functional limits for the fixed-memory model and cover the zero-forcing specialization; they do not subsume the nonconstant time-dependent covariance clock. James–James–Qi (2008) treats time-varying correlated Bernoulli processes with scalar limits. The distinguishing scientific claim is the whole functional clock family, inversion and nonconvergent phase profile, not any generic martingale FCLT. Equivalent unpublished/less-indexed correlated-Bernoulli or urn statements remain a genuine residual risk.

## Mathematical value — PASS
At the critical reinforcement threshold the smallest logarithmically oscillating changes to the repetition probabilities can be invisible to the pointwise limit \(p_n\to3/4\), yet reshape the entire Gaussian covariance clock. The result gives exact structural dependence, a reconstructible modulation profile, and proves lack of a single physical-time CLT at the standard scale. This is a natural process-level boundary for time-dependent reinforcement, not a routine finite test or parameter substitution. No universal general time-dependent functional theorem or downstream application is claimed.

## Scientific limits
Weak convergence in the Skorokhod topology only, no strong coupling. Smooth periodic zero-mean perturbations only. Clock phase labels may coincide for forcing with smaller fundamental period. No exhaustive review of all alternative urn formulations or independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
