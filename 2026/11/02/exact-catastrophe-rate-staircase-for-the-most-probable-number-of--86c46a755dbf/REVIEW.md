# Scientific review

## Correctness — PASS

The claim is for a finite irreducible Markov chain with exogenous independent colonization at empty sites, local extinction and a shared full-reset Poisson clock. Its stationary law follows exactly by regeneration: exponential elapsed time since the reset, independent Bernoulli patch states conditional on elapsed time, and a Beta(1, catastrophe-to-turnover ratio) latent age transform. The adjacent-mass ratios are expectations of a strictly increasing function under a parameter-indexed family with a strictly decreasing likelihood ratio; this establishes strict monotonicity and unique roots. The stationary balance identity enforces a single change of sign across adjacent mass differences, and orders neighboring roots strictly. Every quantifier and boundary, including integer equality \((N+1)\rho\in\mathbb Z\), is covered. The exact-rational checker tests illustrative finite cases; it is not substituted for proof.

## Originality — PASS within inspected evidence

The 2015 Kapodistria–Phung-Duc–Resing preprint has a different infinite-state linear birth/immigration–death generator, with an explicit equilibrium distribution and catastrophe-rate stochastic ordering. These broader methods do not imply a specific finite-patch mode staircase without the finite-site stationary ratio analysis. Artalejo–Economou–López-Herrero (2007) focus on immigration, catastrophe and extinction descriptors, not this theorem in their accessible abstract; its complete article body was not inspected. A full-text search and targeted inspection of the 2015 preprint's equilibrium and stochastic-ordering sections showed no identified statement implying the sharp occupancy-count mode classification. Published mathematical statements were compared for equivalent binomial-mixture modes and correlated patch extinction; none of the inspected statements covered the claim. Absence of a search hit is not proof of novelty. Residual risk: pre-2015 distribution-shape or metapopulation technical literature could have proved an equivalent result. The originality assessment is bounded by the sources actually inspected.

## Mathematical value — PASS

Simultaneous disturbances couple otherwise independent habitat patches, so their count distribution is an overdispersed age mixture rather than an ordinary binomial. A mode is a distinct ecological summary from the mean: it identifies the most likely number of occupied sites. The complete monotone staircase and the exact number of sharp regime boundaries solve this natural modal-classification problem uniformly over all finite patch counts and positive rates. The two-threshold four-patch example demonstrates nontrivial changes not visible from the ordinary marginal occupancy mean alone. This is a theoretical modal-regime result and not an empirical prediction.

## Closest literature and limitations

Artalejo et al., 2007 (DOI 10.3934/mbe.2007.4.573), deals with immigration and catastrophic population models; available abstract only. Kapodistria et al., March 16 2015 (EURANDOM 2015-006), accessible near-complete technical text inspected in the model, equilibrium and stochastic-ordering sections. Evans et al., 2005 (DOI 10.1111/j.1365-2656.2005.00948.x), motivates colonization/extinction mechanisms but is ecological empirical context, not the finite stationary reset theorem. Source coverage and search are not comprehensive; independent historical-priority verification remains to be done. External seed immigration, identical patches and total shared Poisson resets are essential assumptions.

Self-review: passed. Independent audit: not yet performed.
