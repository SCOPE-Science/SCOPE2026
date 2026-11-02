# Scientific review: three-survey directed-dispersal identifiability

## Correctness — PASS

The normalized patch-preference colonization mechanism is explicitly stated, including the occupancy constraint, positivity requirements, and the nonzero disturbance rates. The fraction \((h-p)/[\phi(1-h)+\gamma p+h-p]\) decreases strictly, proving existence/uniqueness/attractiveness of the positive equilibrium under the stated viability inequality. Its exact balance is linear in the three transformed positive parameters. Row reduction proves both the complete noncollinearity criterion and the L-design determinant. The positive inverse and an open family of counterparameters when rank fails complete the global-identifiability and impossibility claims. An exact-rational example and the standalone standard-library checker reproduce the calculations over 2,500 grids. Finite checks corroborate, rather than replace, the proof.

## Originality — PASS within inspected evidence; historical-priority risk remains

The 2005 Purves–Dushoff full main text supplies the original model, its equilibrium response, and the confounding of single-baseline fits. These are explicitly credited. In its accessible model, response and fitting sections, it does not present the exact joint three-parameter recovery criterion, the all-parameter L-design determinant, or the sharp obstruction for single-axis surveys. The 2012 Lele–Moreno–Bayne full text studies detection-process identifiability, not this equilibrium-mechanism inversion. Royle 2006 treats heterogeneous detection. Harding–McNamara 2002 supplies a general biological framework, but the accessible abstract does not establish the specific claim. Published research-record comparisons included different Klausmeier, seed-bank, detection-mixture, and ecological occupancy models; their claims do not imply an inverse for these three normalized directed-dispersal parameters. The 2005 supplemental appendix and Harding–McNamara technical full text were not materially available; they are residual priority risks, not asserted non-covering full texts.

## Value — PASS

The problem is mathematically and ecologically natural because the original model has **two independent dispersal preferences** plus an unknown colonization scale, yet different parameter combinations can reproduce an observed habitat response. The theorem specifies exactly when complete mechanistic inference is possible from ideal equilibrium data, proves that an arbitrarily dense one-control survey is inadequate, and gives a guaranteed feasible minimal mixed habitat/disturbance design with a closed inverse. It distinguishes a lack of mechanistic information from simply having too few samples, and the determinant gives a direct diagnostic of fragility under nearly repeated conditions. This is a complete structural-identification boundary for a concrete ecological model, not a general claim of reliable empirical estimation.

## Closest sources and limitations

- Purves and Dushoff, *Journal of Ecology* (2005), DOI 10.1111/j.1365-2745.2005.00988.x: full accessible main text inspected, especially directed-dispersal model and survey-fitting sections; source equations credited.
- Harding and McNamara, *American Naturalist* (2002), DOI 10.1086/341014: abstract only; possible broader-coverage risk.
- Lele, Moreno and Bayne, *Journal of Plant Ecology* (2012), DOI 10.1093/jpe/rtr042: accessible full article inspected on detection and covariates, distinct observation model.
- Royle, *Biometrics* (2006), DOI 10.1111/j.1541-0420.2005.00439.x: accessible abstract on heterogeneous detection, not mechanistic preference identification.

Strictly positive equilibrium, exact occupancy, known disturbance rates, common biological parameters, and the specified globally mixed model are necessary. No independence or external certification is asserted.

Self-review: passed. Independent audit: not yet performed.
