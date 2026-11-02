# Scientific review: finite-horizon convex-risk minimum for two habitats

## Correctness — PASS

The model's column sums are \(c_q=1-q+sq\), which gives a mean-one normalized total abundance with a conditionally unbiased annual multiplier. Spatial exchangeability supplies a conditional symmetrization inequality for every convex test. Convexity of the one-period averaging operator closes the induction over all finite horizons. The strict argument requires \(q\ne1/(1+s)\), positive habitat masses, nonidentical growth shocks with positive probability, and finite relevant convex expectations; these are stated. The two-year variance identity follows by direct conditional second moments and the exact first-year habitat contrast. The independently implemented path enumerator passes 6022 rational checks; enumeration does not certify arbitrary horizons or distributions.

## Originality — PASS within inspected evidence

Morita--Yoshimura (2012, arXiv:1207.4618) explicitly contains the dispersal matrix and its well-mixed condition; both are acknowledged and not claimed as new. Its main established conclusions concern stationary patch ratios and asymptotic logarithmic growth. Morita--Yoshimura (2013, arXiv:1307.7903) studies many-patch power-law behavior and approximate growth variances. Jansen--Yoshimura (1998) treats allocation maximizing long-run geometric growth. The inspected texts do not give the present *all finite horizons, all convex functionals* ordering of strategy-normalized total abundance, its strict unique optimum, or the exact two-year variance gap. A separate previously documented antiphase patch-ratio result concerns stationary Cantor support and a dispersal duality; those conclusions neither imply nor are implied by the present finite-horizon convex order of total abundance. The static convex symmetrization inequality is standard and is credited as proof machinery. Full technical coverage of Schreiber (2010), Keeling (2000) and any undiscovered dynamic diversification theorem remains a priority risk; an unsuccessful search is not a uniqueness certificate.

## Value — PASS

The primary paper identifies risk spreading as ecologically important while concentrating on long-run typical growth and patch-ratio distributions. The new law gives a complete, distribution-free finite-horizon answer for relative abundance risk, robust to arbitrary within-year spatial correlation and every convex loss including upper-tail and shortfall hinge losses. It pinpoints the migrant-survival-adjusted optimum \(q_*=1/(1+s)\), identifies the earliest horizon at which unequal dispersal is detectable, and quantifies the exact two-year penalty from spatially unequal shocks. Crucially, it distinguishes this relative-risk objective from absolute abundance, migrant mortality and biological persistence. This is a natural structural result for stochastic ecology, not an arbitrary numerical slice.

## Closest literature and limitations

The principal comparator is Morita and Yoshimura (2012), whose equation for the dispersal matrix is the precise forward model. The independent-year assumption is necessary to use the convexity operator recursively; habitat exchangeability is necessary for the pointwise symmetrization. Models with temporal dependence, nonexchangeable patch environments, nonlinear competition, stochastic individual extinction, or a fixed absolute-wealth target are not addressed. The strict-variance law assumes second moments. Literature comparisons are limited to accessible texts and the inspected search results; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
