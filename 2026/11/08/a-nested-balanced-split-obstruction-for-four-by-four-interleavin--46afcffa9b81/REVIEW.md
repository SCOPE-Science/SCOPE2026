# Scientific review of the four-by-four interleaving claim

**Correctness — PASS.** Every hypothesis is an explicitly enumerated length-eight word with exactly four letters of each type, and all 16 queries are evaluated exhaustively by integer masks. The proof supplies a depth-five construction by successive first-element splitting, plus a finite exhaustive upper-bound certificate showing that every potential depth-six root fails. The executable replay checks the decisive counts and independently computes the minimax recursion.

**Originality — PASS within inspected material.** Chase and Freitag (arXiv:1904.10122v1) present the general dimension framework, not this exact two-chain profile. Li, Sun and Zhang (arXiv:1610.03266v1) study the standard worst-case number of comparisons needed to merge, which has different decision-tree quantifiers and does not imply the maximum complete-tree depth. The earlier asymmetric three-plus-four first-query-count obstruction is excluded from novelty; the square four-plus-four case has a distinct nested obstruction even after perfectly balanced root splits. Results under older alternative nomenclature remain a residual priority risk.

**Value — PASS.** The first balanced-square failure is a natural threshold in an elementary but highly structured concept class. Its mechanism demonstrates that a balanced first comparison and the information-theoretic number of leaves are insufficient for optimal adaptive shattering, and isolates the exact downstream obstruction. This structural distinction is the mathematical motivation for the finite invariant; no unsupported larger-size extrapolation is made.

Self-review: passed. Independent audit: not yet performed.
