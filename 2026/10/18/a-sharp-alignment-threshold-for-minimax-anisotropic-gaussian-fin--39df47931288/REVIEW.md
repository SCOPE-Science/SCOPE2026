# Scientific review

## Correctness — PASS
The central two-point difference is exactly a directional derivative on the centered quadratic, and the inverse-covariance Gaussian estimator is unbiased. The Gaussian fourth-moment identity yields the stated linear matrix recursion and its exact closed-form solution for every nonnegative integer horizon. The full-SPD minimax reduction follows from convexity of \(B\mapsto x^{\mathsf T}B^{-1}x\), orthogonal block-group invariance, and averaging, without presupposing diagonal covariance. Endpoint optimization supplies the unique block covariance ratio and the rank-fraction threshold. The leading-exponent claim follows because the coefficient of \(L^k\) is strictly positive for every nonzero start. The supplied program reproduces scalar optimization, Gaussian simulations, and finite matrix identities, not an infinite proof.

## Originality — PASS, with residual risk
The closest examined result is Ma and Huang, arXiv:2510.19975: their minimum-variance two-point estimator optimizes perturbations subject to isotropic second moments, rather than an inverse-covariance corrected Gaussian family with unrestricted SPD covariance, uncertain alignment, and an all-horizon minimax criterion. Starnes et al., arXiv:2411.11747, study anisotropic objective smoothing, not the exact stochastic moment recursion here. The directional-hint source, arXiv:2609.08277, concerns control variates but was accessible only as abstract/metadata, so an unexamined equivalence remains possible. Targeted mathematical-record searches did not identify matching statements or a stronger theorem that immediately implies the result, but search failure does not prove novelty. Independent literature review is still advisable.

## Mathematical value — PASS
The theorem gives a complete sharp decision rule for whether uncertain directional hints justify Gaussian covariance tilting, optimized against *all* SPD probes and simultaneously for *all* finite horizons, plus a no-improvement theorem for the asymptotic mean-square exponent. This separates a useful finite-horizon variance prefactor gain from a rate claim that the model does not support. The rank-fraction phase boundary is a natural structural quantity rather than an arbitrary parameter slice.

## Scope and verification limits
The result is limited to a centered isotropic quadratic with noiseless function values, fixed covariance and stepsize, and independent Gaussian probes. One motivating source was accessible only as an abstract, and older unindexed literature may contain equivalent formulations. Numeric experiments are corroborative, not certificates of infinite-dimensional or asymptotic claims. No independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
