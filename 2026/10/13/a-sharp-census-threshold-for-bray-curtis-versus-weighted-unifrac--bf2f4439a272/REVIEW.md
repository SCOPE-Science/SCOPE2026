# Self-review

## Correctness — PASS

A direct reduction of the standard normalized weighted UniFrac branch sum on the stipulated ultrametric tree gives \(U_t=(k-tc)/N\), with integers \(0\le c\le k\le N-3\). The gap of at least one between distinct Bray–Curtis ranks is stronger than the maximal phylogenetic discount whenever \(t(N-3)\le1\). Conversely the exhibited three-community construction attains the maximal discount and reverses rankings when the inequality is strict. The witness, the equality boundary, normalization, and positive-count hypotheses were checked explicitly. The standalone exact-rational computation returned `VERIFY_OK` for 10,584 direct-versus-reduced pair distances and 218,484 three-community checks. Infinite correctness rests on proof, not this finite test.

## Originality — PASS

The closest sources are Bray and Curtis (1957) for abundance overlap, Lozupone et al. (2007) for normalized weighted UniFrac, Evans and Matsen (2010/2012) for its general tree transport formula, Schmidt et al. (2016/2017) for comparison with Bray–Curtis while introducing interaction-adjusted similarity indices, Roldán Ahumada and Avendaño Garrido (2019) for small-sample UniFrac metric behavior, and Pendleton and Schmidt (2026) for four-taxon numerical comparisons. Their relevant full-text sections establish definitions, transport equivalence, alternative indices, or finite simulations, but not the necessary-and-sufficient **integer three-tip common-reference rank-reversal boundary**. The general transport identity is prior work and is not claimed as new. No exact published cutoff or dominating all-census theorem was found in scientific literature and indexed mathematical-result searches. Residual risk: a broader unindexed theorem on integral transport versus total-variation rankings could imply the present special case.

## Value — PASS

The theorem exactly identifies when two widely used ecological beta-diversity indices can disagree on the **relative ordering** of community dissimilarities on the smallest nontrivial rooted phylogeny. A universal no-reversal zone, sharp census staircase, equality behavior, and smallest concrete shared-reference example characterize a natural finite-read design limitation. This is more informative than a numerical demonstration that phylogenetic weighting changes metric magnitudes. It is not a claim of general ecological effect size or statistically reliable ranking in real data.

## Limits

Fixed three taxa with all taxa in all communities, equal finite integer censuses, a rooted ultrametric binary tree, and normalized relative-weighted UniFrac. The parameterized formula does not establish analogous thresholds for arbitrary phylogenies or missing taxa. Independent human assessment and independent audit remain unperformed.

Self-review: passed. Independent audit: not yet performed.
