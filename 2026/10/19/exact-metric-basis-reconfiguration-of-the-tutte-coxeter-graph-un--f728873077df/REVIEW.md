# Review of exact metric-basis relocation on the Tutte–Coxeter graph

## Correctness — PASS

The two complete executable checks enumerate all potential resolving sets of cardinality at most six, using separate incidence constructions and two logically different resolving predicates. The first uses all-pair separation masks; the second compares direct distance signatures. They agree that there are \(32{,}460\) minimum six-sets and no smaller resolving set. Token-jump and token-slide neighbors are constructed in two ways. Verified natural automorphism generators create \(62\) genuine orbits covering all bases; complete breadth-first search of one representative per orbit (and connectedness checks) establishes each full eccentricity profile. The programs and their outputs are included and were replayed. A finite program is used to prove only a finite quantified result.

## Originality — PASS, with explicit residual uncertainty

Bailey's 2013 arXiv paper reports minimum resolving-set size \(6\) for the Tutte eight-cage; this old result is **not** claimed. The inspected §3 and §4 do not provide the all-metric-bases census or jump/slide graph invariants. The generalized-quadrangle bounds of Bartoli and collaborators do not determine either relocation graph. Relevant public metric-basis reconfiguration project summaries concern other graph families. Exact-claim and alternative-name searches did not retrieve the new classification, but nonhits are not originality proof. The listed 2026 *Reconfigurations of Metric Bases* thesis was inaccessible in full and could contain overlap; that risk is not dismissed.

## Value — PASS

This is a complete metric-basis relocation benchmark on the order-two generalized quadrangle (the smallest classical cubic eight-cage). It establishes that all optimal landmark placements are mutually reachable **without adding landmarks** under both legal moves, yet local sliding multiplies worst-case relocation length from eight to twenty. The single maximal-eccentricity jump orbit provides a natural, symmetry-defined obstruction. These are intrinsic whole-space classifications, not routine reformulations of metric dimension.

## Limits

The claim is solely about thirty vertices and optimal six-element resolving sets. No analogous assertion for generalized quadrangles of other orders, larger landmark budgets, or other reconfiguration moves is made. Unindexed literature and unavailable thesis content remain possible overlap sources. The two checkers are separate computational implementations, not an independent outside audit.

Self-review: passed. Independent audit: not yet performed.
