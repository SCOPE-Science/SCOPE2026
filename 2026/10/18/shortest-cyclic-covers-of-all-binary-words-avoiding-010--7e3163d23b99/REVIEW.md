# Scientific review

**Correctness — PASS.** The argument derives the exact vertex divergences in the forbidden-factor overlap graph, proves shortest negative-to-positive path lengths, and gives an injection from negative vertices to positive targets, therefore a sharp integral lower bound and a balancing Eulerian construction. The ordinary generating functions follow from an explicitly counted run decomposition. The standard-library checker recomputes graph distances, Euler tours and exact coverage for ten parameter values, and exhaustively checks optimality at the first two values.

**Originality — PASS within examined evidence.** The closest primary works, Moreno–Matamala (arXiv:0711.1695) and Sawada–Gabrić (arXiv:2510.16545), were examined in relevant full-text sections. The former minimizes the lexicographic label of Eulerian de Bruijn sequences of periodically admissible languages; the latter generates cycles for run-forbidden and other Eulerian families. Neither examined result supplies the minimum length of a cyclic cover of *all linearly* admissible \(010\)-avoiding windows. Broader overlap under different terminology, older theses and unindexed results remain risks. A published formula for forbidding adjacent equal symbols or longer runs would not by itself cover the alternating pattern \(010\).

**Value — PASS.** This is a nontrivial exact solution to a natural shortest-cover problem on a non-Eulerian restricted de Bruijn graph: an infinite family of sharp lengths, a rational excess-cost series, a matching lower bound, and an explicit constructive algorithm. The result explains the unavoidable duplicated windows rather than merely producing finite numerical examples.

**Limits.** No claim is made for other forbidden patterns or uniqueness of optimum cycles. The finite checker is not a substitute for the infinite proof. Some less accessible relevant theses could not be inspected fully; independent external validation is absent.

Self-review: passed. Independent audit: not yet performed.
