# Scientific review: sharp token-jump diameter in subdivided cliques

## Correctness — PASS

The classification of maximal matching sizes follows from the original incidence-graph maximality predicate. The size-\(n\) stratum corresponds bijectively to maps without fixed or reciprocal pairs; an edge jump updates one coordinate. Computing allowed targets establishes degree \(n(n-3)\). The explicit routing algorithm resolves permitted direct updates and blocked inverse directed cycles, using at most one nonfinal move for each cycle of at least three coordinates. Reversed disjoint directed cycles require one nonfinal move per cycle, showing exact diameter \(n+\lfloor n/3\rfloor\). The proof checks \(n=3\) separately and does not conflate maximal and maximum. Original-graph predicate checks and exhaustive adjacency comparisons for orders \(3\) through \(6\), plus full all-pair routing at orders \(4,5\), confirm the nonstandard finite boundary cases; general quantifiers rely on proof.

## Originality — PASS, with priority uncertainty

The initial 2019 paper of Baste et al. concerns minimum maximal matchings and approximation bounds; the 2018 paper of Bousquet et al. gives general token-jump matching-distance algorithms and connectivity criteria. The relevant full-text introductions, main results and matching-reconfiguration conclusions were inspected. Neither provides this exact family-specific diameter or the complete two-tier reconfiguration structure. The function count and inclusion–exclusion formula were explicitly located in OEIS A134362 and are not credited as new. Semantic record searches under matching, subdivision, functional-digraph, reverse-cycle and reconfiguration aliases and comparisons with accessible prior local claims did not identify a stronger covering result. There remains priority risk from unindexed literature or different functional-digraph terminology; a negative search alone does not certify uniqueness.

## Value — PASS

An exact exchange diameter measures the worst-case number of local moves needed to convert one optimal matching into another, a natural metric distinct from counting matchings or determining minimum matching size. Here the diameter exceeds the number of originally matched vertices by a sharp cycle-obstruction term and grows linearly, while the same configuration space is regular but coexists with completely frozen minimum maximal matchings. The constructive proof supplies explicit optimal-scale routes and worst-case witnesses, giving nontrivial reconfiguration structure beyond known counting formulas and generic algorithmic reachability.

## Scope and limitations

The result applies only to one-subdivisions of complete graphs and the token-jump rule defined in the mathematical statement. Independent mathematical audit and external validation have not been performed; arbitrary-order assertions rely on the supplied proof, not finite checks. OEIS A134362 predates this result. Equivalent unindexed work is a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
