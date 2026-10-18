# Scientific assessment

## Correctness — PASS

Every red/blue rainbow path has at most two edges, so rainbow connectivity of \(K_{a,b}\) is exactly pairwise distinction of all row and column signatures. The minimal red-edge count follows by a strictly minimizing Hamming-weight exchange. The potentially nontrivial boundary case \(u=v\) is checked separately from \(u\ge v+1\) to ensure the minimum rows automatically separate columns. The complete distribution is obtained by a finite, exact partition-lattice Möbius inversion on row and column equality constraints. Global color swapping establishes coefficient reciprocity around half the number of edges. The standalone checker separately enumerates two-edge paths and the Möbius product for all stated cases, including infeasible \(K_{2,5}\). This is a general proof supplemented by finite validation, not extrapolation from examples.

## Originality — PASS with residual risk

The closest primary source, Barát–Boyadzhiyska–Freschi [1], treats whether a red/blue rainbow-connected coloring exists for broad graph classes and minimum-degree conditions, rather than optimizing how many red edges occur in every such coloring of complete bipartite graphs. Septyanto–Sugeng [2] provide the relevant color-code framework and rainbow connection existence techniques. The row/column-code correspondence and capacity condition are background; neither inspected source states the exact minimum red-edge weight, its entire labeled optimizer class, or the full weighted rectangle-partition formula. Searches using the precise optimization and its equivalent binary-array and twin-free bipartite formulations did not identify covering literature. A classical minimum-weight separating-system or weighted enumeration result may still be unindexed; its absence from search results is not proof of nonexistence.

## Value — PASS

For a standard and actively studied two-color rainbow-connectivity problem, color *existence* is only one question; here the number of edges receiving a designated costly color is minimized exactly, and the complete space of optimal assignments is counted for every feasible bipartition size. The separate partition formula supplies the full edge-color resource distribution, not only an extremal number. The \(u=v\) boundary and the \(u=2^v\) endpoint are included without special exceptions. This is a natural complete two-parameter optimization and enumeration, not a fixed small-order calculation or a reparameterized existence criterion.

## Closest literature and remaining scope

[1] J. Barát, S. Boyadzhiyska, A. Freschi, *Rainbow connecting \(2\)-colorings of super-Dirac graphs*, arXiv:2609.11437 (2026-09-10).

[2] F. Septyanto and K. A. Sugeng, *Color code techniques in rainbow connection*, Electron. J. Graph Theory Appl. 6(2) (2018), 347–361, DOI:10.5614/ejgta.2018.6.2.14.

Only red/blue, complete bipartite graphs with both sides of size at least two, named vertex labels, and named colors are claimed. Independent replication or bibliographic review might uncover an equivalent published weighted matrix enumerator.

Self-review: passed. Independent audit: not yet performed.
