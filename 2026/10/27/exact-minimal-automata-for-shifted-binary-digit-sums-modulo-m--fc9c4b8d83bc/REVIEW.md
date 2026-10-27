# Scientific review

**Correctness (PASS).** The prefix/suffix splitting formula gives an explicit reachable Moore automaton. Distinct carry values are separated by the suffixes \(2^L-e\), whose digit-sum difference changes by one with \(L\); distinct residues at equal carry already differ on empty input. The proof shows every zero-carry residue is reachable, classifies all remaining states by a finite prefix horizon, and counts the dyadic shifts directly. Independent partition refinement and direct computations checked 1,032 parameter pairs and 132,096 test inputs.

**Originality (PASS on examined evidence).** The relevant 2025 full-text treatment of linear subsequence complexity considers the binary Thue--Morse shift in most-significant-first form and establishes bounds, rather than the exact, all-moduli, least-significant-first residual count. The 2021 multiplication/translation theorem is about a different set transformation. Existing exact parity-only or different-numeration classifications are weaker or structurally inapplicable. A hidden general result in older automata references or unindexed material remains a historical-priority risk; failure to find an identical theorem is not a uniqueness proof.

**Value (PASS).** The exact minimal-state count for every residue modulus and every shift answers a natural automata minimization question in a common family of automatic sequences. The proof gives a reusable separation criterion for digit-sum residuals. The closed dyadic staircase reveals a modulus-sensitive transition that is invisible from parity-only data. This is not an asymptotic bound for all representations, and no analogous most-significant-first claim is made.

**Closest literature and limits.** Moradi--Rampersad--Shallit, arXiv:2512.10017v1 (2025); Charlier--Cisternino--Massuir, EJC 28(3) P3.12 (2021); Moradi--Popoli--Shallit--Vukusic, arXiv:2603.18858 (2026). The tests are finite and supplementary. Independent mathematical evaluation has not been performed.

Self-review: passed. Independent audit: not yet performed.
