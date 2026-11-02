# Scientific review

## Correctness — PASS

The independent-occupancy identity follows exactly from the period-\(d\) class itinerary and independent uniform vertex labels. The central strict log-concavity inequality for the coupon-collector CDF follows from a geometric-sum representation, log-concavity under convolution, and a termwise ratio estimate; it is not merely observed numerically. Circular floor-difference starts make every partial-period visit profile balanced, giving stochastic order at all integer horizons; strictness for any nonbalanced circular window gives the if-and-only-if classification. The occupancy factorial-moment argument proves the subsequential Poisson scaling with the correct period offset and Jensen's inequality gives its nonnegative imbalance penalty. All six allocations for the unequal-size counterexample were evaluated as exact fractions. A standalone checker passed 190,907 exact finite assertions and directly enumerated small walker trajectories. Computation is corroboration, not an infinite proof.

## Originality — PASS, qualified

The nearest primary paper is Rivera–Sauerwald–Sylvester (arXiv:2011.07893, 2020-11-16): it establishes expectation bounds for parallel walk cover times on general finite undirected networks, with stationary and worst-case starts. Its results do not characterize a whole-distribution optimum for directed periodic multipartite walks under deterministic class-count starts. Kim–Lawley (arXiv:2310.07905, 2023-10-11) studies a different continuous-time large-searcher regime on discrete networks; its general cover-time inclusion-exclusion does not establish the circular stochastic-optimum or its equality cases. The 2007 work of Alon et al. addresses multi-walk cover-time speedups on undirected graphs. The universal occupancy formula and log-concavity tools are classical; only their all-horizon joint allocation optimization, exact equality classification, periodic-density law, and unequal-size boundary are proposed here as novel. Searches for synonymous cyclic-scheduling and coupon formulations did not identify prior implication-equivalent coverage. Literature that describes the same result under a different scheduling vocabulary may exist.

## Value — PASS

The problem asks where to place multiple independent stochastic searchers among periodic directed network classes to minimize the *entire* random cover time. A single explicit allocation works at every horizon and for all sizes, with an if-and-only-if classification instead of an expectation-only bound. At macroscopic walker density, the exact penalty quantifies when spatially uneven starts incur a persistent coverage loss. The unequal-class example demonstrates that this universal order is a structural effect of equal class capacities, not an automatic occupancy observation. These statements are motivated by stochastic resource allocation and parallel network coverage rather than a chosen numerical exception.

## Closest literature and residual limitations

Rivera–Sauerwald–Sylvester (https://arxiv.org/abs/2011.07893) and Kim–Lawley (https://arxiv.org/html/2310.07905) are the closest inspected papers. Full author-independent review has not occurred; priority remains qualified. Scope is synchronous directed complete cyclic classes, uniform conditional start labels, and the stated integer-time subsequence regime. Coverage at different times can be optimized by different allocations if class sizes are unequal.

Self-review: passed. Independent audit: not yet performed.
