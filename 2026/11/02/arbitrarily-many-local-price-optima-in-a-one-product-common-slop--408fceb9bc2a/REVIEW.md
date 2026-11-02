# Scientific assessment

## Correctness — PASS

The derivation differentiates each binary-logit component exactly. The uniform bound \(|f_\theta'(p)|\le1+p/4\) preserves existing finite strict derivative witnesses after a sufficiently small positive new weight. At a later price the old mixture derivative is negative but arbitrarily close to zero, while the new component derivative approaches one as its valuation increases. At a price one unit beyond that valuation both the old derivative and the new derivative are negative. This yields a new independent positive-to-negative sign pair. Analyticity makes the resulting interior maxima and intervening minima strict. Normalizing weights and taking small perturbations preserve all signs. A reproducible rational interval checker certifies four illustrative finite parameter sets (50 assertions); it is not substituted for the all-integer proof.

## Originality — PASS within inspected evidence, provisional

The model, two-segment multimodality, and failure of quasiconcavity are acknowledged prior art. In particular, the 2018 Li–Webster–Mason–Kempf paper already illustrates a single-product common-slope two-segment counterexample, while van de Geer and den Boer (2022) give another two-segment example and an optimization algorithm. The assessed contribution is instead the theorem that every number of segments can force at least as many strict local price optima, accompanied by an explicit inductive construction and an open-parameter-set guarantee. The 2013 mixed-logit competition paper studies equilibrium conditions rather than this unbounded lower bound. The most serious residual risk is an existing unlocated general result for mixtures of sigmoids or price-revenue curves that already implies the lower bound.

## Value — PASS

The number of separate revenue maxima is mathematically unbounded even in a one-dimensional single-product optimization problem with a common demand slope. Thus adding latent consumer segments, rather than extra products or heterogeneous price coefficients, suffices to create progressively complex objective landscapes. This distinction is relevant for interpreting failures of unimodal pricing heuristics and motivates global methods. The claim does not assert a computational-hardness bound or empirical prevalence.

## Closest literature and limitations

Aksoy-Pierson, Allon, and Federgruen (2013), https://doi.org/10.1287/mnsc.1120.1664 ; Li, Webster, Mason, and Kempf (2018), https://doi.org/10.1287/msom.2017.0675 ; van de Geer and den Boer (2022), https://doi.org/10.1287/mnsc.2021.4272 . The construction permits highly separated valuations and very unequal market weights, and makes no assertion about the number of global maximizers or realistic finite-data detectability. Historical priority remains open to independent review.

Self-review: passed. Independent audit: not yet performed.
