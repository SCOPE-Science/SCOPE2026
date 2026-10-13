# Scientific review

## Correctness — PASS

The exact stabilizer-support linear constraints show that two consecutive losses separate surviving clusters. If no four consecutive vertices survive and no cluster contains five retained vertices linked by gaps at most two, every surviving cluster has stabilizer rank at most one, hence a fully separable marginal. Conversely the four consecutive retained sites yield the explicit negative eigenvalue \(-1/8\) after a one-qubit partial transpose. The 16-pattern union bound is exact as an inequality and the Poisson factorial-moment argument correctly treats overlapping four-runs; it does not confuse enumeration with an infinite proof. A standard-library verifier exhaustively checked the required rank decompositions for all 64,512 masks on cycles of order 10 to 15. Risk: extension to non-cycle graph states or correlated losses is not justified.

## Originality — PASS

The closest motivating preprint, Han–Zhang–Zhang arXiv:2606.08561v1, already proves the four-site NPT witness and the lack of worst-case \(m\)-resistance of larger cycles; these are *not* claimed as new. Its full accessible manuscript, including main cycle theorem and discussion, treats adversarial fixed-number loss rather than the probability of non-full-separability under independent Bernoulli losses. The new structural upper bound via five-site gap patterns and its Poisson survival profile address a different mathematical implication that is not contained in the explicit results inspected. Relevant graph-state particle-loss Bell-inequality and noisy-graph coherent-information studies address different observables and noise ensembles. There remains a priority risk of an equivalent, unindexed specialization of general stabilizer or word-pattern results, but no identified source has been found to cover both the quantum separability sandwich and the sharp survival window.

## Value — PASS

The exact critical law resolves a natural quantitative particle-loss question for an infinite family of resource states: rather than just stating a worst-case impossibility, it predicts a sharp probability crossover and gives a finite-size error bound tied to identifiable local quantum entanglement witnesses. The fourth-root exponent and Poisson curve can benchmark random-erasure experiments and mathematical models without needing entanglement-magnitude reconstruction. This is a structural phase-window calculation, not an arbitrary tabulated case or a mere renaming of the known witness.

## Sources and residual scientific limits

Material read: Han–Zhang–Zhang, arXiv:2606.08561v1, publicly accessible full manuscript, especially stabilizer-marginal method and cycle proof; Silberstein–Arnon-Friedman (2023), particle-loss Bell-violation study; Sajjad et al. (arXiv:2404.09014), depolarizing-noise coherent-information analysis. The exact nature of the survival event, source date, non-full-separability condition, and finite-verifier scope have been cross-checked. The four-site NPT test is not new; only probabilistic retention of *some* entanglement is proved, not broader robustness.

Self-review: passed. Independent audit: not yet performed.
