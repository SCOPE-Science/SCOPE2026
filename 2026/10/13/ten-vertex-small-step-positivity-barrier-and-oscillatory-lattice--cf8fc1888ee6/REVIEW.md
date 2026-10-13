# Scientific self-review

## Correctness: PASS

The finite-cycle sharp cutoff follows from the explicit Radau IIA rational function, its exactly reconstructed coefficients through order five, and shortest-path support of powers of the symmetric nearest-neighbor generator. The infinite-lattice claim follows from an exact conjugate-resolvent decomposition, the unique decaying Green root \(q\) with \(0<|q|<1\) and nonzero imaginary part, and a periodic/dense rotation argument producing infinitely many negative kernel entries for each \(h>0\). Absolute convergence justifies periodization and transfer to arbitrarily large cycles. The limit of the spectral multiplier on a fixed cycle proves eventual positivity. Exact-rational matrix tests and floating-point kernel diagnostics supplement, but do not replace, these proofs. The theorem does not state a complete positivity-interval classification for finite cycles.

## Originality: PASS, with residual historical risk

The closest primary source is Horváth's 2004-online/2005 paper on strict Runge–Kutta positivity thresholds (DOI: 10.1016/j.apnum.2004.08.026): its Table 1 explicitly finds a zero universal positivity threshold for two-stage Radau IIA on Dirichlet heat problems, but it gives neither the sharp periodic cycle threshold of ten vertices nor the all-positive-timestep infinite-lattice alternating-sign Green kernel. Horváth's 1998 general positivity theory (DOI: 10.1016/S0168-9274(98)00050-6) likewise does not provide these cycle- and kernel-specific statements. A published eight-state Gauss–Legendre Padé Markov barrier concerns a different rational function and directed generator; a backward-Euler-filtered Crank–Nicolson result has a different, strictly positive lattice kernel. Zappavigna et al.'s 2012 Padé examples do not imply these Radau-on-cycle conclusions. Full or substantial relevant source texts were inspected; unlocated equivalent specialized literature remains possible. Search nonappearance is not a proof of novelty.

## Value: PASS

This is not only a formal Taylor sign check: it identifies the exact finite periodic lattice size where arbitrarily-small-step positive-semigroup consistency ceases to preserve the nonnegative cone and proves, through a complex-pole Green-function mechanism, that *every* positive step has negative influence at infinitely many infinite-grid distances. The transfer theorem rules out every mesh-independent positive timestep, while L-stability produces eventual positivity on each fixed finite cycle. This quantitative topology and finite/infinite distinction is motivated by mass/positivity requirements in numerical heat diffusion and has a complete analytic proof. The exact small-step threshold and the all-step infinite obstruction are meaningful as a combined statement, even though extremely distant negative coefficients may be small.

## Scientific scope and limitations

The theorem is for symmetric unit-rate nearest-neighbor cycles and the infinite line, the standard two-stage order-three Radau IIA end-step, and exact arithmetic. It does not classify every finite-step positivity window or extend to nonlinear PDEs, nonnormal matrices, boundaries, or internal stages. The stronger historical-specialization priority question is not independently certified.

Self-review: passed. Independent audit: not yet performed.
