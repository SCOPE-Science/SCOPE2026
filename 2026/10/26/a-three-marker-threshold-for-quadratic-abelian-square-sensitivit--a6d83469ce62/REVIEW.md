# Scientific assessment

**Correctness — PASS.** The classification separates squares with zero and two marked symbols, and inclusion–exclusion distinguishes two adjacent-one pairs when their intervening gaps match. The parity-restricted lattice counts yield both exact neighboring-word formulas. The proof that any swap moves only two zero gaps by one and changes parity counts by at most a constant per row establishes the low-support linear bound. `verify_swap.py` independently enumerates substrings over every four-gap tuple of total gap length at most ten, tests the formulas and local swaps, and contains no assumed infinite conclusion.

**Originality — PASS, qualified by priority risk.** Fici–Mignosi's inspected 2015 Proposition 1 has a two-marker quadratic construction, not a one-swap sensitivity comparison. Kociumaka et al. study maximal numbers of distinct nonstandard squares, not sparse-support local sensitivity. The existing exact two-marker result is a strict lower-support prerequisite, not an implication of the displayed three-marker swap construction. Searches by adjacent transposition, one swap, fixed sparse composition and Abelian-square factors found no covering indexed statement; absence from a retrieval index is not proof of first discovery. Alternative terminology or unindexed results remain possible.

**Value — PASS.** The construction demonstrates a structural instability invisible to global maximum counts: a single local edit separates two large families of identical factor strings. The lower-support proof makes the example a sharp threshold theorem, rather than an arbitrary three-marker calculation. Sensitivity to local edits of repetition statistics is relevant to robust string analysis.

**Limitations.** Exact globally largest adjacent-swap difference and generalization to non-Abelian repetitions are not established. The original 2015 literature has the lower-support quadratic construction, which is explicitly credited.

Self-review: passed. Independent audit: not yet performed.
