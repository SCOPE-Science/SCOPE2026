# Scientific review: zero forcing on complementary paths and cycles

## Correctness — PASS

The argument computes the number of initially white neighbors exactly as the number of whites minus at most two neighbors in the original graph. This excludes every forcing set smaller than \(n-3\). With three white vertices, the first force exists exactly when a blue degree-two original-graph vertex has both neighbors white; after that force, two whites always disappear by the absence of twin pairs in paths and cycles of order at least five. The incidence counts explicitly account for every duplicated center/triple pair, including the two triple-center configurations at order six. This proves the complete polynomial formulas, not merely an asymptotic assertion. Independent direct simulation of all vertex subsets for orders \(5\) through \(14\) confirms the derived coefficients and set-level classification.

## Originality — PASS with residual risks

The closest inspected literature contains the zero-forcing number of complementary paths and cycles (Curl et al., 2022), plus general high-degree polynomial coefficients and exact polynomials of noncomplemented paths and cycles (Boyer et al., 2018). Neither supplies the newly computed minimum-set multiplicity coefficient, its exceptional six-cycle correction, or the equality of all other coefficients across the two complementary graph families. Searches under co-path, antihole, complete-graph-edge-deletion, zero-forcing-polynomial, and minimum-set-count terminology, including mathematical result records, yielded no covering earlier statement. Overlooked tables or separately circulated results remain possible; the search does not prove uniqueness or chronological priority.

## Value — PASS

These are canonical dense complements of sparse connected graph families studied in the complement-zero-forcing literature. The coefficients count all choices of optimal initial conditions, a finer graph invariant than the known minimum cardinality. A single natural edge deletion can strictly change the minimum-set count without changing the minimum itself, and the exact difference has an exceptional six-vertex case. The result is a motivated complete classification across two infinite families rather than an arbitrary finite instance.

## Scientific limits

Only \(n\ge5\) and the two specified complement families are covered. The algorithmic checks are exhaustive only on bounded orders; the infinite proof is combinatorial. Independent priority assessment and scientific validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
