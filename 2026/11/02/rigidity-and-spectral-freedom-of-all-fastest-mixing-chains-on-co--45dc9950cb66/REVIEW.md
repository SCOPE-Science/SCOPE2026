# Review of all-optimal-chain rigidity on complete split graphs

## Correctness
PASS. A two-dimensional quotient-mode Rayleigh bound and a trace-compression bound on the independent-set zero-sum subspace give a matching universal lower envelope for the mixing objective. Equality on a positive-semidefinite spectral envelope forces all cross-edge probabilities to coincide, *without* assuming invariant edge weights. With cross weights fixed, the remaining eigenvalues reduce exactly to the nonzero-index Laplacian spectrum of the independently weighted clique, yielding necessary and sufficient interval and degree conditions. Boundary \(q=2p\), positive-clique-connectivity \(p>q\), and a nonuniform clique example were checked. The exact-rational program checks 70 small parameter pairs and 1,575 additional asymmetrically weighted feasible cases; the infinite theorem is analytic.

## Originality
PASS, with residual priority uncertainty. Boyd--Diaconis--Parrilo--Xiao (2009, Section 5.4.2) solve the complete-bipartite symmetric optimization and Jafarizadeh (2020, Theorem 1 and star formulas) already implies the **optimal value** on split graphs as a clique lift. Consequently that value is NOT attributed to this result. The assessed increment is a full characterization of *every* global optimizer over unrestricted edge weights, including forced uniformity of the cross block and spectral / degree constraints on all feasible optimal clique blocks. The inspected material provides a lifted optimal chain, not these all-optimal-face necessary-and-sufficient statements. Further specialized literature may contain such a classification.

## Value
PASS. Global-optimal-face structure matters when a designer must preserve or eliminate internal connections in addition to reaching the fastest rate. The theorem shows a nontrivial distinction: cross connections are always rigid, while the internal clique can range over nonuniform optimal graphs, must retain connectivity below one imbalance threshold, and must be deleted at another. The result is an all-parameter classification rather than a restatement of the known best objective value.

## Scope and residual risks
Only symmetric stochastic chains with self-loops permitted and at least two vertices in each part are covered. No independent validation is implied. Jafarizadeh's general lifting theorem is explicitly acknowledged as covering the rate and one optimal allocation. Additional published work on optimal-face uniqueness and weighted split graphs could cover the incremental classification; no absolute priority claim is made.

Self-review: passed. Independent audit: not yet performed.
