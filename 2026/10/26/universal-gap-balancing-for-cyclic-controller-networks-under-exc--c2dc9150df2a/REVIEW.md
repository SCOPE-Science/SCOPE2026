# Scientific review

## Correctness

PASS. Every non-controller vertex lies in a unique controller gap. It is nondeleted and unserved precisely when each of its two internally disjoint paths toward the neighboring controllers contains a deleted vertex. Inclusion-exclusion gives the exact fixed-cardinality count, and conditioning on the failure count handles any exchangeable law. Pascal identities give a nonnegative discrete second difference of the gap penalty; balancing improves every fixed-cardinality expectation and hence every mixture. Under the stated positive-mass or fixed-cardinality condition, strict convexity at every nonbalanced transfer gives the exact gap characterization. The independent-failure identity follows from disjoint path events. Exhaustive integer checks corroborate all small cases and the required algebraic identities.

## Originality

PASS on the inspected evidence, with stated residual priority risk. The 2026 motivating paper studies worst-case and strategic mixed attacks on general graphs, not a permutation-exchangeable failure law with an exact all-budget cycle formula. The closely related 2023 mixed-game paper explicitly uses antipodal controllers on a cycle for a particular two-controller strategic equilibrium, which is acknowledged as existing prior art. That equilibrium does not imply optimality for every fixed failure count, every controller count, and every exchangeable law, nor the new gap-convexity identity. Searches for equivalent or stronger all-budget stochastic cycle statements did not identify coverage; indexing incompleteness and unpublished related network-reliability analyses remain priority risks.

## Value

PASS. The result solves a natural robust placement question for ring communication networks: a single geometry of controllers is optimal across all exchangeable failure distributions, including correlated failures, without knowing the attack-count law. The exact outage expression quantifies risk as a function of controller gaps, and the strict equality result rules out unbalanced designs when two-site failures have positive probability. This is useful beyond the previously analyzed special strategic equilibrium and distinguishes best average service from worst-case attack guarantees.

## Limitations and closest sources

The result concerns expected served-vertex count only, not a distributional stochastic ordering, heterogeneous networks, or adaptive attacks. Closest literature: Gutowski et al., arXiv:2605.17572v1; Pióro et al., DOI:10.1109/RNDM59149.2023.10293051; Junosza-Szaniawski and Nogalski, DOI:10.1109/ICMCIS59922.2023.10253594. The 2023 cyclic strategic-equilibrium example is an important overlap comparator rather than a novelty source. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
