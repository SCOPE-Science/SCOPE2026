# Self-review

## Correctness — PASS

The critical equivalence is exact: on a simple unit-valued graphical instance, all-good EFX fails precisely on a directed edge from a source to a vertex with at least two incoming edges. On a cycle, this is equivalent to a cyclic binary \(010\) or \(101\) pattern. The forbidden-pattern equivalence, even-parity change set, independent-cycle counting polynomial, refined binomial coefficient, and bounded-correction asymptotics are proved with all quantifiers and edge cases. `verify.py` independently checks the literal EFX inequalities and the formulas for every \(3\le n\le14\). The program is supporting evidence, not an infinite proof.

## Originality — PASS, with residual risk

The closest source, Zeng (arXiv:2609.36498v1), classifies EFX orientability under arbitrary valuations rather than counting valid orientations of a fixed valuation. Zeng–Mehta (arXiv:2404.13527v2) likewise treats existence and structural conditions. Kanellopoulos et al. (arXiv:2512.25033v1) develop decision algorithms and hardness results. Deligkas et al. (arXiv:2409.13616v1) clarify the difference between deleting any good and deleting only positively valued goods. Targeted searches of research records and the literature did not yield the claimed Lucas–period-six formula or the change-count refinement. Classical circular independent-set enumeration itself is not claimed as new. Unindexed papers or a hidden enumerative formulation remain risks.

## Value — PASS

An existential guarantee does not quantify how many allocations are fair or how likely a uniformly random orientation is to be fair. This full-family exact invariant gives both a sharp labeled count and a finer distribution by cyclic direction changes, demonstrating exponential rarity despite guaranteed existence. That is a natural structural robustness question in graphical fair division rather than an arbitrary finite slice. The restricted scope and elementary counting tools are openly acknowledged.

Self-review: passed. Independent audit: not yet performed.
