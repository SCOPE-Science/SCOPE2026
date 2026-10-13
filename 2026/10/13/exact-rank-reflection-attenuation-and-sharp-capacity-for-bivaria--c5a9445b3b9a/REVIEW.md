# Scientific review: Exact rank-reflection attenuation and sharp capacity

## Correctness — PASS
The population coefficient is normalized as six times the integrated variance of conditional response CDFs for a uniform response. The reflected conditional-CDF fluctuation is the negative reflected original fluctuation. Splitting it into orthogonal even and odd components gives the biased-channel attenuation formula. Folding the response rescales the even component by exactly four in squared norm. All coefficients, boundary cases and equality statements then follow from total variance and the standard zero/one characterizations of Chatterjee's coefficient. The explicit mixture of comonotonicity and independence realizes every capacity value. The packaged exact-rational checker independently passed 2,752 tests covering nonsymmetric checkerboards, reflection-symmetric cases and rational interpolation parameters; those tests do not replace the general proof.

## Originality — PASS, with priority risk
Rockel's 2026 paper proves a comparison with Kendall's tau under stochastic increasingness, not an exact formula for independent reflection of an arbitrary copula. Ansari–Rockel's 2025 exact rank-correlation region does not identify the reflection-channel contraction. The 2024 table already supplies the Fréchet mixture coefficient and thus a sharp endpoint witness; the endpoint by itself is not new. Standard data processing suggests upper bounds but does not by itself furnish the exact identity, its reflection-even/odd decomposition and the fair-coin equality transition. Literature and mathematical-record searches did not reveal a covering statement. Possible unindexed equivalences and generic Markov-operator treatments remain residual risks.

## Value — PASS
Reflection is a natural, model-independent form of latent sign ambiguity. The exact attenuation law quantifies the information retained by Chatterjee's directed rank coefficient at every flip probability, not just at one example. It provides the full capacity interval, proves the different equality conditions at unbiased versus biased reflection, and explains why two usual concordance coefficients can both vanish while directional predictability persists. The identity is useful for rank-based dependence calibration under randomized orientation loss and complements the 2026 positive-dependence comparison.

## Limitations and scientific priority
The theorem concerns population copula ranks and an independent orientation coin. It does not treat observation-dependent flipping or sampling uncertainty. Prior results compute the Fréchet endpoint, and these values are not presented as original. No independent scientific validation has been undertaken.

Self-review: passed. Independent audit: not yet performed.
