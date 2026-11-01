# Scientific review: sharp rare-event and moment laws for antithetic nested Monte Carlo at a kink

## Correctness — PASS

For two independent inner-block sample means with a shared outer variable, convexity makes the coarse-average-minus-fine correction nonnegative. Its conditional dependence on the outer variable is exactly the compactly supported triangular hat \(\left(d/4-|y+c|/2\right)_+\). Integrating its powers produces the exact conditional width formula, and the classical central limit theorem with uniform integrability controls every stated limiting constant. A bounded density continuous at zero permits a localized replacement by its value at the kink. The correction occurrence probability determines the independent-pilot zero-count limit. Moment orders one through four prove the sharp ordinary centered kurtosis. In the normal specialization, independence of the Gaussian sum and difference gives the exact two-half-normal law, and polar integration gives the finite-sample formulas. A standard-library reproducer passed 593 deterministic checks of algebraic identities, finite Gaussian moments, limiting coefficients and pilot probabilities. These finite checks do not establish the asymptotic claims on their own; the analytic arguments do.

The hypotheses are essential to the reviewed claim: independent identically distributed centered inner errors with positive variance; a bounded, positive, continuous outer density at zero; specified moments for the \(r\)-th moment law; independent outer replications for the pilot statement; and normality for the exact finite formulas. Every limit is over even inner sizes. Reversing the multilevel sign convention changes the signed correction, not its magnitude or rarity.

## Originality — PASS, with publication-priority limitations

Haji-Ali and Spence, *Nested Multilevel Monte Carlo with Biased and Antithetic Sampling* (arXiv:2308.07835v1; 2023), Section 2 and Appendix A, give general antithetic-correction moment **bounds**, while their numerical discussion describes the growth of high-level kurtosis and the difficulty of estimating a variance with few samples. The present claim does not reassert those rates or the phenomenon as new. It supplies exact asymptotic constants at an outer kink, a positive-event detection threshold, and the entire finite Gaussian law, none of which follows as a numerical equality from an upper bound alone. Giles and Goda, *Decision-making under uncertainty* (arXiv:1708.05531v1; 2017), likewise supply the antithetic nested-MLMC construction and complexity results, not this complete law. Giles and Haji-Ali (arXiv:1802.05016v1; 2018) address a Heaviside payoff and adaptive inner sampling, rather than this continuous positive-part Jensen-gap law. Spence's 2023 dissertation develops related higher-level kurtosis estimates; it does not settle these constants in the inspected sections.

General Gaussian ratio, positive-part and bivariate-normal integration formulas are established background mathematics; the new scoped claim concerns their specific antithetic correction identification and exact application together with the full non-Gaussian asymptotic moment and pilot laws. Full-text comparison with Bourgey, De Marco, Gobet and Zhou (2020), *Multilevel Monte-Carlo methods and lower-upper bounds in Initial Margin computations*, remains incomplete because an accessible full-text copy was not obtained. That source addresses a particularly relevant nested maximum, so this is an explicit publication-priority risk rather than a declaration that the article does not cover the claim. Search absence never proves novelty; independent literature review remains warranted.

## Value — PASS

High-level antithetic corrections concentrate strongly at zero despite useful small variance. Pilot procedures that calibrate multilevel allocation from a handful of fine-level samples can therefore return a misleading zero sample variance; the sharp positive-event constant shows precisely when that failure is overwhelmingly likely and how many outer replications are needed merely to observe a correction. The exact Gaussian formulas offer a finite-sample benchmark for variance and pilot calibrations, and the full non-Gaussian moment constants quantify the limiting rare-event/kurtosis mechanism. This is a motivated computational-statistics diagnostic, not an arbitrary normalization or an improvement claim about unrelated algorithms.

## Closest sources and limitations

- A.-L. Haji-Ali and J. Spence, arXiv:2308.07835v1, https://arxiv.org/abs/2308.07835 — same antithetic nested maximum, general bounds and kurtosis issue; not an equality for these coefficients in the inspected sections.
- M. B. Giles and T. Goda, arXiv:1708.05531v1, https://arxiv.org/abs/1708.05531 — earlier antithetic nested decision-making construction.
- M. B. Giles and A.-L. Haji-Ali, arXiv:1802.05016v1, https://arxiv.org/abs/1802.05016 — different Heaviside/adaptive-sampling problem.
- F. Bourgey, S. De Marco, E. Gobet and Y. Zhou, https://doi.org/10.1515/mcma-2020-2062 — relevant initial-margin work, full comparison outstanding.

No optimal allocation theorem, dependent-noise extension, discontinuous-payoff extension, nonnormal finite closed law, or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
