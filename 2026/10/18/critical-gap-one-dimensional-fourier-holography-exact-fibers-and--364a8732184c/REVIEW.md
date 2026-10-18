# Self-review

## Correctness — PASS

The finding concerns the known reference \(b\ne0\) at index \(2n\), integer \(n\ge1\), and completely arbitrary unknown complex coefficients on indices \(0,\ldots,n\). Exact Fourier autocorrelation identities recover all lower-index coefficients from outer lags and reduce the final coordinate to one explicit real-linear map. The minimum singular value vanishes precisely when all interior coefficients vanish and the two endpoint amplitudes balance. The remaining norm datum then proves the stated exact twofold conjugate-reflection fiber. A nonaliasing discrete Fourier grid gives the finite sampling assertion. All boundary and normalization cases, including \(n=1\), vanishing coefficients, and coincident reflection partners, are covered.

## Originality — PASS, with stated historical-priority risk

The motivating Novikov–Xu paper (arXiv:2604.25662v1) constructs subcritical background ambiguities and recalls the supercritical uniqueness regime, but does not derive the present discrete critical known-spike fiber. The two-dimensional reference-block deconvolution of Barmherzig et al. (arXiv:1901.06453) cannot be applied unchanged to the colliding one-dimensional edge lag. Crimmins–Fienup (JOSA 73 (1983)) assumes strict separation, and Bendory–Beinert–Eldar (arXiv:1705.09590) provides general and generic phase-retrieval theory, not this complete critical family. Searches of published mathematical findings and accessible published mathematical claim summaries did not identify equivalent/stronger coverage. Such searches cannot exclude an unindexed old result. The structured audit gives implication checks and precise inspection scopes.

## Value — PASS

The result isolates the boundary between isolated reference cross-correlations and the first unavoidable autocorrelation collision. It gives an entire exact fiber classification for every length, not a favorable example, and specifies a sharp conditional inverse stability margin that collapses at exactly the same algebraic degeneracy. These facts are natural design criteria for one-dimensional reference-aided Fourier phase retrieval. The claim is deliberately confined to one known point-reference; it is not a general holography uniqueness theorem.

## Verification and limitations

The ordinary checker is `verification/check.py`, using only the Python standard library. It passed 2,185 parameter cases, including independent exact-lag, discrete Fourier, real-Gram-spectrum, and balanced-fiber checks. These tests supplement an analytic proof; no finite simulation establishes its all-parameter quantifiers. The singular spectrum is conditional on already knowing the earlier coefficients. The critical exception is a classical conjugate-reversal ambiguity, not an unknown new symmetry. No independent evaluation is asserted.

Self-review: passed. Independent audit: not yet performed.
