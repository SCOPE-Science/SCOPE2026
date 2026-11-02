# Scientific review: quadratic logarithmic localization

## Correctness — PASS
At stationarity, exponential holding ages are independent of entry positions and exactly exponentially distributed after multiplication by the rare-switch scale. The integral absolute logarithm bounds are proved uniformly over all entry positions. Total variation under random translation of an exponential has a Lipschitz bound, yielding quadratic errors. The mean constants follow from a separate dominated-convergence limit, \(\int_0^\infty -\log(1-e^{-bt})\,dt=\pi^2/(6b)\), and its doubled decay argument. The equal-sign entrance distribution and both distinct Poisson hazards are explicit. The reproducible checker passed finite numerical consistency tests, which were not used as proof.

## Originality — PASS, qualified best-knowledge
Sun, Ye and Chen (arXiv:2610.24961v1, sections IV and appendix C) already derive the conditional stationary position laws for independent run and tumble rates; Basu et al. (arXiv:1910.10083v1) already establish the equal-rate three-state stationary law and density singularities. Those achievements are not claimed. The narrower contribution is the fully quantified rare-switching logarithmic *conditional probability law* in total variation, with a globally uniform quadratic error and two distinct order-two conditional mean constants. Direct review of the primary texts found density formulas and edge exponents but not these exact quantitative statements or proofs. The earlier exact densities may nevertheless imply them after nontrivial analysis; independent publication-priority verification remains unperformed. The 2025 predecessor (arXiv:2409.00578v2) was also inspected in full; it contains exact total densities, a moment construction and peak exponents, but no stated conditional quadratic error or two order-two mean coefficients. Existing closed-form density expressions remain a residual implicit-coverage risk.

## Value — PASS
Power-law stationary density divergences by themselves do not specify the finite-rate quality of the exponentially scaled logarithmic peak laws. The order-two total-variation estimate provides a usable distributional guarantee for rare switching; the two different dilogarithmic mean corrections quantify non-leading peak structure and distinguish separately tunable duration hazards. The precise result matters when interpreting highly concentrated experimental/simulation histograms and cannot be replaced by a limiting atomic positional law or a leading edge exponent alone.

## Limitations
The model excludes thermal diffusion, non-harmonic forces, position-dependent hazards, and orientation persistence through tumbles. Neither the numerical checks nor the literature review prove absolute novelty; independent scientific and priority validation remain open.

Self-review: passed. Independent audit: not yet performed.
