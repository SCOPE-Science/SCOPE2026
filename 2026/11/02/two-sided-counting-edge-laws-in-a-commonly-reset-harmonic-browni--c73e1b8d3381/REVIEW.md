# Scientific review — Two-sided counting-edge laws in a commonly reset harmonic Brownian gas

## Correctness — PASS

For positive fixed \(\mu,D,r,a\), the one-clock stationary renewal representation gives an exponential reset age and independent Gaussian particle positions conditional on that age. The exact transformation \(Y=e^{-2\mu T}\) yields a beta density; conditional counting is binomial. Strict monotonicity of \(q(Y)\), differentiation and a Gaussian Mills expansion prove the compact-support limit and both density-edge laws. The lower-edge finite-population theorem follows by uniform binomial central-limit scaling after \(y=z/(B\sqrt N)\), with Hoeffding domination. The all-inside event follows from a two-threshold Tauberian sandwich. The zero-endpoint Gaussian integral coefficient was checked independently using the gamma integral; the standalone checker passed deterministic finite-population, inverse-CDF and asymptotic-consistency checks. No claim relies on finite computation as a proof of an infinite statement.

## Originality — PASS, with identified residual risks

The broad conditional-IID mixture method is not original. The 2025 unconfined-gas full counting results (arXiv:2509.06658) already cover counting statistics without a harmonic restoring force; they do not state a positive equilibrium counting floor or its finite-size boundary exponent. The 2026 confined-gas work (arXiv:2606.31634) provides the Gaussian mixture and analyzes density/correlations/edge order statistics; the accessible original abstract does not assert this explicit center-window counting theorem, and a detailed scientific reading identifies counting statistics as a topic left for further investigation. A 2025 resetting Dyson gas (arXiv:2503.14733) treats interacting particles and hence differs in both the conditional law and its edge scaling. Published research-record searches for simultaneous-reset counting and related equivalents returned nearby OU extremes, OU sensor thresholds and oscillator results, not this two-sided counting-edge theorem. Accessible prior claims concerning common-reset OU maxima and partial-reset Brownian tail events were checked for implication, not treated as novelty proof.

The two most important risks are an uninspected appendix or updated full text of the 2026 confined-gas source and an unlocated generic binomial-mixture edge theorem that implicitly gives the finite-population \(N^{-r/(4\mu)}\) scale. The relevant primary full texts could not all be obtained for full-section comparison. These access limits are disclosed rather than being classified as negative evidence.

## Value — PASS

Counting the fraction of a confined population within a fixed sensor region is a natural bulk observable, complementary to the maxima and gaps studied in the motivating literature. The result gives exact finite-population event probabilities, a sharp continuously tunable exponent, a transition between divergent and vanishing lower-edge densities at \(r=2\mu\), and a contrasting universal inverse-logarithmic all-inside law. These provide quantitative rare-event predictions and a sensitive distinction between long and short common-reset ages; the point is not merely the known conditional-binomial formula. The result is narrow to one natural physical model and does not purport to give a general theorem for interacting gases.

## Closest literature and limitations

De Mauro, Majumdar and Schehr, arXiv:2606.31634 (2026): harmonic confinement, common resetting, stationary Gaussian mixtures, extreme and gap observables. De Mauro, Biroli, Majumdar and Schehr, arXiv:2509.06658 (2025): full counting statistics for unconfined noninteracting Brownian gases under renewal resets. Biroli, Majumdar and Schehr, arXiv:2503.14733 (2025): interacting Dyson Brownian counting under resetting. The proof requires positive fixed parameters, common Poisson resets to the trap center, a centered observation window and independent OU particles; it does not establish uniformity under changing parameters. Independent priority and proof audits are unperformed.

Self-review: passed. Independent audit: not yet performed.
