# Scientific review

## Correctness — PASS

The identity follows by conditioning separately on a planted copy of the motif, retaining independence of all unforced edges, and dividing its conditional degree probabilities by the ordinary binomial degree probability. The unique probability roots follow from strict decreasing inverse powers, the degree-index law from rising falling factorials, and the sparse/dense thresholds from controlled finite-degree expansions. No inference relies on simulation. Reproducibility: `python3 verify.py` returns `PASS: 159 exact finite graph-case/threshold groups` and `PASS: 16 additional asymptotic/root checks`; the verifier is finite corroboration rather than a proof.

## Originality — PASS (provisional historical priority)

The closest inspected primary sources are Lin–Reinert's joint degree-count analysis (arXiv:0912.4812) and Sah–Sawhney's local limit theory for motif counts (arXiv:2006.11369). Neither inspected treatment states or implies the exact finite mixed covariance with every fixed degree, its two-way single-crossing sign theorem, and the sparse/dense threshold corrections. A published component–triangle covariance concerns total connected components rather than exact-degree counts and does not imply this claim. Janson's 1994 orthogonal decompositions are plausibly strong enough to imply mixed-moment representations and remain the greatest historical-priority uncertainty because its full text was not accessible. No absence-of-search-results assertion is treated as uniqueness proof.

## Mathematical value — PASS

The result gives a complete sign-phase classification across the whole degree range for an arbitrary noninduced motif, separating the sparse regime from the dense regime and revealing that the covariance sign depends only on the motif's degree sequence, not on its internal shape or placement weights. This dependence is not determined by separate degree/motif marginals, and the exact two-direction phase diagram yields useful qualitative information beyond a single covariance computation.

## Limitations

Only independent-edge, noninduced motifs without isolates, nonnegative deterministic weights and interior probability parameters are covered. No independence follows from a zero covariance; no signed-weight version is asserted. Full inspection of Janson's monograph and other possible broader treatments remains outstanding.

Self-review: passed. Independent audit: not yet performed.
