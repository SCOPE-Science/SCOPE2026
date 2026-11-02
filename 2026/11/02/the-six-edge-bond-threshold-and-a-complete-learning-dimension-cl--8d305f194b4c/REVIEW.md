# Scientific review: graphic-bond static and online shattering

## Correctness

**PASS.** Every bond of a three-path theta graph is either a transversal triple (one edge on each endpoint-to-endpoint path) or a pair of edges from one path; this follows from a connected-bipartition proof. Consequently all theta bonds have support size at most three, bounding online depth. An explicit three-edge shattered transversal establishes equality when all three paths have length at least two. A direct endpoint edge obstructs every shattered triple, while a two-edge support is explicitly shattered. A verified depth-three, eight-leaf tree on the six-edge house supplies the remaining online lower bound, and the six-concept counting bound handles the smaller diamond.

For trees and unicyclic graphs, the proof enumerates all bonds structurally and bounds online depth through the positive-branch forms. For the sharp edge threshold, connected simple graphs with at most six edges and at least two cycles reduce to a handful of graph-core types. The classification is supplemented by exhaustive, independently formulated exact finite verification of 595 connected labeled graphs, with 60 strict-gap labelings all isomorphic to the house. The proof does not infer infinite results from that computation.

## Originality

**PASS within inspected source and database comparisons, subject to historical-priority limits.** The nearest substantive full-text result, Guingona–Kolesnikov–Nierwinski–Soucy (arXiv:2109.04805), proves equality for *all* zero sets of nonzero linear combinations, not the subfamily of maximal proper zero sets. In the graphic representation, the latter corresponds to graphic matroid hyperplanes, or complements of bonds. The house example demonstrates the noninheritance of their equality after the maximal-flat restriction. Duarte et al. (arXiv:2007.04513) define bonds via connected bipartitions and investigate largest-bond computation, not these learning dimensions. Database and literature queries also tested the aliases *minimal edge cuts*, *graphic cocircuits*, *matroid hyperplanes*, *maximum zero sets*, *theta-graph bond concepts*, and *online shattering*; the inspected material did not imply the theorem.

The earlier literature on complete zero-set classes and graph cuts is credited rather than treated as new. Residual risk: an independently published classification under another model-theoretic or matroidal vocabulary may exist; neither search absence nor the local finite census proves historical novelty.

## Mathematical value

**PASS.** The result identifies the first and unique smallest simple connected graph (by number of edges) where VC and Littlestone dimensions of bond concepts separate. It also completely determines both learning dimensions for every simple theta graph, shows exactly which path-length configurations create the gap, and proves equality on all trees and unicyclic graphs. The maximal-hyperplane restriction of a represented linear zero-set class retains maximum online complexity while losing static dimension in the smallest example. This is a structural boundary with direct relevance to online concept complexity of matroid cocircuits, not merely an isolated numerical table.

## Limitations and comparison risks

The theorem does not cover arbitrary multicyclic graphs, minimum-cardinality cuts, or vertex separators. The finite census is complete within its stated graph-size range, whereas broader novelty is established only against the accessible inspected material. External independent validation has not been performed; exact proof and check artifacts are included.

Self-review: passed. Independent audit: not yet performed.
