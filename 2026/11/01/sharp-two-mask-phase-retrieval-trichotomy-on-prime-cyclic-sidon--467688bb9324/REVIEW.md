# Scientific review

## Correctness
**PASS.** Two complete intensity arrays yield exact cyclic autocorrelations. Directed Sidon uniqueness isolates one complex pair product at each nonzero shift. The ratio of the two chirp-masked correlations gives an unambiguous \(p\)-th root of unity; inversion of \((r_1-r_0)d\) and of 2 recovers each pair of absolute endpoint indices. For support size at least three, the exact off-diagonal products give every diagonal via a three-index ratio, hence the rank-one vector modulo phase. For two sites, the quadratic magnitude equation has exactly two assignments; for one site all positions are indistinguishable. The translation argument proves one-mask insufficiency, and magnitude swapping proves persistence under arbitrary phase-only masks. The accompanying checker passed 4,983 finite exact-algebra tests. The full theorem is proved analytically, not inferred from this census.

## Originality
**PASS relative to checked literature and accessible mathematical research.** The motivating 2026 Novikov–Xu paper studies conventional Fourier phase ambiguities and Pauli/background problems, not quadratic chirp-coded intensity recovery. The 2013 Jaganathan–Oymak–Hassibi paper concerns generic/most sparse Fourier retrieval modulo translations/reflections; it neither asserts universal Sidon-class recovery nor determines absolute locations with two deterministic chirps. The 2015 Jaganathan–Eldar–Hassibi work uses nonunimodular zero-containing masks, with different measurements and hypotheses. The closest published finite-cyclic chirp-Gabor tomography and two-sparse STFT findings use full Gabor or STFT data, rather than exactly two Fourier intensity patterns. Searches for aliases and stronger coverage gave no decisive implication, but an unindexed equivalent coded-diffraction result is a residual risk.

## Value
**PASS.** The result determines the exact deterministic mask-complexity threshold on a natural distinct-difference sparse class, gives an explicit algebraic reconstruction, and identifies sharp information-theoretic exceptions for all phase-only masks. Recovering absolute support rather than support modulo time-shift is a meaningful distinction in coded diffraction. The theorem does not claim the same guarantee without Sidon geometry or establish noise stability.

Self-review: passed. Independent audit: not yet performed.
