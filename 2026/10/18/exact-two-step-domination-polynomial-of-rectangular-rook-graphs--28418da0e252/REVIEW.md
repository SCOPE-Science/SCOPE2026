# Scientific review: two-step-domination polynomial of rectangular rook graphs

## Correctness — PASS
For each vertex, exact distance-two coverage is equivalent to finding a selected cell outside its row and column. Requiring two different external columns per row is necessary and sufficient. Partitioning by zero, one or at least two columns containing multiple selected cells is disjoint and exhaustive, and the three combinatorial enumerators sum to the claimed symmetric polynomial. The minimum-set patterns follow directly from the same condition. The exact verifier directly enumerated 714,576 vertex subsets across 13 graph dimensions and compared every coefficient, plus 841 larger symbolic parameter checks. These finite tests support but are not a proof of the infinite identity; that identity is justified by exhaustive case algebra in `RESULT.md`.

## Originality — PASS, residual priority risk
The mathematical object also equals the total-domination enumerator of the tensor product of two complete graphs. Zhao–Shan–Ahangar (2013), Theorem 3, already provides the minimum cardinalities 3 and 4, which are explicitly excluded from the novelty claim. Burcroff–O'Brien (2021), Section 5, concerns ordinary domination, not the total-domination polynomial; Das–Das–Islam (2026) studies complexity, not these coefficients. The entire distribution and the exact counts of minimizers were not located in compared accessible primary material or mathematical-record searches. A directly relevant Dod (2016) graph-product paper has only its abstract accessible; its complete results were not inspected. This creates a stated bibliographic uncertainty and means publication priority has not been independently established.

## Value — PASS
Two-step domination is a natural exact-distance version of vertex coverage for which complexity is nontrivial even on regular graphs. The theorem gives a polynomial-size formula for the complete enumerative distribution in a natural infinite regular family, not just another bound or a previously known minimum. It also classifies all minimizers geometrically, separating the two-row obstruction from the injective three-cell regime.

## Scientific limitations
The claim concerns labelled subsets, not symmetry orbits. It is limited to two-factor rook graphs; one-factor complete graphs have no distance-two vertices. No finite run establishes an infinite statement by itself. Bibliographic priority remains subject to full inspection of Dod (2016) and independent review.

Self-review: passed. Independent audit: not yet performed.
