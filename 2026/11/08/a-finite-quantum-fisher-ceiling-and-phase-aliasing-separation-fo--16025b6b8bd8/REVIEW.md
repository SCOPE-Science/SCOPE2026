# Self-review

## Correctness — PASS

The stationary reset age is an exponential random variable. Folding it modulo the physical Rabi period gives the exact one-dimensional hidden phase density. The score identity for every POVM follows by differentiating the mixed outcome law; its conditional variance yields a universal quantum Fisher ceiling. Alternating local \(\sigma_y\) and \(\sigma_z\) data asymptotically identify the phase, and the bounded-score martingale closes the information bound. An exact reflection argument establishes the strict \(\sigma_z\)-only gap; a uniform weak-rate expansion supplies its quadratic coefficient. The independent-clock control is computed from one Bernoulli marginal. A standalone numerical verifier reproduced 320 diagnostic assertions, including density-matrix quantum Fisher checks, normalization, finite population likelihoods, and asymptotic constants. Diagnostics do not prove the infinite limits.

## Originality — PASS, with publication-priority risk

Magoni et al., arXiv:2202.12655v1, establishes the noninteracting common-reset spin model, its renewal stationary state, density correlations and local quantum uncertainty. These are acknowledged inputs. Smiga et al., arXiv:2305.16480v1, treats information in temporal stochastic records, and Radaelli et al., arXiv:2206.00463v1, proves finite-Markov-order correlated-record Fisher statements. None of the inspected material derives the exact global-reset stationary quantum Fisher ceiling, proves asymptotic attainment by fixed local readouts, or identifies the differing orders of weak-reset information between two observation schemes. Classical data processing and martingale convergence are standard tools, not novel contributions. A recent reset-metrology preprint, arXiv:2610.31249v1, was only accessible through secondary material, so its full text is a named priority risk, as is broader unindexed literature.

## Mathematical value — PASS

The result answers a natural experimental inference question: whether increasing the number of correlated spin probes allows arbitrarily precise estimation of their common reset clock. It supplies a sharp finite resource-independent limit and a physically realizable optimal measurement. The \(\sigma_z\)-only weak-reset information collapses while complementary phase-sensitive measurements remain informative. Independent reset clocks restore extensive information, isolating common-age correlation as the obstruction.

## Limits of the reviewed claim

Only a stationary, single-snapshot, noiseless, noninteracting Rabi model with a common complete Poisson reset clock and known Rabi frequency is covered. No finite-ensemble quantum Fisher closed formula, estimator efficiency, repeated-snapshot inference, or noisy-hardware guarantee is asserted. Population limits precede rate limits. Priority has not been independently confirmed.

Self-review: passed. Independent audit: not yet performed.
