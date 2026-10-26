# Scientific assessment

## Correctness — PASS

The exact single-edge flow is a positive column-stochastic map for every finite positive step. All six three-edge compositions contract the two-dimensional zero-sum subspace. Cyclic symmetry implies an unbiased stationary mean and isotropic stationary covariance; direct enumeration yields the scalar covariance fixed point and the displayed rational error. The two deterministic stationary bias classes are explicit. Sign factorizations and a strictly increasing crossover polynomial prove the universal sharp comparison. The packaged SymPy reproducer verifies the nontrivial algebra; it is not used as an infinite-domain proof.

## Originality — PASS, within documented search scope

Blanes–Iserles–Macnamara (arXiv:2102.08242) motivates positivity-preserving graph-Laplacian exponentials. Gourgoulias–Katsoulakis–Rey-Bellet (arXiv:1511.08240) studies long-time relative-entropy splitting error for CTMC path laws, not invariant covariance of independently permuted distribution-vector integrators. Childs–Ostrander–Su (arXiv:1805.08385) and Jin–Li (arXiv:2109.07987) study randomized unitary simulation rather than Markov equilibrium error. The abstract of Speth–Green–Macnamara–Strang (doi:10.1137/120878641) concerns corrected deterministic balanced splitting; only its abstract and repository metadata were inspected and fuller coverage remains a risk. Targeted published-literature and mathematical-record searches did not reveal an exact or stronger covering statement; this is evidence-limited novelty, not proof that none exists.

## Mathematical value — PASS

The phenomenon occurs at equal implementation cost on a natural minimal noncommuting Markov cycle. The exact crossover distinguishes a small-step regime where randomization improves the stationary squared-error order from a large-step regime where the best deterministic ordering wins. The calculation clarifies which equilibrium statistic, rather than positivity or transient operator norm, governs the comparison.

## Limitations and priority risks

Only three equal-rate directed edges with uniform independent order selection are treated. Errors measure evolving probability vectors, not individual simulated CTMC trajectories. The balanced-splitting full text was not examined and specialized stationary random-product literature may contain equivalent examples. The comparison has not received an independent literature or scientific audit.

Self-review: passed. Independent audit: not yet performed.
