# Correct injective edge chromatic index of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with partite classes \(V_1,\ldots,V_r\), where \(r\ge2\) and \(n_i=|V_i|\ge1\). In an injective edge coloring, two edges must receive distinct colors when they are at distance two in the line graph or lie in a common triangle. Define the corresponding conflict graph \(H_{\mathrm{inj}}(G)\) on the edge set of \(G\).

Then
\[
H_{\mathrm{inj}}(G)\cong\bigvee_{1\le i<j\le r}\overline{L(K_{n_i,n_j})}.
\]
Hence
\[
\chi'_{\mathrm{inj}}(G)=\sum_{1\le i<j\le r}\min\{n_i,n_j\}.
\]
If \(n_1\ge\cdots\ge n_r\), this becomes
\[
\chi'_{\mathrm{inj}}(G)=\sum_{j=2}^r (j-1)n_j.
\]

There is also an exact optimizer classification. On each cut \(E(V_i,V_j)\), every minimum coloring partitions the cut into the stars centered on an entire minimum shore. If \(n_i<n_j\), the center shore is forced to be \(V_i\); if \(n_j<n_i\), it is forced to be \(V_j\); if \(n_i=n_j\ge2\), either shore may be chosen. Let
\[
t=\bigl|\{\{i,j\}:i<j,\ n_i=n_j\ge2\}\bigr|,
\qquad
k=\chi'_{\mathrm{inj}}(G).
\]
Then there are exactly \(2^t\) optimal color-class partitions up to renaming colors, and exactly \(2^t k!\) optimal colorings using a fixed labeled palette of size \(k\).

In particular,
\[
\chi'_{\mathrm{inj}}(K_{2,2,2})=6.
\]
This gives a direct counterexample to Proposition 2.7 of Bhanupriya C K, Dominic, and Sunitha (2023), which states the value \(\min\{t_1,\ldots,t_k\}\) for a complete \(k\)-partite graph and therefore gives \(2\) on \(K_{2,2,2}\).

## Assumptions and scope
All graphs are finite and simple. The complete multipartite notation permits singleton partite classes. An injective edge coloring is not required to be a proper edge coloring: the constraint is only that first and third edges in a three-edge path, and any two edges in a triangle, receive different colors. Equivalently, the conflicting pairs are edges at line-graph distance two or edges belonging to a common triangle.

The recent literature anchor is Tian and Wang, arXiv:2610.04891v1, first public on 2026-10-04 UTC. It studies general upper bounds for the same injective chromatic index. The complete-multipartite correction concerns the earlier 2023 Filomat paper cited below. The foundational complete-bipartite value \(\chi'_{\mathrm{inj}}(K_{a,b})=\min\{a,b\}\) is already known and is not claimed as new.

## Proof
Partition \(E(G)\) by unordered pairs of partite classes. Write \(E_{ij}=E(V_i,V_j)\).

First consider two distinct edges \(e,f\in E_{ij}\). If they meet at a vertex, their other endpoints lie in the same partite class, so those endpoints are nonadjacent and the two edges do not lie in a triangle. Because the edges already meet, their line-graph distance is one rather than two. Thus they do not conflict. If they are disjoint, an endpoint of \(e\) in \(V_i\) is adjacent to an endpoint of \(f\) in \(V_j\), so a connecting edge gives a three-edge path with \(e\) and \(f\) as its first and third edges. Thus they conflict. Therefore the conflict graph induced by \(E_{ij}\) is exactly \(\overline{L(K_{n_i,n_j})}\).

Now take edges from two different cuts. If they share a vertex, their other endpoints lie in two different partite classes, hence are adjacent; the two original edges lie in a triangle and conflict. If they are disjoint, choose either endpoint of the second edge. Its partite class cannot equal both partite classes met by the first edge, so it is adjacent to at least one endpoint of the first edge. That connecting edge produces a three-edge path, so the two original edges again conflict. Hence every vertex of one cut-conflict graph is adjacent to every vertex of every other cut-conflict graph. This proves the join decomposition
\[
H_{\mathrm{inj}}(G)\cong\bigvee_{i<j}\overline{L(K_{n_i,n_j})}.
\]

Chromatic number is additive over graph joins. It remains to compute
\[
\chi\!\left(\overline{L(K_{a,b})}\right).
\]
An independent set in \(\overline{L(K_{a,b})}\) is a pairwise-intersecting set of edges of \(K_{a,b}\), hence is contained in one star. Therefore a coloring of this factor is exactly a partition of the edges of \(K_{a,b}\) into stars. Choosing a center for each color gives a vertex cover of \(K_{a,b}\), so at least \(\tau(K_{a,b})=\min\{a,b\}\) colors are needed. Conversely, the stars centered at all vertices on a smaller shore partition all edges and use exactly \(\min\{a,b\}\) colors. Summing over the joined factors gives the formula.

For the optimizer count, a minimum factor coloring has exactly \(\min\{a,b\}\) distinct star centers, and these centers form a minimum vertex cover of \(K_{a,b}\). If \(a<b\), the unique minimum cover is the entire \(a\)-vertex shore; if \(b<a\), the other shore is forced. If \(a=b\ge2\), the only minimum covers are the two shores. For \(a=b=1\), both center descriptions yield the same one-edge color class. Once the center shore is fixed, every edge is forced into the star of its unique chosen endpoint. Different cuts have disjoint palettes because the conflict graph is a join. Therefore the independent choices on equal nontrivial cuts give exactly \(2^t\) unlabeled optimal partitions, and assigning \(k\) distinct color labels bijectively to their \(k\) classes multiplies the count by \(k!\).

## Verification
The standalone file `artifacts/verify.py` reconstructs the injective-conflict relation directly from the definition, without using the theorem as its conflict test. It checks every complete multipartite isomorphism type through order seven by exact chromatic-number search, compares every edge pair with the claimed cut decomposition, and exactly counts optimal unlabeled conflict-graph colorings through order six. It also constructs the theorem's coloring for every multipartite type through order twenty-five. The recorded replay output is:

`ALL CHECKS PASSED; exact_types=37; exact_edges=388; structural_pairs=2375; count_types=23; counted_optimal_partitions=34; constructive_types=9270; constructive_edges=1685858; max_constructive_order=25`

These finite computations are stress tests only. The theorem for arbitrary positive part sizes is established by the analytic proof above.

The smallest correction witness can also be checked without computation. In \(K_{2,2,2}\), the three bipartite cuts each induce a conflict factor \(\overline{L(K_{2,2})}\) of chromatic number two, and palettes from different cuts cannot overlap. Thus the injective chromatic index is \(2+2+2=6\), not \(2\).

## Relationship to prior work
Cardoso, Cerdeira, Cruz, and Dominic introduced the injective edge chromatic index and proved, among other exact values, \(\chi'_{\mathrm{inj}}(K_{a,b})=\min\{a,b\}\). Their structural characterization by induced star forests is compatible with the proof above but does not state the complete-multipartite cut decomposition, the all-parameter sum formula, or the optimizer count.

Bhanupriya C K, Dominic, and Sunitha study graph products and joins. Their Proposition 2.7 explicitly identifies \(K_{t_1,\ldots,t_k}\) as the join of the empty graphs on the partite classes and then states
\[
\chi'_{\mathrm{inj}}(K_{t_1,\ldots,t_k})=\min\{t_1,\ldots,t_k\}.
\]
That statement agrees with the known bipartite endpoint only when \(k=2\), but it fails already for \(K_{2,2,2}\). The present theorem supplies the corrected value and a structural reason for the failure: injective colors cannot be reused across different unordered part-pairs.

Tian and Wang's 2026 preprint proves a general maximum-degree upper bound for injective edge coloring. Its inspected text does not state a complete-multipartite theorem, and the general bound does not determine the exact values or optimal colorings above.

Targeted searches under the exact invariant name, complete multipartite and complete tripartite aliases, the 2023 proposition number, the sum-of-minima formula, induced-star-arboricity terminology, and the conflict-graph decomposition found no later correction or stronger exact theorem covering this statement.

## Limitations
The theorem is restricted to complete multipartite graphs. It does not improve the best general maximum-degree bounds for arbitrary graphs. The optimizer count is for color-class partitions on a fixed labeled graph; the labeled count uses a fixed palette of exactly \(k\) colors. Search-based literature review cannot exclude an unindexed correction or equivalent result under substantially different terminology.

The computational verifier checks only finite orders and is not used as an infinite proof. The correction of Proposition 2.7 rests on the displayed definition and proposition in the 2023 paper together with the analytic conflict argument, not on numerical experimentation.

## References
1. L. Tian and R. Wang, “A note on the injective edge coloring of graphs with bounded maximum degree,” arXiv:2610.04891v1, first submitted 2026-10-04 UTC.
2. Bhanupriya C K, C. Dominic, and M. S. Sunitha, “Injective edge coloring of product graphs and some complexity results,” Filomat 37(12) (2023), 3963--3983, DOI 10.2298/FIL2312963K.
3. D. M. Cardoso, J. O. Cerdeira, J. P. Cruz, and C. Dominic, “Injective Edge Chromatic Index of a Graph,” arXiv:1510.02626v1 (2015).
