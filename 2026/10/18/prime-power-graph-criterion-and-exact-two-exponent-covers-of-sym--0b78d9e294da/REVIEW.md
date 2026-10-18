# Self-review

**Correctness — PASS.** The graph criterion is a deductive if-and-only-if theorem: maximal distinct-prime powers of an order cost at most the permutation degree; the two-set pairwise intersection property forces each permutation's entire prime-power support onto one covering exponent. Normalization by the group exponent and an exhaustive divisor scan prove finite optima. The supplied standalone verifier enumerates every permutation order by cycle-length recurrence, every divisor of the group exponent, and compares the graph and full-order residuals on every case through degree 40. Its recorded output passed; no infinite conclusion is inferred from the finite table.

**Originality — PASS within compared evidence.** The closest inspected Xu–Regan work defines and constructs covers, but does not characterize exactly two-exponent covers by the compatibility graph or give the minimax table. The full Bulatov–Karpova–Shur–Startsev preprint concerns shortest positive identities instead. Exact, alias, parameter, and broader-coverage searches were made against mathematical research records and compared with accessible preceding claims. Full text of Karpova–Shur 2021 remained uninspected, so an equivalent previously reported result cannot be excluded.

**Value — PASS.** The two-exponent minimax problem is the first fixed-cardinality nontrivial case of the covering method of Xu–Regan, where the largest exponent directly controls a constructive upper bound for positive identities. The prime-power graph equivalence eliminates higher-cardinality cycle supports exactly and exposes the special two-index intersection mechanism; the initial 38-degree exact classification supplies a reproducible benchmark with clear potential for subsequent optimization. It does not claim shortest word identities or improved asymptotic state complexity.

**Limitations and closest work.** Xu and Regan, arXiv:2610.11098v1, Sections 3–4; Bulatov et al., arXiv:1609.03199v1, Section 3; Karpova and Shur, Algorithmica 83 (2021) (full text not reviewed). The 38 certified values do not imply behavior above degree 40.

Self-review: passed. Independent audit: not yet performed.
