# Scientific review of Poisson-reset absolute-area extremes

## Correctness — PASS

The statement is scoped to independent complete renewal cycles. The path functional has the exact distributional factorization \(A=T^{1+\beta/2}Y\). The Gaussian shape factor satisfies a logarithmically sharp quadratic tail by comparing with its signed Gaussian integral and applying Borell concentration to the supremum representation of the absolute area. The maximal variance \(v=4K/((\beta+1)(\beta+2))\) is attained by the constant sign, because the covariance kernel is nonnegative. A one-dimensional strictly convex saddle then proves the exact log-tail constant. The i.i.d. maximum and its duration follow from rare-event counting and a joint constrained Laplace bound; the order-statistic mismatch is strict because the selected fraction is smaller than one. The physical-time version uses renewal-count sandwiches. The independent code checks 276 algebraic/numerical identities; it cannot certify probabilistic limits.

## Originality — PASS (qualified best knowledge)

The closest directly motivating source is Méndez–Cristín, arXiv:2610.19985 (Sections IV.1 and VI.1), which derives Poisson-reset absolute-area moments and large-reset-interval extremes in power-law regimes, not the joint Poisson extreme-area/duration limit. Den Hollander et al., arXiv:1801.09909 (Section VI), establish a flat large-deviation-rate branch for the ordinary Brownian time-averaged absolute area but do not supply the marked Poisson-cycle result. Smith–Majumdar, arXiv:2202.03546, treat signed Gaussian area and condensation, a close saddle analogue rather than the same absolute cycle-maximum assertion. Smith–Majumdar–Schehr, arXiv:2301.11026, treat record ordering rather than extreme scales. Targeted mathematical-record searches and available previous claims were checked; the resulting priority judgment is not an independent exhaustive literature audit.

## Value — PASS

The theorem answers a motivated question left open by moment and power-law-extreme studies of the same observable: what controls the largest complete-cycle area during Poisson resetting? The exact extreme magnitude and selected-duration fraction distinguish long waiting from an atypically large Gaussian excursion and invalidate the simple longest-duration identification at the logarithmic extreme scale. The ordinary Brownian case gives the particularly transparent coefficients \(3/8\) for the leading squared-log area and \(3/4\) for the duration ratio.

## Limits and risks

The proof requires renewal of both position and diffusivity age, exact exponential waits, and a Gaussian scaled-Brownian path. Only first-order logarithmic extremes are claimed; centered Gumbel fluctuations and total-area large deviations are not. Closely related general Gaussian-excursion saddle results or an unlocated marked-renewal extreme theorem could imply a portion of the package. No independent mathematical audit or literature-wide certification was performed.

Self-review: passed. Independent audit: not yet performed.
