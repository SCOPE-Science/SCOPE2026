# Scientific review

## Correctness

PASS. The exact bad-phase formula comes from a complete geometric partition of matching sites within each distinct-letter run: a prefix produced by the smaller shift, a suffix produced by the larger shift, and the complementary uncovered interval. Positive shifts smaller than the full period cannot match the run letter anywhere else. Zero uncovered length in every run is equivalent to the precise inequality \(s+p-t\leq\min_j r_j\). Triangular enumeration and optimal-delay uniqueness are then proved with explicit bounds, and finite two-copy equivalence follows because every residue phase is tested. The supplied Python verifier separately enumerates finite cases; it is not substituted for the proof.

## Originality

PASS at the level of the accessible record, with explicit residual risk. The primary paper (Meleshko et al., 2022/2023, arXiv:2207.10171) defines the forward-shift invariant and proves general run/alphabet bounds and NP-completeness, but the inspected relevant full-text sections do not contain a complete classification of shorter-than-period pairs for distinct-run cyclic words, an exact phase-failure count, or the triangular delay-budget spectrum. Published-record semantic searches, web queries about pseudoperiodic run blocks and cyclic shift mismatch, found no dominating formula. A previously unlocated equivalent specialization cannot be excluded. The finite-period checking corollary is not itself presented as novel.

## Mathematical value

PASS. The output is an exact, all-parameter phase diagram for the first nontrivial shift-set cardinality, over arbitrarily many distinct alphabet symbols and unequal run lengths. It identifies when two delays strictly below the primitive period exist, the unique best maximum delay, exactly how the feasible set grows with a delay budget, and the number of failed phases for every rejected pair. This is a structural special-case solution within the general pseudoperiod setting, not a routine renaming or an isolated finite census. No claim is made to solve the general decision problem.

## Closest literature and limitations

J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171, relevant full-text sections 1–2 and 5–7, is the principal comparator. Distinct-letter runs and the restriction to two shifts below the primitive period are essential. The small computational sweep cannot prove an unbounded assertion, and the scholarly overlap search is not an independent specialist audit.

Self-review: passed. Independent audit: not yet performed.
