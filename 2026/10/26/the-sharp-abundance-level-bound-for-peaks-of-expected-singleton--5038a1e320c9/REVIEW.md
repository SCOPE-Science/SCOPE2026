# Scientific review: expected singleton-richness peaks

## Correctness

PASS. The expected singleton count follows directly from multinomial sampling. A continuous exponential-polynomial interpolation has derivative with \(L\) distinct exponents and degree-one polynomial coefficients; the generalized Rolle argument bounds its real zeros by \(2L-1\), and therefore bounds the number of strict sample-size peaks by \(L\). The separated-abundance family creates \(L\) alternating prominence regions. The generic transcendental choice eliminates ties, proving sharpness. The rational three-species witness has all six strict adjacent inequalities checked by the included verifier.

## Originality

PASS, subject to the residual literature risks below. Magurran (2005) treats species-abundance histograms rather than modal sample sizes of the expected observed-once count. Chao and Jost (2012) treat accumulating richness and coverage, not local maxima of singleton frequency as a function of effort. O'Hara (2005) treats bias of richness estimators. The closest database occupancy results treat richness-frequency covariance or modal multinomial masses, neither of which implies the bound or construction. The root-count bound itself is classical and not claimed as new. A more specialized treatment of exponential mixtures or occupancy counts might entail the theorem and remains a bibliographic risk.

## Mathematical value

PASS. Singleton counts are used in biodiversity completeness analyses, yet their expectation as sampling effort grows need not be unimodal even for only three species. The sharp bound relates global sampling-effort complexity directly to the number of abundance levels; examples achieve every possible complexity class. The theorem delineates precisely what abundance heterogeneity can permit, rather than providing a routine evaluation at a fixed sample size.

## Closest literature and limitations

Full-text material reviewed from Magurran (2005), O'Hara (2005), and Chao and Jost (2012). Mao and Colwell (2005) had abstract-level material only, leaving a targeted unresolved bibliographic risk. No inference from an inaccessible source was treated as a proof of noncoverage. Conclusions require iid sampling with replacement from a finite fixed positive probability vector. The proof is mathematical and does not show multimodality to be common in field surveys. Independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
