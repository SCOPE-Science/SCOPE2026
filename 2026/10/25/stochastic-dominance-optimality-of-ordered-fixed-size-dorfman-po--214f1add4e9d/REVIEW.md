# Scientific review: ordered fixed-size Dorfman pooling

## Correctness — PASS

For independent people, the count of positive pools is a sum of independent Bernoulli variables with negative probabilities given by products of individual noninfection probabilities. Sorting and taking equal consecutive blocks majorizes **every** other group log-negative-probability vector, because its largest \(r\) blocks use the largest \(rk\) individual log-probabilities. A logarithmic two-pool spread keeps the product of negative probabilities fixed and increases their sum; the probabilities of at least one and at least two positives therefore respectively stay fixed and decrease. Majorization's finite transfer characterization and convolution establish first-order stochastic dominance of test workload for all pool partitions. Strict convexity of the exponential gives the exact equality characterization. For size-two pools, integrating the signed mixed derivative of \(st(1-st)\) and applying the four-point exchange proves the half-risk variance reversal. An exact standalone verifier establishes all reported finite checks; the proof is analytic and independent of finite enumeration.

## Originality — PASS, with explicit bibliographic residual risk

Dorfman (1943) gives the homogeneous expectation/variance baseline. Black–Bilder–Tebbs (2012) study halving protocols; Aprahamian–Bish–Bish (2019), especially Theorem 1, provide expected-objective ordered-partition optimality but not an arbitrary-threshold distributional inequality. Bobkova–Chen–Eraslan (2023) modify the second stage by conditional last-test omission; their negative-assortative optima apply to this different protocol. Saraiva (2026) studies expected savings from positive assortative matching, as confirmed by its accessible abstract; its full text was not inspectable. Majorization/Poisson–binomial related research using fixed pair sums does not imply the fixed-product pool transfer here. The exact claim and its pairwise variance reversal were compared to research-record summaries and primary material under aliases; a search with no hit is not proof of novelty, and an independent literature audit remains outstanding.

## Mathematical value — PASS

Capacity planning in screening depends on the probability of exceeding each available assay budget, not just expected consumption. The theorem delivers simultaneous control of all upper tails for every heterogeneous risk vector, equal pool size, and feasible partition, with no approximation or low-prevalence restriction. The exact characterization of distributional ties and the 50% pairwise variance reversal show why this stronger guarantee should not be mislabeled a variance-minimization result. It is nontrivial across arbitrary partitions and operationally motivates checking the full workload law.

## Limitations and closest-source uncertainty

This is an idealized independent, perfect-test, fixed-size, full-Dorfman-retesting theorem; neither correlated infection nor variable group sizes nor imperfect assays are covered. Full-text inspection of the Saraiva (2026) source was not possible, leaving a bibliographic risk; related reviews of majorization under alternative terminology may exist. Finite certificate cases supplement but do not establish the general proof.

Self-review: passed. Independent audit: not yet performed.
