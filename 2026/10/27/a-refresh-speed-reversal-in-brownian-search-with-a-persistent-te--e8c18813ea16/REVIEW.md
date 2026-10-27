# Scientific review: a refresh-speed reversal in Brownian search

## Correctness — PASS

The claim is an exact statement for one-dimensional Brownian motion with a symmetric two-state environmental Markov chain; conditional resetting rates are strictly positive, and position resets leave the environmental state intact. Both the nonlocal backward boundary equation and a distinct environment-preserving renewal-kernel construction lead to the same matrix-square-root formula. The renewal kernel has row sums strictly below one, justifying finite mean absorption and the inverse without assuming that the environment restarts. The slow-switching limit follows by continuity of the matrix formula and a strictly positive closed form for the second derivative of the ordinary Brownian reset-search mean. The fast-switch expansion is obtained by diagonalizing the two-state killing matrix and retaining the low eigenvalue shift and spectral-projector coupling through order \(1/\nu\). The unique positive root in the derivative of the ordinary reset-search mean supplies the sharp sign condition. The proof asserts the existence, not uniqueness, of a finite switching-speed crossover.

An independent renewal representation was compared with the boundary-value formula across evaluated parameter cases, and a discrete-space absorbing/reflected generator was solved in four test cases. The packaged verification program passed 176 deterministic assertions. The boundary-value and renewal identities, not these finite tests, bear the infinite-parameter and asymptotic arguments. The leading special-function threshold is already classical and is not separately claimed as a discovery.

## Originality — PASS with explicit residual risk

The most directly relevant source is Arutkin and Reuveni, *Diffusion with doubly stochastic resetting* (arXiv:2509.25365, 2025). Its stationary Fourier law uses a reset intensity that survives individual position resets and its conclusion identifies first-passage questions as open directions; the accessible text develops stationary spatial laws rather than first-passage switching-speed inequalities. The known stationary-density decompositions do not, by themselves, determine the absorption-time sign reversal.

Barman, Nandi and Das, *Optimizing search processes in systems with state toggling* (arXiv:2410.06933; Physical Review E 111, 024142, 2025), analyze a Brownian searcher with a *constant* reset intensity and environmentally switching drift. Their methods justify that environmental state should be tracked across a spatial reset, but their parameter comparisons do not include two environmentally modulated reset intensities at fixed mean. The present differential problem is not obtained merely by choosing an environmental drift in their stated specialization. Work on stochastically gated targets and ordinary Poisson restart likewise addresses different couplings.

Searches for telegraph/Cox/Markov-modulated reset intensity, first passage, fast switching, and convex-order or rate-variance comparisons did not identify an implication-equivalent published claim among sources inspected. These searches do not prove novelty. The clearest unresolved risk is a general matrix-resolvent or Markov-modulated first-passage theorem that may imply the full result, potentially without explicit mention of this model; independent literature assessment is not yet performed.

## Value — PASS

The two reset intensities have the same stationary mean as their constant-rate comparator, and the environmental switching time is a natural experimentally adjustable scale. Slow fluctuations introduce a strictly unfavorable persistent-rate mixture for *every* nonzero amplitude. Above a precise and physically distinguished benchmark—the classical optimal Brownian reset rate—the sign reverses in the fast-switch regime. This provides a falsifiable model-specific control principle, not an arbitrary numerical correction or a restatement of the traditional reset optimum. Its proof also identifies the correct environmental-state renewal operator, useful for extensions with more rate states.

## Boundaries and source risk

The result does not classify the critical mean rate at which the first fast-switch correction vanishes; does not assert that the crossover is unique; and does not extend to asymmetric switching, active drift, resetting the environmental state, or simultaneous singular limits. The exact finite-switching matrix formula is proved within the stated model, but publication priority has not been independently established. The main-text HTML of the motivating paper and the complete relevant mathematical sections of the closest toggling paper were inspected. Broad general results not located by targeted search remain possible implicit coverage.

Self-review: passed. Independent audit: not yet performed.
