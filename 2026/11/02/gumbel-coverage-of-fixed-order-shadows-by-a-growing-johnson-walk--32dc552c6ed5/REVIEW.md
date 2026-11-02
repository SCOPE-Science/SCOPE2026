# Scientific review: growing-block Markovian super-coupon coverage

## Correctness — PASS

The exact projected transition kernel is derived directly from the single-swap rule; stationary initialization is the hypergeometric marginal. For any fixed number of marked \(s\)-sets, this yields a state space bounded independently of \(n\) even though \(r_n\to\infty\). The pure-death comparison has an explicit zeta-basis of eigenvectors, so the spectral separation on scale \(1/r_n\) and the uniform projector perturbation are justified. Stationary entrance flux is exactly \(\binom{r_n-1}{s-1}/\binom ns\) for one target; simultaneous-target corrections are relatively \(O(r_n/n)\). Excursion counting and the first-return transform identify the killed eigenvalue to the same relative accuracy. The condition \(r_n\log n=o(n)\) makes this error negligible in the Gumbel window. Uniform fixed-order factorial moments yield Poisson and Gumbel limits; a geometric tail sum gives the mean asymptotic. An independent implementation of the full chain and the finite projection passed 396 exact-rational checks. These checks support only the finite identities; the analytic lemmas provide the infinite proof.

## Originality — PASS, qualified

The 2023 super-coupon paper explicitly formulates the single-replacement model and conjectures its mean cover-time scale, while the open-access 2025 journal text proves only the state-cover case and proves a Gumbel law for *independent* draws. The already-known fixed-\(r\) Markovian Gumbel law does not apply uniformly to \(r_n\to\infty\); the new proof supplies an explicit \(O(r_n/n)\) rare-event-rate estimate and handles all allowed diverging block sequences. Opposite dense-block results with \(r_n=n-k\) concern a disjoint parameter range. General Markov-chain cover-time theorems not located in the search could still subsume the result; no database-search failure is treated as proof of novelty.

## Mathematical value — PASS

The source problem asks how temporal dependence changes coverage when one label is replaced per step. A growing retained block is a natural intermediary between a fixed-sized moving subset and a macroscopic subset, and fixed-parameter convergence cannot answer it. The theorem supplies the entire Poisson count and Gumbel completion profile, not only the expectation, and identifies an explicit growth window in which the per-update innovation scale remains valid. It therefore supplies a motivated boundary and an interpretable \(r_n^{s-1}\) speed-up rather than an arbitrary parameter substitution.

## Limitations and risks

The growth condition is sufficient, not shown sharp. The target order must be fixed; the chain must begin in stationarity. Some potentially applicable general cover-time results may remain unindexed or use a different terminology. The argument concerns a specific finite-state Markov projection and does not imply asymptotic independence of all missed-target indicators simultaneously. The exact finite checks cannot certify the analytic limits.

Self-review: passed. Independent audit: not yet performed.
