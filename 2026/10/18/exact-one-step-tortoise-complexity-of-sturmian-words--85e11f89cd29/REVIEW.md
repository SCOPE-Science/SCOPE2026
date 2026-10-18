# Review of the exact Sturmian tortoise-complexity formula

## Correctness — PASS

The proof uses mechanical coding by an irrational rotation and enumerates all \(n+1\) factor cylinders from the \(n\) distinct discontinuities \(t_j=\lceil j\alpha\rceil-j\alpha\). At each interior discontinuity the factor changes locally from \(01\) to \(10\), and the tortoise images coincide exactly when the prefix before this swap has no 1. The number of ones in that prefix is \(\lceil j\alpha\rceil-1\), yielding the exact count of identical neighboring images. A separate argument handles the final-bit transition; the empty and one-symbol cases are explicit. Five algebraic irrational slopes were checked by complete finite-cylinder sampling through length 100 and separately by finite-orbit catalogues through length 60. The proof, not the finite tests, establishes the universal quantifiers.

## Originality — PASS within the checked literature

Campbell and Rampersad, arXiv:2604.25811, §3 and §7, define precisely the one-step tortoise equivalence considered here, give a general bounded-defect result for bounded-gap linear-complexity words, provide exact evaluations for paperfolding and Thue–Morse, and raise questions concerning Sturmian tortoise complexity. Their full-text theorem statements do not supply an exact slope-dependent Sturmian formula. Defant and Kravitz, arXiv:1809.09158, introduce the operation but do not enumerate Sturmian factor images. De Luca and Fici, arXiv:2206.00995, enumerate cyclic-conjugacy Lie classes in Sturmian languages; Allouche et al., arXiv:2406.09302, quotient factors by reversal. These are mathematically different equivalence relations and their results do not imply the stated image count. Search comparisons for the exact formula, parameter aliases, and the relevant specialized words did not reveal the same statement. Searches cannot guarantee absolute uniqueness; unindexed or inaccessible literature remains a residual risk.

## Value — PASS

The theorem gives an exact answer to a natural, explicitly motivated question at the boundary of stack sorting and Sturmian factor enumeration. More than determining eventual growth, it locates every merged adjacency in the rotation partition, identifies the precise slope-dependent constant defect, and resolves all finite lengths at once. In particular the plateaus for small lengths and the linear regime are distinguished without requiring numerical fitting; the effect of exchanging the two letters is also specified.

## Limits and status

The formula is restricted to irrational binary Sturmian words with frequency of ones \(\alpha\). The comparison with adjacent complexity invariants does not claim a complete literature census. No external independent audit or validation has been performed.

Self-review: passed. Independent audit: not yet performed.
