# Scientific review: finite voting-cost spectra

## Correctness — PASS

The model fixes strict participation only when the advantage over the competing platform exceeds the cost. For separated platforms, a cost type below the separation contributes exactly a voter-CDF term with argument \((a+b-c)/2\) for the left candidate. Finite support permits a small move toward the opponent without changing which cost types participate. Full support makes each active CDF term increase strictly. All possible equilibria must therefore have no participating cost types; checking unilateral deviations to the policy endpoints gives exactly \(I^2\). The thresholds \(1/2\) and \(1\) include equality cases. The empirical-CDF bound is proved interval by interval, and the limiting \((1/4,3/4)\) best responses follow from exact quadratic maxima. The code checks representative rational profiles but the proof does not depend on enumeration.

## Originality — PASS under accessible-source comparison

The primary 2026 source analyzes cost distributions with densities and reports a positive-turnout quartile equilibrium under uniform distributions, whereas the submitted claim treats every finite atomic cost spectrum and derives a universal no-positive-turnout dichotomy and uniform-approximation failure. The governing hypotheses and implications differ: a theorem for a continuous CDF/density does not apply to a finite-step CDF, and continuous-cost equilibrium cannot prove atomic-cost existence. Searches for finite cost atoms, deterministic cost thresholds, spatial abstention, and prior equilibrium classification found no logically equivalent theorem in the available materials or accessible research-record summaries. The strongest residual risk is unexamined material in the motivating manuscript's appendix or older political-economy work. An absence of retrieved matches is not taken as a uniqueness proof.

## Value — PASS

Voting-cost distributions are routinely discretized for computation and simulation. Here a finite approximation whose CDF is within \(1/(m+1)\) of the uniform law eliminates pure equilibria entirely for every \(m\geq2\), while preserving a quantitative approximate-equilibrium guarantee. This is a structural warning about exact-equilibrium inference, not a single numerical counterexample: the classification is uniform over all atomless full-support electorates, every finite set of cost atoms, and all positive masses. It pinpoints the strictly positive minimum cost, rather than other parameters, as the exact existence threshold.

## Closest literature and remaining limitations

Wolf and Meir, arXiv:2609.29869v1 (September 24, 2026), is the motivating source and supplies the continuous-cost comparison. Nikram's generalized Hotelling–Downs tournament game and Barelli's majority contest analyze different voting/payoff structures. The available portion of Wolf and Meir's primary HTML and its indexed contribution statements were read, but the complete appendix could not be retrieved; priority checking is therefore not exhaustive. The theorem excludes mixed continuous-atomic costs, strategic voter participation, winning-probability payoffs and alternative indifference conventions.

Self-review: passed. Independent audit: not yet performed.
