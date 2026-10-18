# Scientific review

**Correctness — PASS.** For the stated six-particle continuous-time Markov chain, every permitted interchange removes exactly one inversion. First-step conditioning gives a terminating triangular system over exactly 89 nonterminal arrangements. The complete `check.py` computation uses exact rational functions to evaluate that system, compare the final probability against the displayed formula, and prove that its derivative has only positive coefficients. The model is precisely specified, and neither simulation nor an incomplete enumeration is used as a proof.

**Originality — PASS, qualified.** Direct examination of the full 2026 motivating paper and the relevant 2022 oriented-swap study found no finite six-particle, gap-dependent *last interchange type* probability. The motivating results give separate cut-completion marginals and asymptotic sorting speeds, not the joint event determining which cut completes last. The older study uses different interchange rates. Searches for three-species last swaps and exact finite competition revealed no covering formula. The possibility of a general theorem that implies the present small case remains a priority risk.

**Value — PASS.** This is the first nontrivial balanced three-species population (the one-per-species case is a two-clock race), and the identity of the final overpass is exactly the finite analogue of the bottleneck-cut question studied in the motivating paper. The result determines a previously unprovided natural joint statistic for all positive gap ratios, supplies its full rational law, and proves a sharp bias threshold and monotonicity. It does not pretend to extend the macroscopic theorem or claim a general population-size result.

**Limitations.** The small exact case is not evidence of a universal formula or monotonicity at higher particle counts. Priority is qualified pending independent verification.

Self-review: passed. Independent audit: not yet performed.
