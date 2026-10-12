# Self-review

**Correctness — PASS.** The exact partition recursion gives level sizes \((2,12,88,640,4656)\) and \((7,2,0,0,0)\). Its code comprises precisely \(33872\) distinct six-letter words; the standalone program exhaustively verifies that the proper-prefix and proper-suffix sets are disjoint for each of five lengths. The constrained class has \(R_2=\cdots=R_5=\varnothing\) and therefore a code size of \(a(9-a)^5\) for \(1\le a\le8\), with global integer maximum \(33614\). These are complete finite arguments, not extrapolations.

**Originality — PASS, with priority risk.** The 2024 Stanovnik–Moškon–Mraz publication states the contradicted claim as Conjecture 1 (arXiv:2307.12593, doi:10.1007/s10623-023-01344-z). The same author prints it again as Conjecture 5.1 in a 2025 dissertation. The authors' separate 2024 almost-balanced/run-restricted follow-up addresses a distinct constrained setting. Searches for the exact cardinalities, q=9/n=6, and cross-bifix-free equivalents revealed no indexed covering counterexample; unseen and unindexed sources remain possible.

**Value — PASS.** The result settles a concrete published universal conjecture negatively, using an explicit witness whose size is \(258\) above the cutoff-restricted maximum. It demonstrates that the cutoff cannot be imposed without losing optimality. The true maximum \(S(9,6)\), smaller parameters, and Blackburn's separate sufficiently-large-alphabet conjecture are not resolved.

The self-contained finite witness, full construction proof, and reproducibility program provide checkable evidence. A later independent mathematical review and comprehensive priority study have not been performed.

Self-review: passed. Independent audit: not yet performed.
