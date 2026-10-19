# Scientific review: alphabet rigidity of the one-gap three-deck at length thirteen

## Correctness — PASS

The proof's arbitrary-alphabet step is the letterwise-map identity: for any target pattern, its number of gapped occurrences equals the sum of the source-pattern counts mapping to it. It follows that every putative collision with at least three jointly occurring letters would descend to a collision using all three letters of a ternary alphabet, contradicting the exhaustive ternary census. Distinct pairs of original alphabet letters therefore yield independent disjoint edges. Counting those edges gives the maximum-codebook and maximum-codebook-enumeration formulas. The binary census also rules out collisions at lengths three through twelve over arbitrary alphabets by mapping disagreement letters to the two binary values.

The finite critical premise is replayable: `gapped3_qary_cert.cpp` enumerates every binary word of lengths three through thirteen and every ternary word of length thirteen and compares complete exact multiplicity arrays, not probabilistic hashes. It checks the exact list of twelve ternary collision pairs and their binary projections; the standalone independent direct-index and dynamic-programming counter provides a separate calculation of individual signatures. Count arithmetic fits the explicitly bounded 16-bit histogram cells, and the complete ternary word universe fits the 32-bit enumeration index. All proof quantifiers and the exceptional two-letter degenerate length are explicit.

## Originality — PASS, with residual literature risk

The prior binary shortest-collision length and four binary collision pairs are not new and are stated as existing baseline information. The new scientific assertion is the arbitrary-\(q\) rigidity: no three-letter collision survives at length thirteen, hence the full reconstruction graph is a matching of exactly \(4\binom q2\) edges and has exactly \(2^{4\binom q2}\) optimal labeled codebooks. An arbitrary-alphabet alphabet-aggregation argument alone does not imply ternary rigidity from the binary classification; complete ternary analysis supplies an independent premise. The primary studies of Golm et al. (2022) and Rigo et al. (2023) establish the deck framework and investigate constructions/complexities, but the inspected material does not establish the stated exact arbitrary-alphabet class partition. Related two-multispectrum and deletion-channel classifications concern different observations.

There is residual risk of a previously published all-alphabet reconstruction equivalence hidden in unindexed or uninspected work. A failed search by itself is not novelty evidence; the positive comparison here distinguishes the new three-letter exclusion and codebook count from the scopes of the closest identified papers.

## Mathematical value — PASS

The complete characterization determines the exact largest zero-error reconstruction code, the exact number of maximizing codes, and every confusable pair for all alphabet sizes in the first nontrivial collision regime. It is useful for transferring a binary reconstruction threshold to larger-alphabet sequence models, where binary collision enumeration alone gives no prohibition against additional three-symbol collisions. Unlike a routine relabeling, the ternary rigidity is a substantive additional fact and is necessary for the all-alphabet classification. The theorem does not address larger source lengths or stronger/noisier observations.

## References and limitations

- R. Golm, M. Nahvi, R. Gabrys, O. Milenkovic, *The Gapped \(k\)-Deck Problem* (2022), arXiv:2201.12671, https://arxiv.org/abs/2201.12671.
- M. Rigo, M. Stipulanti, M. A. Whiteland, *Gapped Binomial Complexities in Sequences* (ISIT 2023), https://orbi.uliege.be/handle/2268/302524.

The finite ternary step is an exact computer-assisted lemma with independent spot-checking, not a symbolic closed-form proof. No claim is made of higher-length uniqueness or completeness of unindexed literature.

Self-review: passed. Independent audit: not yet performed.
