# Mathematical assessment

## Correctness

**PASS.** The result concerns a fully specified finite absorbing Markov chain: pairs of states in the classical Černý automaton with two independent equiprobable letters, and a uniformly sampled unordered starting pair. A unique coordinate representation of all pairs gives the complete transition list. The first- and second-moment Bellman equations are solved by explicit polynomial potentials, including the odd- and even-diameter boundary cases, and aggregate pair averages reduce to polynomial identities by summation. Both supplied Python verifiers check the local equations and aggregate identities for every pair state through \(n=80\), and an independent rational linear-system solution verifies the statewise moments through \(n=11\). These are supporting finite checks; the proof for all \(n\ge2\) is the symbolic Bellman substitution and finite-sum identity in `RESULT.md`. Main residual correctness risk is an overlooked formal substitution or algebraic identity in the all-parameter presentation; no external mathematical audit has been conducted.

## Originality

**PASS, with a residual publication-priority risk.** Gusev, *Synchronizing automata with random inputs* (2014, arXiv:1404.6731), treats exactly the relevant random-input family. The inspected full Section 3 supplies first-moment equations and closed values for the hardest initial pair under general Bernoulli probabilities. It does not provide this paper's uniform-initial-pair second moment, full variance polynomial, or asymptotic coefficient of variation. The recent Lipin–Volkov work (2026, arXiv:2601.18362) concerns adversarial games and deterministic shortest words, while Szykuła's 2026 survey (arXiv:2608.24245) addresses deterministic synchronization questions; neither implies an absorption-time variance formula. Direct indexed searches for the precise second-moment invariant and equivalent descriptions yielded no covering result. Gusev's underlying chain and first-moment calculations are explicitly credited and are not claimed as new. The result is algebraically reducible to that chain, but its second-moment solution and exact aggregate are not a specialization of Gusev's first-moment formula. Unindexed, unpublished, or inaccessible equivalent work could exist.

## Value

**PASS.** The variance of a random synchronization delay is a natural reliability statistic distinct from its average. The theorem settles the exact variance at every automaton size and reveals a nonvanishing relative-fluctuation limit \(\sqrt{7/5}\). It shows that fluctuations remain comparable to the mean in the second-moment sense, a reliability feature invisible in first-moment bounds. The full all-length result goes beyond a finite census or an isolated optimization and does not assert an unrelated breakthrough about deterministic reset thresholds.

## Scope and limitations

The stochastic law averages over both a uniform unordered pair and independent fair input letters. It is not a fixed-pair variance formula, not an all-state reset-time result, and not a biased-input result. The second-moment recurrence is specialized to this model. Scientific review here is limited to the supplied exact proof and checks, and broader literature priority may require further investigation.

Self-review: passed. Independent audit: not yet performed.
