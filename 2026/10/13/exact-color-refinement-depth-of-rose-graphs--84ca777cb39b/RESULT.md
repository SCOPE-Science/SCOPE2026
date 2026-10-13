# Exact color-refinement depth of rose graphs
## Finding
Let \(t\ge2\), let \(L_1,\ldots,L_t\ge3\), and let \(R(L_1,\ldots,L_t)\) be the rose graph obtained from the cycles \(C_{L_1},\ldots,C_{L_t}\) by identifying one vertex of every cycle to a single central vertex and making no other identifications. Let
\[
\lambda_1<\lambda_2<\cdots<\lambda_s
\]
be the distinct cycle lengths occurring among \(L_1,\ldots,L_t\). Run ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round whose induced vertex partition is already stable.

Then
\[
\operatorname{Stab}(R(L_1,\ldots,L_t))=
\begin{cases}
\left\lfloor \lambda_s/2\right\rfloor,&s=1,\\[1mm]
\max\!\left\{\left\lfloor \lambda_s/2\right\rfloor,\lambda_{s-1}\right\},&s\ge2.
\end{cases}
\]

Equivalently, when at least two distinct petal lengths occur, the only two possible bottlenecks are refinement within the longest cycle and the final separation between the two largest distinct cycle lengths.

Moreover, the stable color partition is exactly the automorphism-orbit partition for every rose graph.

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. A rose graph has \(t\ge2\) cycle petals that share exactly one common central vertex and are otherwise vertex-disjoint. Round \(0\) is the uniform coloring. Each later round replaces a vertex color by its old color together with the multiset of old colors on its neighbors. Stabilization concerns the induced partition, so a change of color names without a further split is irrelevant.

For a vertex on a petal of length \(L\), write \(i\in\{1,\ldots,L-1\}\) for its distance from the center in one cyclic direction; its two distances to the center along that petal are \(i\) and \(L-i\).

## Proof
The center has degree \(2t\), while every other vertex has degree \(2\), so round \(1\) separates the center from all petal vertices.

Fix a petal of length \(L\). For every round \(r\ge1\), an induction along the two directions of the cycle shows that the color of the position \(i\) is determined, among petal vertices, by the unordered clipped-distance pair
\[
\left\{\min\{i,r\},\min\{L-i,r\}\right\}.
\]
The reason is that both directions terminate at the same center color, and every refinement round extends the visible colored path by one edge in each direction. Conversely, equal clipped-distance pairs give isomorphic rooted colored neighborhoods to the required depth, so they receive the same color.

Within a fixed petal length \(L\), the partition induced by these pairs stops splitting in round \(\lfloor L/2\rfloor\). Indeed, by then positions are classified exactly up to the reflection \(i\leftrightarrow L-i\); later rounds can change the numerical clipped pair but cannot split any such reflection class.

Now compare two distinct petal lengths \(L<M\). At round \(L-1\), the vertices one edge from the center on the two petals still have the same clipped pair,
\[
\{1,L-1\}.
\]
At round \(L\), the shorter-petal vertex has the full pair \(\{1,L-1\}\), while the longer-petal vertex has \(\{1,L\}\), so a strict split occurs. No cross-length equality can survive beyond round \(L\): once the shorter petal is fully visible from both directions, its two endpoint distances sum to \(L\), whereas any equal pair coming from the longer petal would have to sum to \(M>L\), unless one entry were still clipped at \(L\), in which case its sum is already greater than \(L\).

Thus a pair of distinct petal lengths \(L<M\) contributes a last cross-petal split exactly in round \(L\). Over all distinct lengths, the latest such split is therefore \(\lambda_{s-1}\), the second-largest distinct length. The longest petal itself may continue refining until \(\lfloor\lambda_s/2\rfloor\). Taking the maximum gives the stated formula; if there is only one distinct length, only the within-petal term remains.

For the orbit statement, automorphisms may permute petals of the same length and independently reflect each such cycle through the center. Hence the automorphism orbits are the center together with, for each length \(L\) and each \(1\le d\le\lfloor L/2\rfloor\), all vertices on \(L\)-petals whose nearer cyclic distance to the center is \(d\). The stable clipped-distance description gives exactly these classes, so the stable partition equals the orbit partition.

## Verification
The accompanying standalone program `verify.py` constructs rose graphs directly and implements ordinary color refinement without graph-library dependencies. It checks every nondecreasing petal-length tuple with two through five petals and lengths from \(3\) through \(12\). For each case it verifies both the exact depth formula and equality of the stable partition with the explicit orbit partition.

It returns:

`VERIFY_OK depth_checks=2992 orbit_checks=2992 petals=2..5 lengths=3..12`

The computation is a finite consistency check only. The all-parameter result rests on the proof above.

## Relationship to prior work
He and van Dam define a \(k\)-rose graph as \(k\) cycles meeting in one central vertex and study the full arbitrary-\(k\) family through spectral invariants. Their preprint was first posted in July 2016. That source establishes the standard object and its structural importance but does not discuss color refinement or Weisfeiler--Leman iteration depth.

Krebs and Verbitsky formalize the stabilization parameter for color refinement and its relation to truncated universal covers. Their general framework explains the local propagation used here, but it does not state a rose-graph depth formula.

The two-petal case is the infinity-graph subfamily. A prior calculation for that subfamily gives the corresponding two-length formula. The present result treats arbitrary numbers of petals and arbitrary multiplicities simultaneously; the interaction of all cross-petal collisions collapses to the second-largest distinct cycle length, while the longest petal supplies the independent internal-refinement term.

Targeted searches for rose graphs together with color refinement, \(1\)-WL, Weisfeiler--Leman stabilization depth, equitable partitions, refinability, and orbit partitions did not locate an equivalent all-rose formula.

## Limitations
The theorem concerns ordinary one-dimensional color refinement from the uniform coloring on simple rose graphs. It does not cover general cactus graphs, roses with trees attached, higher-dimensional Weisfeiler--Leman refinement, or graph-pair distinguishing depth. The orbit statement may also be obtainable as a special case of broader structural characterizations of refinable graphs; the originality claim here is centered on the exact stabilization-depth formula. The literature search was targeted rather than exhaustive.

## References
1. C. He and E. R. van Dam, *Laplacian spectral characterization of roses*, arXiv:1607.05466, first posted 19 July 2016.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
3. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015.
