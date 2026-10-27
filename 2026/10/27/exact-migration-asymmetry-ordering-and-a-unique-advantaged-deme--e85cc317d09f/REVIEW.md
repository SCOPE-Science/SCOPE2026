# Research assessment: two-deme Poisson branching under asymmetric migration

## Correctness — PASS

The central assertion concerns the nonzero survival fixed point of a two-type Poisson Galton–Watson process, not an arbitrary finite-population fixation probability. Existence follows from the Perron vector and supercritical concavity, while uniqueness uses strict subhomogeneity. The inequality \(-t\log t<1-t\), for \(0<t<1\), verifies that the fixed-point Jacobian has spectral radius below one, supporting the implicit differentiations. Direct inversion gives the exact sign of the mean-survival derivative; the unequal-type sign is established by continuation from symmetric migration and absence of crossings. In the rank-one complete-redistribution case, monotone decrease of the disadvantaged-type survival identifies exactly one sign change of the advantaged-type derivative. The scalar characterization has a unique root in its stated interval. Local curvature and numeric illustrations are supplementary and were checked independently of the analytical sign proof.

Residual correctness risk: No claim is made that the Poisson branching process exactly reproduces fixation in finite populations or outside its biological approximation regime. In particular, any biological extrapolation to rare migration or density-dependent bottlenecks is unproved.

## Originality — PASS (self-review)

Abbara–Bitbol (arXiv:2306.10879, 2023), Supplement Eqs. S25 and S59–S61, already provide the relevant branching fixed point and first-order weak-selection star formulas, including the two-deme case. Their main monotonic-suppression narrative is explicitly acknowledged. The assessed advancement is the **exact all-supercritical-parameter strict ordering along a fixed-total-migration path, its curvature at balance, and a unique interior optimum for the favored initial type at full redistribution**. These are not entailed by that first-order expansion or by the published circulation/noncirculation dichotomy. Czuppon et al. (DOI:10.1086/714034, 2021) examine a qualitatively related, but mathematically different, habitat-dependent mutant-establishment system. Targeted literature searches and published mathematical-result comparisons found no directly implying theorem. Publication priority remains nonexhaustive.

## Value — PASS

The source literature identifies directional migration imbalance as an important mechanism affecting beneficial-mutant establishment. The theorem resolves an exact control question: at **fixed overall exchange**, does every increase in bias reduce mean establishment, even when selection is not infinitesimal? It answers yes under a precise two-deme branching model. A second, biologically interpretable separation is that maximizing the establishment chance from a strategically favored introduction deme is not the same as maximizing that chance for a random introduction. The complete-redistribution case has a universal, exact, unique optimum for the favored introduction type for every \(\lambda>1\). The exact quadratic coefficient measures sensitivity close to balanced migration. This is a structural theorem rather than a parameter-specific recomputation of the weak-selection source formula.

## Sources and limitations

- A. Abbara and A.-F. Bitbol, *Frequent asymmetric migrations suppress natural selection in spatially structured populations*, arXiv:2306.10879, first public June 19, 2023: https://arxiv.org/abs/2306.10879.
- P. Czuppon, F. Blanquart, H. Uecker, and F. Débarre, *The Effect of Habitat Choice on Evolutionary Rescue in Subdivided Populations*, *The American Naturalist* (2021), DOI:10.1086/714034: https://www.journals.uchicago.edu/doi/full/10.1086/714034.

The analysis is two-type, Poisson, supercritical, and column-stochastic. The mean concerns uniform choice of initial type. The local maximizer result is specific to complete redistribution. No finite-population equivalence, all-graph theorem, or independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
