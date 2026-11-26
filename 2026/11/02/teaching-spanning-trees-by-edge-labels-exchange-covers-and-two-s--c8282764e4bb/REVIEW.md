# Independent mathematical audit

## correctness

PASS

For each single exchange, a teaching sample must hit the two coordinates that change. Conversely if a different tree T′ agrees on the sample, take e∈T minus T′ and an f∈T′ crossing the cut of T−e. Such an f is outside T; both changing edges are unqueried, and they form an exchange. Thus the vertex-cover criterion is exact for every sample. König gives the cardinality result. For weights place query costs on source-to-tree and cotree-to-sink arcs and use a capacity above the sum of all costs on each directed tree-to-cotree exchange arc; finite optimal cuts give precisely minimum-cost covers. Hall on F⊂T counts |F| tree and |N(F)| cotree edges crossing the components of T−F. Tree packing gives the Hall inequalities; for the converse, refine any partition into its induced connected components without changing the crossing count and choose T connected within each refined part, so the corresponding F gives the required partition bound. On the other side, taking F=N(Y) for cotree edges Y implies F∪Y has the same components as forest F, so under the two-forest bound |Y|≤|F|. Conversely a violating induced connected subgraph admits an internal tree extended to T, and its internal cotree edges violate Hall. The K_{p,q} cases are exhaustive: a singleton shore is a tree; two stars cover a two-vertex shore; the listed K_{3,3} remaining four edges form a path; the two disjoint K_{3,4} trees extend by two separately assigned edges at each new vertex. At K_{3,4}, r=c and both characterizations apply. The bridged K5 example has an isolated bridge coordinate in the exchange graph and a core with two disjoint spanning trees, so it gives 4 versus bounds 5 and 6. An independent replay, python3 /workspace/checks/05_cover_certificate.py, exhaustively compared every sample with all-tree and single-exchange consistency for 3,494 target/sample pairs over 43 connected graphs through four vertices (135 targets), and checked the K_{3,4} packing. Larger frozen verification counts are recorded evidence, not a fresh run.

## originality

PASS

The supported distinct result identifies exactly which samples teach each fixed target via its fundamental-exchange graph, including weighted sampling. It connects the all-target teaching extrema to classical matroid packing/partition criteria and yields the complete-bipartite formula. Credit the graph conditions and shattering ranks to prior work; the pointwise teaching reduction is not given by those results or by the inspected alternative teaching models.

## value

PASS

Testing sample uniqueness against all spanning trees could involve exponentially many hypotheses. The exact criterion reduces all those constraints to one bipartite instance determined by fundamental paths, and supports minimum-cost teaching even when positive and negative edges have different costs. The graph-wide extremal statements characterize when one of the two obvious samples is optimal for all targets, and give an exact uniform value for a canonical graph family. The value is the teaching application and local-to-global bridge, not a new proof of bipartite matching duality or matroid union.

The dated certificate retains the supplied scientific assessment, sources and limitations.
