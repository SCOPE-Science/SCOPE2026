# Scientific review

## Correctness — PASS

Each conflict edge is violated exactly when its endpoint-position difference equals the difference of two independent uniform block shifts. Distinct block-pair differences are pairwise independent, even on an interaction cycle; this proves the exact additive variance identity without presuming joint independence. The sharp integer extrema follow by strict balancing and concentration of sums of squares under the feasible histogram bounds. Every histogram is realized by selecting edges within disjoint offset matchings. Fourier inversion and character orthogonality prove the full distribution; spanning-forest elimination counts admissible flows and establishes joint independence exactly for forest-shaped interactions as a general guarantee. The explicit triangle demonstrates possible dependence on cycles. The finite independent calculations in `verify.py` corroborate, but do not prove, the unbounded quantifiers.

## Originality — PASS, subject to historical-priority risk

The closest inspected primary source is Yoneda and Yoneda, *Fair Division with Soft Conflicts* (arXiv:2602.20929v1), especially Section 4, which proves cyclic-round-robin EF1 and derives the mean/conditional expectation benchmark but does not derive the complete random-shift law, the variance envelopes, or the interaction-graph independence criterion. A relevant older full-text mathematical source, Huijben, Patel, and Regts, *Sampling from the low temperature Potts model through a Markov chain on flows* (DOI:10.1002/rsa.21089), develops general finite-group graph flows in a Potts context. That standard Fourier method is credited, and the generic flow expansion is not separately represented as original. Searches for equivalent randomized round-robin conflict-distribution results and checks against accessible mathematical research records identified no specific dominating theorem. Other graph-spin formulations of the same distribution may exist, so priority remains uncertain.

## Mathematical value — PASS

A first-moment guarantee alone does not quantify fluctuations of the random EF1 baseline. Sharp conditional minimum and maximum variances describe exactly when random shifts are deterministic, nearly concentrated, or maximally unstable at fixed block-pair conflict density. Simultaneous attainability makes these genuine worst-case bounds rather than loose inequalities. The forest law gives an exactly computable full distribution by convolution, while the triangle exhibits a minimally sized obstruction to assuming joint independence. This is a structural fairness-versus-conflict variability result, not a textbook restatement of independent hashing: the shifts are shared by all goods within each ranked EF1 block.

## Risks and boundaries

The results are confined to identical additive values and independent random block rotations. They do not concern the deterministic min-cost-shift algorithm's own output distribution; within-block conflict edges are never violated. The methodology for the Fourier expansion is established in prior graph-flow literature. No claim of external or independent verification is made.

Self-review: passed. Independent audit: not yet performed.
