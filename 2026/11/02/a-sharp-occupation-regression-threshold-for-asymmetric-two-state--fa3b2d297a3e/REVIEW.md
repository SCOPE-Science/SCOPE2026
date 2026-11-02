# Scientific review

**Correctness — PASS.** Explicit alternating-path densities give the tilted-beta conditional occupation law. Folding about half occupation yields a likelihood-ratio order with ratio proportional to \(1-a^2\), and the conditional sign mean has derivative of the required sign exactly when \((\alpha-\beta)t\le2\). A beta exponential-tilt expansion yields the sharp necessity condition; checks in `verify.py` corroborate representative regimes. The proof treats the no-switch atom separately and covers all positive rates and times.

**Originality — PASS, residual risk retained.** Searches considered exact conditional occupation distributions, number of jumps, asymmetric telegraph bridges, likelihood-ratio monotonicity, and the threshold. The closest readable bridge note derives an equal-rate beta law for another observable, while the Kovchegov–Meredith–Nir and Bogachev–Ratanov references concern occupation-time densities. Roldán–Vivo's published work concerns discrete-time bridges. Colwell's abstract addresses Markov jump-count and occupation formulas; full text was not inspected. No inspected result states or immediately implies the precise signed-regression threshold without additional folding/order analysis. Historical priority remains uncertain, particularly given older joint occupation-law research.

**Value — PASS.** In a two-rate Markov bridge, changes in the number of return cycles alter the expected residence fraction in a qualitatively different way across a sharp dimensionless parameter. A universal monotone concentration law survives asymmetry while signed occupation regression reverses. These are natural diagnostics of dynamical imbalance, not arbitrary parameter slices.

Self-review: passed. Independent audit: not yet performed.
