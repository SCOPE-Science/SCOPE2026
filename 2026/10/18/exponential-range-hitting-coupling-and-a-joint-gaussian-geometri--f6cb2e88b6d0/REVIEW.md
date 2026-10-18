# Scientific review

## Correctness

**PASS.** The proof identifies cycle coverage with the first time the lifted walk's integer range has width \(n-1\). It constructs a concrete event on which both the cover time and final vertex agree *pathwise* with a random hitting-level pair. The two failure terms are rigorously bounded using the geometric law of the ultimate negative minimum and a strong-Markov gambler's-ruin estimate. The passage-time variance follows from a first-step recursion, while a finite-prefix conditioning argument proves asymptotic independence rather than merely convergence of the marginals. Exact rational and exhaustive finite-path diagnostics pass. The diagnostics do not prove the infinite results, for which the written argument supplies the necessary quantifiers and limiting steps.

## Originality

**PASS, with priority risk.** The closest full-text source is Idnani and Salem, arXiv:2610.15115 (2026), which gives the biased cycle's marginal last-covered-vertex law; its Theorems 3.4 and 4.1 and relevant concluding discussion do not contain a joint time-location limit or a finite-\(n\) exponential *pathwise* comparison with an ultimate-minimum-indexed hitting time. Buchanan, Horn and Rombach, arXiv:2209.08079, address uniformity of last-visited vertices for simple walks on directed graphs; they do not establish this biased time-location coupling. The classical gambler's-ruin, renewal CLT, and symmetric cycle cover-time tools are correctly treated as prior ingredients. Searches of mathematical records and prior accessible claims found no direct equivalent. An unindexed earlier result or an unexamined stronger drifted-range theorem could still imply the present assertion; independent priority verification is outstanding.

## Mathematical value

**PASS.** The motivating literature quantifies *where* a biased cycle walk finishes, while applications to patrol and exploration also require knowing *when*. The explicit joint exponential coupling supplies a path-level explanation and a finite-size approximation for that two-observable problem. It yields a precise Gaussian–geometric product limit and conditional asymptotic cover-time laws for each fixed terminal offset. This is structurally more informative than repeating the known geometric marginal or a generic hitting-time CLT. The result is limited to fixed strictly positive drift in one dimension and does not quantify the central-limit convergence rate.

## Sources, comparison, and limits

The motivating preprint is Idnani–Salem (2026), arXiv:2610.15115; the directed-graph last-visit comparison is Buchanan–Horn–Rombach (2022/2023), arXiv:2209.08079. Background on gambler's ruin and symmetric-cycle cover times is standard (Levin–Peres, *Markov Chains and Mixing Times*, Chapter 11; Aldous–Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6). The mathematical result remains subject to independent examination of proof and priority. A negative literature search is not itself proof of novelty.

Self-review: passed. Independent audit: not yet performed.
