# Scientific review of the first eight-divisor threshold

## Correctness

PASS. The precisely quantified claim has a complete finite proof via exact subset-cardinality bitsets. Descending updates enforce distinctness, and an induction establishes exact coverage for every sum in \([0,n!]\). A replay over every factorial from \(1!\) through \(12!\) checks \(U_{h-1}\) noncoverage and \(U_h\) total coverage. The 175 missing seven-term targets are all independently listed and checked against the newly recomputed bits. Smaller cases were also checked by a separate C++ word-array implementation. The code and targets are part of this same package; finite evidence does not imply anything for larger factorials.

## Originality

PASS subject to publication-priority uncertainty. Hughes (arXiv:2609.10902, 2026) establishes asymptotic bounds for the same function, not an inspected exact small-factorial table or this 175-target classification. The classical 1990 and 1995 work underlies the knapsack problem and may contain numerical data; the 1995 source was located bibliographically but not read in full. Nearby enumerative work on different divisor families and multiplicative factorial decompositions does not imply these cardinality-constrained factorial sums. Searches for exact values, exceptional endpoint targets, and alternate subset-sum formulations found no equivalent table. An inaccessible table is an unresolved priority risk, not evidence of absence.

## Mathematical value

PASS. This is the complete first crossing of a natural complexity threshold in a named factorial knapsack invariant, not an arbitrary selected integer or an isolated recomputation of a known table. The hard-to-cover set collapses to exactly 175 exceptional integers among 479001600 targets, so it also identifies the complete extremal obstruction set and its unexpected oddness and near-upper-end concentration. A complete finite cutoff is meaningful independently of the unresolved asymptotic growth question, though no later-case theorem is claimed.

## Boundaries and residual risk

Implementation correctness is supported by exact invariants and replay, but the long \(12!\) coverage computation has no independently published certificate. Full texts of some older sources were unavailable, and no human priority audit was performed. No claim is made for \(n\ge13\).

Self-review: passed. Independent audit: not yet performed.
