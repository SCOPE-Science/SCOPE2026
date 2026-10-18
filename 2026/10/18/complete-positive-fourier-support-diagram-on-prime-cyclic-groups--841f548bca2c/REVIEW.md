# Scientific review: complete positive Fourier-support diagram on prime cyclic groups

## Correctness — PASS

The proof reduces necessity to the exact prime-cyclic Chebotarev--Tao inequality, strict positivity of the zero-frequency coefficient for every nonzero nonnegative function, and conjugate pairing of all nonzero frequencies. Sufficiency explicitly produces one grid-nonnegative trigonometric polynomial vanishing at exactly \(p-k\) consecutive residues, with Fourier degree \(\lceil(p-k)/2\rceil\). The lower bound and parity force every Fourier mode in that allowed band to be nonzero. Multiplying by powers of a strictly positive one-cosine perturbation then introduces each remaining pair of adjacent outer frequencies; its leading coefficients are nonzero powers of the perturbation parameter. No infinite assertion is based on finite computation. A self-contained checker corroborates 114 exact-support pairs for the sample primes 3, 5, 7, 11, and 13.

## Originality — PASS, subject to documented bibliographic limits

Tao's *An uncertainty principle for cyclic groups of prime order* (arXiv:math/0308286, Theorem 1.1, including its converse) treats arbitrary complex-valued vectors. Its statement does not enforce pointwise positivity, and the existence proof uses arbitrary complex Fourier linear combinations; hence it does not logically imply this positive-cone realizability classification. The 2023 DFT uncertainty-diagram paper likewise studies arbitrary vectors and defines KD classicality through a different quasiprobability distribution. Two closely relevant published specialized findings were materially inspected: *Sharp quarter-zero law and extremizer dichotomy for positive three-atom Fourier transforms on dyadic cycles* treats a three-atom cone on even prime-power groups, whereas *Phase-only four-sparse uncertainty over prime cyclic groups* treats an equal-magnitude complex four-point constraint and fixed support geometry. Neither proves all nonnegative support pairs over odd prime groups. Database searches tested full-pair diagrams, nonnegative prime-cyclic sharpness, positive trigonometric factors, and characteristic-function formulations. Residual risk: an unindexed older positive Fourier or probability-cone support theorem could contain the classification.

## Value — PASS

This is the full realizability diagram, not a single low-dimensional table or a preselected special support size: every odd prime and every exact time-support and Fourier-support cardinality are settled. The positive cone represents probability weights, and requiring all time coefficients to be nonnegative destroys the complex linear-combination argument behind unrestricted support-pair realization. The theorem identifies the only remaining obstruction (odd Fourier support due to DC and conjugacy) and supplies an explicit construction for every admissible pair. It does not claim a result for prescribed positional support sets, composite orders, or quantitative conditioning.

## Limitations and closest work

Theorem 1.1 of Tao (2003) supplies the additive uncertainty inequality and the unrestricted complex support-set converse, so neither is claimed new. The 2023 uncertainty-diagram source was available through excerpts but its publisher full page returned an HTTP 429 when opened; no whole-paper negative coverage claim is made from those excerpts. The two closer special-condition published results were read in full as scientific result documents; their group and coefficient constraints differ materially. This review is not an independent audit and does not establish absolute historical priority.

Self-review: passed. Independent audit: not yet performed.
