# Exponential domination flags and a three-replacement barrier in the Tutte–Coxeter graph

## Finding
Let \(G\) be the Tutte–Coxeter graph, equivalently the point–line incidence graph of the generalized quadrangle \(\operatorname{GQ}(2,2)\). Both the (blocking-source) exponential domination number and the porous exponential domination number of \(G\) are \(4\). Exactly \(45\) four-vertex subsets satisfy either optimum condition. They are indexed bijectively by the \(45\) incident point–line flags \((r,L)\) of \(\operatorname{GQ}(2,2)\): retain the other two points on \(L\) and the other two lines through \(r\). Every such optimum contains two points and two lines.

For distinct optimum sets \(S,T\), \(|S\cap T|\le1\). Consequently a simultaneous replacement of fewer than three selected vertices can never move between optima. Define the exact-three-replacement graph by joining \(S,T\) when \(|S\cap T|=1\). It has \(45\) vertices, \(450\) edges, degree \(20\), radius \(2\), and diameter \(2\). The intersection histogram among its \(\binom{45}{2}=990\) unordered pairs is \(540\) with intersection zero and \(450\) with intersection one.

## Assumptions and scope
All graphs are finite, simple, and undirected. Fix six labels \(0,\ldots,5\). The fifteen *points* are the duads (two-element subsets), and the fifteen *lines* are the synthemes (partitions into three duads). A point is adjacent to a line exactly when the duad is a block in the partition. This realizes the unique \(\operatorname{GQ}(2,2)\) and its thirty-vertex, cubic, girth-eight Levi graph.

For any vertex subset \(S\), and for each unselected vertex \(u\), its blocked exponential weight is
\[
 w_S(u)=\sum_{s\in S}2^{1-d_{G-(S\setminus\{s\})}(s,u)},
\]
with the contribution zero if no path exists. In the porous version the distance is taken in \(G\) without deleting other sources. A set dominates in the respective sense when each unselected vertex has weight at least \(1\). Selected vertices automatically qualify. The replacement graph is defined only on all *minimum* sets and imposes feasibility at endpoints; it does not require feasible intermediate smaller exchanges.

## Proof
**Incidence geometry and distance weights.** Every vertex has distance spheres of sizes \(3,6,12,8\) at distances \(1,2,3,4\). Two points are at distance \(2\) precisely when their duads are disjoint, and otherwise are at distance \(4\); two lines are at distance \(2\) precisely when they intersect, and otherwise at distance \(4\). A point and line are at distance \(1\) if incident and \(3\) otherwise. If a selected set has \(a\) points and \(b\) lines, with \(a+b=4\), the eightfold porous weight at an unselected point \(x\) is
\[
  a+3c(x)+2b+6i(x),
\]
where \(c(x)\) is the number of selected points collinear with \(x\), and \(i(x)\) is the number of selected lines incident with \(x\). The corresponding formula for an unselected line interchanges points and lines.

**No set of size at most three works, even porously.** It suffices to exclude size three, because adding sources cannot decrease porous weights on unselected vertices. If all three sources are points, at least six of the fifteen lines miss them, and each missed line receives only \(3/4\); the all-line case is dual. For two selected points and one selected line, among the eight lines disjoint from that selected line at least two miss both selected points (each selected point lies on just three lines). Such a line has porous weight \(1/4+1/4+1/8=5/8\). The case of one point and two lines is dual. Therefore both minima are at least four.

**The side profiles at size four.** Suppose first that there are one point and three selected lines. Eight of the fifteen points are noncollinear with the chosen point. By the projection axiom, each chosen line covers at most two of these eight, hence one remains uncovered. Its porous weight is \(1/8+3/4=7/8\). The three-point/one-line case is dual.

For four selected points, each of the eleven unselected points would have to be collinear with at least two selected points, as one contribution of \(1/2\) plus three of \(1/8\) totals only \(7/8\). Let \(e\) denote the number of disjoint pairs among the four selected duads. Counting point–point collinearity incidences from the selected family to its complement gives \(24-2e\ge22\), so \(e\le1\). If \(e=0\), four pairwise intersecting duads form a four-subset of a five-duad star; the omitted fifth star duad has no selected collinear neighbor. If \(e=1\), relabel the selected duads as either \(\{01,34,13,14\}\) or \(\{01,34,13,23\}\). The outside duad \(15\) in the first case and \(35\) in the second has only one selected collinear neighbor. Both contradict the required two. By the self-duality of \(\operatorname{GQ}(2,2)\), four selected lines also fail. Thus any four-source optimum has exactly two points and two lines.

**Forcing the flag geometry.** Let the selected points be \(p,q\). There are four other points noncollinear with both, and each must belong to a selected line: without incidence its four-source porous weight is at most \(1/8+1/8+1/4+1/4=3/4\). Under label permutations there are two cases. If \(p=01,q=02\), the four uncovered duads are \(03,04,05,12\); each syntheme containing two of these contains \(12\), so two synthemes cannot cover all four. If \(p=01,q=23\), the uncovered duads are \(02,03,12,13\), and exactly two synthemes contain two of these each: \((02|13|45)\) and \((03|12|45)\). They are forced. More invariantly, \(p,q\) are the two points of a line \(L\) different from a marked third point \(r\), while the selected lines are the two lines through \(r\) different from \(L\). There are \(15\cdot3=45\) such flags, with no duplicates.

**Sufficiency for blocked exponential domination.** By permutations of the six labels all \(45\) flags are equivalent. For the representative set consisting of points \(01,23\) and lines \((02|13|45),(03|12|45)\), exact shortest paths avoiding the other selected vertices give the following weight multiset on the \(26\) unselected vertices:
\[
 \{\underbrace{9/8,\ldots,9/8}_{16},\underbrace{21/16,\ldots,21/16}_{8},3,3\}.
\]
Every weight exceeds one, so all forty-five flags are exponential dominating. The preceding porous necessity proves there are no other size-four exponential or porous solutions, and the minimum is exactly four in both models.

**Replacement graph.** Enumerate the forty-five flags using the point–line incidence formula above. Comparing their four-element selected sets gives exactly \(540\) unordered disjoint pairs and \(450\) pairs sharing one selected vertex; no pair shares two or three. Every flag has exactly twenty one-intersection neighbors. The complete forty-five-by-forty-five exact adjacency calculation further shows that each vertex has precisely twenty neighbors at distance one and twenty-four other vertices at distance two. Hence the three-replacement graph is connected, regular of degree twenty, self-centered, and has diameter two. The standalone checks reproduce all \(990\) pair comparisons and all \(45\) breadth-first traversals.

## Verification
`verify_duads.py` constructs the graph directly from six-element duads and synthemes, enumerates every source set through size four, compares the \(45\) porous minima to the \(45\) flag sets, and computes *blocking-aware* rational weights. It also derives the intersection-pair histogram and verifies all graph distances. `verify_symplectic.py` independently constructs the generalized quadrangle from isotropic two-dimensional subspaces of \(\mathbb F_2^4\), uses a different bitmask shortest-path checker, and reproduces the same optimum and swap-graph invariants. Both scripts use only Python's standard library and can be run by `python verify_duads.py` and `python verify_symplectic.py`. Their exact outputs are stored with the scripts.

## Relationship to prior work
The original exponential-domination concept and the distinction between blocked and porous weights come from Dankelmann et al. (2009). Bessy, Ochem and Rautenbach's publicly dated 2015 preprint examines exponential domination in subcubic graphs and gives general bounds and complexity results. These do not classify minimum sources in the thirty-vertex girth-eight cage. Héger and Hernandez Lucas (2020) establish ordinary domination number \(9\) for this generalized quadrangle; ordinary domination is a different condition from the exponentially discounted one, and its minimum configurations do not determine the forty-five exponential optima or their reconfiguration distances. The flag–source correspondence and three-replacement geometry are the contribution considered here.

## Limitations
All exact classifications and distances concern this one thirty-vertex graph; no statement about larger generalized quadrangles, other cages, or other attenuation bases is implied. Novelty searches cannot exclude unpublished, unindexed or inaccessible equivalent computations, including historical material on the original exponential-domination definition. The finite graph-distance checks are exhaustive for the stated \(45\) states and are not extrapolated to infinite families.

## References
- P. Dankelmann, D. Day, D. Erwin, S. Mukwembi and H. Swart, *Domination with exponential decay*, Discrete Mathematics 309 (2009), 5877–5883, DOI:10.1016/j.disc.2008.06.040.
- S. Bessy, P. Ochem and D. Rautenbach, *Exponential Domination in Subcubic Graphs*, arXiv:1511.01398v1 (first posted 2015-11-04); Electronic Journal of Combinatorics 23(4) (2016), #P4.42.
- T. Héger and L. Hernandez Lucas, *Dominating sets in finite generalized quadrangles*, Ars Mathematica Contemporanea 19 (2020), 61–76, DOI:10.26493/1855-3974.2106.423.
- H. S. M. Coxeter, classical duad–syntheme construction of the Tutte–Coxeter graph (1958); the thirty-vertex graph is the Levi graph of \(\operatorname{GQ}(2,2)\).
