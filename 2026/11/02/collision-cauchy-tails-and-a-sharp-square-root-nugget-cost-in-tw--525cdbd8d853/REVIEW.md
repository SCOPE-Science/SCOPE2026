# Scientific review

## Correctness — PASS

The exact symmetric/antisymmetric diagonalization of the two-node Gram matrix gives the singular \(m'(u)/(\alpha\delta)\) weight difference and bounds the remainder by a Gaussian-tail variable. The explicit positive-tail calculation integrates over signed node separations and Gaussian noise; dominance and symmetry give the matching negative-tail coefficient and complete absolute-moment cutoff. Lipschitz evaluation differences cancel the collision singularity for the noiseless estimator. Rescaling separations by \(\sqrt\eta\) and applying dominated convergence gives the exact ridge constant. The self-contained numerical verifier passed 47 diagnostic checks; these tests do not substitute for the analytic limit proof. Risks: the statements require independent Gaussian observation errors, exact arithmetic and the stated smooth Gaussian kernel.

## Originality — PASS (qualified)

The 2017 random-node kernel-quadrature paper considers random design but not this independent observation-noise collision law. The 2018 Gaussian/positive-weight literature explains weight instability and geometric conditioning but does not state this exact two-point random-collision tail and ridge asymptotic. The 2022 noisy Bayesian quadrature paper provides general noisy error rates and regularization methods, not the displayed two-node singular tail constant. The 2023 sampling-based Nyström study uses random landmarks with different objectives. The joint tail–moment–ridge classification is not implied by their stated results without a new local random-collision calculation. Risk: classic inverse-Gram and numerical linear algebra estimates, or narrower specialist kernel quadrature sources, could contain an equivalent result not located in the checked literature; publication priority is not independently certified.

## Mathematical value — PASS

The calculation separates a uniformly bounded deterministic quadrature rule from an infinite-mean noisy implementation under the same random nodes. It gives the exact quantitative cost of regularization, including a precise noise-matched mean-square scaling relevant to Gaussian-process Bayesian quadrature design. The objects are naturally motivated by random sampling and independent observational noise, and both exact constants and the critical exponent govern the practical failure mode. Limits: it is a two-point model rather than an arbitrary-node stability theorem.

Self-review: passed. Independent audit: not yet performed.
