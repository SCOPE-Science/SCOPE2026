# Scientific review: cyclic-permutation window antidictionaries

## Correctness

**PASS.** The exact minimum span of a pattern is one plus the sum of its positive cyclic increments, since every next match can be greedily chosen in the periodic stream. Endpoint deletion removes the corresponding increment; an interior deletion either removes no net span or exactly one full period, depending on whether two neighboring increments sum above the alphabet size. Requiring every single-letter deletion to be visible yields the two necessary-and-sufficient inequalities of the language classification. A weighted finite-state transfer then gives the general rational bivariate generating function, and the two-increment alphabet simplifies to a denominator encoding the Padovan recurrence. The pole analysis supports the asymptotic formula. The actual packaged independent checker enumerates all window-subsequence sets, tests every deletion, compares complete antichains in 25 finite cases, and separately checks the binary length distribution. Enumeration does not substitute for the unrestricted proof.

## Originality

**PASS, with bounded bibliographic risk.** The 2022 primary work on bounded-range subsequences supplies the underlying observation model, p-minimality definition, general hardness results, and circular-word motivation; its relevant full-text sections do not state the cyclic-permutation-window antichain or exact generating function. The 2021 foundational work and the 2025 follow-up focus on a single linear word and general enumeration algorithms. Separately known exact minimal-absence spectra for fixed *linear* repeated-permutation words count a different language: here a target is visible if it is a subsequence of any of the periodic phases' windows. Taking minimal forbidden elements of the intersection of the phase-specific absent languages is not the same as combining their individual minimal forbidden counts. Targeted semantic database searches, phrase/alias searches, and these statement-level comparisons found no equivalent or stronger covering result. Unindexed literature and uninspected peripheral material remain residual risks; absence of a search hit is not used as a proof of novelty.

## Mathematical value

**PASS.** The bounded-window observation is a natural model in stream analysis, for which general minimal-absence problems are algorithmically nontrivial. The theorem gives the *complete* symbolic minimal-obstruction antichain for every window length and alphabet size in a canonical periodic family, not merely examples or a single small cutoff. The exact all-alphabet length enumerator and, in the binary case, the explicit length spectrum and plastic-constant growth quantify how a period-two trace nevertheless has exponentially many irredundant forbidden patterns. This distinguishes window-obstruction complexity from both unrestricted subsequence universality and the fixed-linear-word minimal-absence counts. The contribution is restricted to streams with one occurrence of each letter per period; it does not resolve the corresponding general hard problem.

## Closest sources and limits

Primary literature: Kosche–Koß–Manea–Pak (arXiv:2207.09201); Kosche–Koß–Manea–Siemer (arXiv:2108.13968); Manea–Ringleb–Siemer–Winkler (arXiv:2504.21471). Exact linear repeated-permutation spectra are a close but nondominating comparison. Residual risk is an unindexed circular/window-specific formula. The general matrix rational function is exact for every \(q\ge2\); its plastic-constant asymptotic is asserted only when \(q=2\). Tests cover finite domains and do not establish the infinite quantifiers.

Self-review: passed. Independent audit: not yet performed.
