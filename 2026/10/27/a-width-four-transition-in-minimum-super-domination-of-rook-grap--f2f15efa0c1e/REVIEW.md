# Scientific review: optimal super domination of rook graphs

## Correctness — PASS

The proof derives a necessary and sufficient private-neighbor condition from the original graph definition: for each omitted cell \((i,j)\), either its row is occupied exactly once and an empty column exists, or its column is occupied exactly once and an empty row exists. This enforces an incidence star forest, bounds its size by the maximum of the column-transversal and crossed-star possibilities, and classifies equality. Non-surjective functions and the four uniquely determined crossed-star parameters then give the exact seven-case counts. The separate executable checker compares the stated incidence condition with the original private-neighbor definition for 1,810,648 tested complements, and checks the complete optimizer families where enumeration is exhaustive. Finite checks supplement, rather than establish, the proof.

## Originality — PASS, with bibliographic risk

Klein, Rodríguez-Velázquez and Yi, Theorem 30 of arXiv:1705.00928, already determine the numerical minimum for rectangular complete-graph Cartesian products, so it is excluded from the originality claim. Their argument establishes an upper bound on the size of omitted-cell sets but does not enumerate every optimum or state the width-four/width-five change in the growth of their number. Ghanbari, Jäger and Lehtilä, Section 6 of arXiv:2209.01795, count minimum super dominating sets for other graph families, not rectangular rook graphs. The present claim is the complete optimum-set classification and the exact labeled count, a strict refinement not implied by a bare extremal cardinality. Equivalent or unindexed prior enumerations remain a priority risk.

## Value — PASS

Counting minimum super dominating sets is a motivated invariant in the cited 2022 enumerative literature, and the known minimum cardinality for rook graphs does not predict the optimizer distribution. The precise star-forest equality cases expose a structural transition: at fixed width \(3\) or \(4\) the number of optimizers grows exponentially with length, while at each fixed width at least \(5\) it is quadratic. The result classifies a natural infinite graph-product family rather than an arbitrary finite slice.

## Sources and limits

The closest full primary texts inspected were arXiv:1705.00928 (notably Theorem 30, pages 13–14) and arXiv:2209.01795 (notably Section 6, pages 16–24). Public mathematical-record and targeted literature searches were also compared by object, invariant and implication. The proof is restricted to two complete-graph Cartesian factors of orders at least two. All scientific assessments are internal self-review assessments; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
