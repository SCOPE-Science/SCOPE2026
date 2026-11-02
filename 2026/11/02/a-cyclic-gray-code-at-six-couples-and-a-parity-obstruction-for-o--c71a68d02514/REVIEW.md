# Scientific review: ménage transposition Gray codes

## Correctness — PASS
A symbolic determinant calculation gives the exact signed count for every integer \(n\ge3\); every allowed transposition reverses sign, proving the all-odd Hamiltonian-path obstruction. For the positive boundary, the 80-index witness is checked against all admissible six-permutations, with all 80 different and all 80 consecutive cyclic steps legal. Separately implemented Python and C++ routines agree on 80 states, 207 edges, eccentricities 5:48 and 6:32, and the signed counts. The 13-state five-permutation graph is exhaustively enumerated. Scope is expressly limited to the certified dimensions for the positive statements.

## Originality — PASS, residual risk
The full texts of Shevelev–Moses (arXiv:1101.5321, particularly Introduction and Section 2), Zeilberger (arXiv:1401.1089, restricted-position enumeration), and Bonamy et al. (arXiv:1904.06184, Introduction/related work and reconfiguration definitions) were compared by their actual implications. The first two count ordinary admissible permutations; the latter treats general matching-flip reachability and complexity. None of the examined statements delivers the odd-size signed obstruction together with the explicit 80-arrangement Hamiltonian Gray code. Closest research-record hits on derangement swaps concern only one forbidden diagonal or neighboring-position swaps. A previously unpublished or unindexed exact Gray code remains a residual risk; database nonhits alone are not novelty proof.

## Value — PASS
The standard ménage recurrence provides cardinalities but does not tell whether all arrangements can be generated cyclically by one permitted local change. The sharp first nontrivial positive size, the finite 80-state Gray code, and an all-odd algebraic impossibility distinguish enumerability from local traversability. The negative obstruction applies infinitely often and the explicit positive witness is a reproducible benchmark for Gray-code generation or four-cycle perfect-matching switches. The exact radius and diameter are supporting invariants, not a substitute for the structural claim.

Self-review: passed. Independent audit: not yet performed.
