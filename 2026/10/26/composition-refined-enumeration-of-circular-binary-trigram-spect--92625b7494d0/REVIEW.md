# Scientific review: circular binary trigram spectra

## Correctness

**PASS.** Every circular trigram spectrum corresponds exactly to a connected balanced edge-multiset on the order-two binary de Bruijn graph. The proof derives the forced coordinate equalities, parametrizes the remaining counts, checks precisely when isolated loops are forbidden, and uses Euler's theorem for both necessity and sufficiency. Its zero/one composition equations give a one-to-one correspondence with the product count \(F_t(p)F_t(q)\). Finite geometric summations give the rational series, and the pole of order five at one yields the stated asymptotic. Direct labeled-word enumeration, independent parameter enumeration, and integer rational-coefficient verification agree in the packaged checker. There are no unproved infinity claims based solely on finite data.

## Originality

**PASS within the inspected record.** The closest literature on spectrum-preserving Eulerian de Bruijn representations concerns algorithms for recovering or compressing representations of specified read multisets, and the most directly related recent substring-vector coding paper concerns edit-correcting hashes rather than a fixed-composition classification of all feasible cyclic three-mer vectors. A separate available result counts length-only **linear** trigram spectra; its path-boundary geometry differs from the present circular Eulerian geometry, and its numerical formula does not entail this bivariate enumeration. Searches for circular trigram histograms, necklace three-factor frequency profiles, exact count-vector generating functions, and equivalent de Bruijn circulation parametrizations found no dominating result. Absence from an index is not proof of priority; an unindexed formula or general multivariate flow-enumerator specialization remains a residual risk. A recent genome-assembly article was examined in its accessible indexed sections, not every page of its publisher copy.

## Mathematical value

**PASS.** Complete cyclic substring-multiset observations form a natural finite reconstruction channel for circular sequences. The exact admissible eight-vector classification, composition-refined count, and rational length series determine the largest noiseless codebooks from that channel at every length and composition. The connectivity restrictions on the de Bruijn flow are not captured by linear-word counting or by merely counting necklaces. This is an all-parameter structural enumeration, not a tiny benchmark improvement or a renaming of a previous invariant.

## Closest literature and limits

The closest inspected scientific sources are Chen et al. (arXiv:2510.22404; lossless multiset Eulerian cover algorithms), Zhu et al. (doi:10.3390/math14050832; graph-based reconstruction and probabilistic collision models), En Gad (arXiv:2609.19493; substring-count hashing for deletion codes), and Bernardini et al. (doi:10.4230/LIPIcs.CPM.2022.12; Eulerian extensions of de Bruijn graphs). The result does not resolve circular reconstruction ambiguity, noisy observations, larger alphabets, or higher-order reads. Publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
