# Review: shared-clock quantum-walk correlation anomaly

## Correctness — PASS

The stationary state is a trace-class exponential-age mixture and is unique by reset contraction. The single- and double-walker collision traces reduce to the second and fourth powers of the same Bessel return overlap using an exact two-age convolution. Strict Jensen proves the shared-versus-independent purity separation. A standard complete-elliptic-integral representation supplies the logarithmic one-body scale, and absolute integrability of the fourth Bessel power plus dominated convergence supplies the linear two-body scale. These steps determine the multiplicative purity ratio and additive \(o(1)\) entropy remainder for every fixed hopping strength. The executable checker supplies independent finite consistency tests but is not treated as proof of the limiting theorem.

## Originality — PASS (self-review)

Wald–Böttcher (arXiv:2008.00510) establishes the individual stochastic quantum-walk reset framework. Das–Dattagupta–Gupta (arXiv:2106.14181) establishes detailed one-particle tight-binding results, including the stationary origin-site probability that already implies the displayed marginal-purity formula. That marginal calculation is expressly **prior-implied**, not claimed separately as an original theorem. The combined statement compares two-walker protocols whose marginal density matrices agree exactly, gives a strict separable joint-purity distinction, and derives a sharp diverging logarithmically corrected order-two entropy contrast. The primary texts were checked against joint resetting, tensor state comparisons, purity and collision entropies. No covering result was found in the inspected materials or semantic record searches, but broad renewal-process/channel entropy identities remain a legitimate priority risk. Independent literature assessment remains necessary.

## Scientific value — PASS

This is a motivated global-versus-local control question: single-walker state tomography cannot distinguish a common reset clock from independent clocks, but second-order joint state measurements can, with a surprisingly unbounded entropy contrast in the weak-reset regime. The exact \(r^{-1}(\log r)^{-2}\) purity ratio and precise entropy scaling provide a quantitative many-body benchmark even without inter-particle interactions or entanglement. It is not merely a re-expression of a known single-walker localization probability.

## Scope and residual risks

The theorem fixes two distinguishable free lattice walkers and global product resets. No finite-sample measurement protocol or uniform finite-size limit is established. The order-two contrast is not general quantum mutual information, and broad shared-randomness correlation theory could imply the result by a stronger theorem. Independent priority review has not been conducted.

Self-review: passed. Independent audit: not yet performed.
