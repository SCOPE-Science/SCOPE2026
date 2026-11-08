# Independent mathematical audit

## correctness

PASS

The exact binomial propagator gives E||X_n||²=|x1|²q_a^n+|x2|²q_b^n. F_c(u)=u(1-e^{-c/u}) is strictly increasing; thus q_a decreases and q_b increases in p, their crossing uniquely minimizes the max, and at p=1/2 the faster mode q_a<q_b. The rare-event scaling follows by monotone inversion p_h/h->kappa; Bin(n_h,p_h) converges to Poisson(kappa T), whose nonconstant fast multiplier gives positive nonconsistency error. Uniform fixed-p LLN recovers deterministic limit. Large-h crossing expansion checked separately. Independent small-h grid and explicit finite switching-word checks corroborated but do not prove the all-real assertions.

## originality

PASS

The precise minimax *expected squared propagated energy* is different from earlier generator-variance optimization: Veldman–Zuazua Example 3 gives p_var=a/(a+b)>1/2 for the same two-block generator, whereas the present h-dependent optimum has p_h<1/2 and p_h~kappa h. Their fixed-probability convergence estimates do not imply the rare-event Poisson-jump error. Eisenmann–Stillfjord use a different implicit randomized update. Resultary inverse-positive coordinate-sampling result optimizes discrete coordinate-descent energy for a different map, not these exact subflows.

## value

PASS

A concrete motivated counterexample to identifying optimal expected energy decay with approximation accuracy: even matching the exact semigroup worst-mode decay yields nonconvergence of individual state trajectories. Opposite probabilities for variance and contraction and an explicit rare-event process identify the mechanism rather than a numerical artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
