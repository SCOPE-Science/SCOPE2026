# Self-review

## Correctness

**PASS.** The internal coalition-worth term is a sum of two-player unanimity games, one for each directed arc. Shapley linearity gives half of each arc's weight to each endpoint. The unit-weight directed 3-cycle has exact coalition worths \(0,1,2,3\) by coalition size and exact Shapley value \(1\) for every player; the displayed reciprocal-only term yields \(0\). The proof and exact-rational script agree.

## Originality

**PASS, with scope limits.** The result is a source-specific correction, not a claim that the general Shapley identity is new. The 2024 predecessor defines internal trust using all directed arcs, and the 2026 preprint's own unanimity decomposition includes all arcs; its displayed Corollary 3.3 first term omits one-way arcs. published-finding corpus semantic queries and the accessible ledger yielded no directly matching correction. Search absence is not a proof of global novelty.

## Value

**PASS.** The missing term changes Shapley trust scores on any network with positive one-way arcs incident to a player. The exact three-cycle witness changes each computed score from \(1\) to \(0\) under the displayed expression, so the issue is consequential for the source's stated trust-ranking application rather than a cosmetic notation choice.

## Closest literature and limitations

- Ryzák and Kroupa, arXiv:2605.18157v1: Definition 2.1, Lemma 3.2, Corollary 3.3.
- Bandhana, Kroupa, and García, AAMAS 2024, DOI 10.5555/3635637.3662860: Section 3, Definition 3.1.
- MSC2020 91A12: Cooperative games.

The claim is limited to the internal Shapley contribution and its effect on the stated witness. The inspected preprint is v1; a later correction may exist. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
