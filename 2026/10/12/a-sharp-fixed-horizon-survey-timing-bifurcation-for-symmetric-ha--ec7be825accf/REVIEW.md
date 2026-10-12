# Scientific review: fixed-horizon occupancy-survey timing

## Correctness — PASS

The claim is conditional on a stationary symmetric two-state occupancy chain, exact state observation at three fixed-count visits, known common switching-rate structure, and an unknown positive rate scale. Direct Bernoulli score differentiation yields the exact information \(f(\lambda u)+f(\lambda(H-u))\) for \(\log\lambda\). A coefficient-sign proof shows that \(f''\) has exactly one positive zero and that \(f^{(4)}\) also changes sign exactly once, strictly later. Their derivative ordering supplies the global fixed-horizon optimizer classification, including all equality cases. The packaged exact-recurrence/finite-coefficient verifier was executed and its output inspected. Infinite coefficient tails are proven positive using explicit quadratic factors, not numerically truncated. The large-horizon limit follows by compactness and the unique one-gap maximum.

## Originality — PASS, qualified

The underlying binary Markov model and single-gap Fisher information are established. Royle and Kéry (2007) supply ecological turnover motivation. Brown, Solomon and Stephens (1977) and Mehtälä, Auranen and Kulathinal (2011/2015) address interval sampling. Mehtälä and colleagues' 2014/2015 multistate paper is a close comparison whose accessible summary describes optimal time spacing for stationary multistate Markov estimation. Michel's 2018 preprint (full mathematical sections inspected) obtains a unique freely chosen common interval asymptotically and an adaptive interval policy, not the finite fixed-first/fixed-last three-visit phase diagram. No searched evidence explicitly supplied the sharp dimensionless boundary \(2a\) or two asymmetric global optimizers. Inaccessible full-text treatment of fixed endpoint constraints in the Mehtälä work remains a material risk, and the absence of a search match is not asserted as a proof of novelty.

## Value — PASS

A fixed monitoring start and end with just one discretionary interior visit is a natural field-survey constraint; optimizing that visit differs substantively from choosing a free repeating interval. The theorem locates a sharp structural change from midpoint sampling to two asymmetric schedules and quantifies the optimal short gap at long horizons. It is a self-contained exact design benchmark, not an arbitrary parameter slice. The theorem does not transfer automatically to noisy occupancy observations, unequal transition rates, unknown stationary probabilities, or heterogeneous sites.

## Closest literature, constraints, and risks

The closest full mathematical source is Michel (2018), whose freely spaced model contains the same one-interval information but a different constrained optimization problem. The two Mehtälä studies and Brown et al. are closely relevant; complete primary texts were not all available, so their possible stronger fixed-horizon implications remain a genuine novelty risk. Observability, stationarity, rate symmetry, local optimality at a known parameter, and endpoint constraints are essential. High-precision numerical constants and grids corroborate but do not replace global derivative proofs.

Self-review: passed. Independent audit: not yet performed.
