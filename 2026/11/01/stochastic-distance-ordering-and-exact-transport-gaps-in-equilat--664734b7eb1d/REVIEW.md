# Scientific review: complete-bipartite continuum-distance laws

## Correctness — PASS

The theorem concerns two independent points uniformly sampled by **edge arclength** on an equilateral complete bipartite metric graph. Every ordered pair of sampled edges belongs to one of three exhaustive classes with precisely verified counts. The three shortest-route formulas are valid for all points in all edges, including the degenerate star boundary. Direct integration gives the CDF, which is continuous and normalized at its junctions. At fixed vertex count, the CDF difference is the product of a positive reciprocal-edge-count difference and a positive piecewise quadratic. Its unique peak determines total variation; its exact area determines one-Wasserstein distance. The limiting law follows from exact mixture weights.

The accompanying independent shortest-path implementation uses Floyd–Warshall vertex tables, all possible endpoint routes, and exact rational comparisons. It passed 40,570 finite assertions. The general theorem is proved symbolically in `RESULT.md`; these finite checks are not a proof of infinitely many cases.

## Originality — PASS, subject to documented priority risk

Garijo–Márquez–Silveira, *Continuous Mean Distance of a Weighted Graph* (first public preprint arXiv:2103.11676, 2021; open publisher version DOI 10.1007/s00025-023-01902-w, 2023) gives continuous mean-distance algorithms and a formula for equilateral complete graphs. Its accessible Sections 3–4 were inspected, including the general roof-diagram theorem and the complete-graph computation. These results do not assert the full complete-bipartite distance distribution or its sharp stochastic comparison.

Baptista–Kennedy–Mugnolo, *Mean distance on metric graphs* (arXiv:2312.04952, 2023), gives first-moment inequalities, examples, and surgery principles; its accessible introduction and relevant Sections 3–5 were inspected. No theorem there implies this all-threshold stochastic ordering for distinct bipartitions. Bose and collaborators, *Network Farthest-Point Diagrams* (arXiv:1304.1909, first posted 2013-04-06), supplies the continuous network-metric framework but concerns farthest-point queries, not random pair laws. The well-known four-cycle special case follows from the ordinary circle distribution and is not individually asserted as original.

Doyle–Graver, *Mean distance for shapes* (DOI 10.1002/jgt.3190060410, 1982), is a particularly relevant older source. Its available bibliographic/abstract record and later discussion identify mean-distance formulas for constrained graph-shaped families, but its full text was not accessible. This is a genuine unresolved historical-priority risk; a negative search is not a proof of universal novelty. Published mathematical-search comparisons and the accessible cited full texts did not identify an equal or stronger theorem for the exact CDF, first-order stochastic order, and sharp distributional gaps.

## Mathematical value — PASS

Comparing whole distance laws is strictly stronger than comparing mean distances. Under a fixed number of vertices, the class of equilateral complete bipartite networks exhibits a universal and somewhat counterintuitive order: balancing the bipartition adds edges but shifts **every nontrivial distance quantile** upward when the sample measure is normalized total edge arclength. The exact total-variation and Wasserstein gaps quantify this effect optimally, and the star-to-balanced gap persists at size \(2/3\) asymptotically. This is a natural, complete geometric classification with a clear change of sampling space, not an arbitrary fixed-size table. It does not claim the phenomenon for arbitrary weighted networks, for a fixed total network length, or for centered variances.

## Evidence and limitations

The proof is self-contained; the checker has no nonstandard dependencies. Material inspected: publisher HTML of DOI 10.1007/s00025-023-01902-w (Sections 2–4), arXiv-rendered text of arXiv:2312.04952 (introduction, theorems, examples and surgery), the arXiv:1304.1909 abstract and journal summary, and bibliographic information for the older Doyle–Graver article. Absence from a search index does not establish priority; the 1982 full text is a residual limitation.

Self-review: passed. Independent audit: not yet performed.
