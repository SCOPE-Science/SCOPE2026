# Geometric deletion criterion for shattering by noncrossing partitions

## Finding

Let \(n\ge1\). Put \(n\) distinctly labeled vertices in convex position, in cyclic order. A concept is an ordinary noncrossing partition \(\pi\) of the vertices, and the Boolean query \(\{u,v\}\) returns one exactly when \(u\) and \(v\) are in the same block of \(\pi\). For a finite support of pair queries \(S\), draw its straight-line chord graph. Regard all geometric intersections of chords, including those interior to the polygon, as junctions. For each \(e=\{u,v\}\in S\), delete \(e\) and test whether \(u\) and \(v\) lie in distinct geometric connected components.

**Theorem (all-size geometric deletion criterion).** The support \(S\) is VC-shattered if and only if all of its chords pass this deletion test. In particular the support-shattering decision problem has a polynomial-time geometric graph algorithm, rather than requiring enumeration of Catalan-many partitions.

The resulting numerical and structural consequences are
\[
\operatorname{VCdim}(\mathcal N_n)=\operatorname{Ldim}(\mathcal N_n)=n-1,
\]
with the empty-query convention giving zero when \(n=1\). The maximum shattered supports (those with \(n-1\) queries) are precisely the noncrossing spanning trees of the labeled convex polygon; their number is the previously known noncrossing-tree sequence
\[
\frac{1}{2n-1}\binom{3n-3}{n-1}\quad(n\ge2).
\]
For \(n\ge3\), the **exact three-query layer** has cardinality
\[
\binom{\binom n2}{3}-\binom n3-4\binom n4.
\]

The complete support counts by query-set cardinality, obtained by exhaustive verification, are

| Vertex count | Shattered supports at query-set sizes zero through \(n-1\) |
| --- | --- |
| \(4\) | \((1,6,15,12)\) |
| \(5\) | \((1,10,45,90,55)\) |
| \(6\) | \((1,15,105,375,588,273)\) |
| \(7\) | \((1,21,210,1155,3276,3990,1428)\) |
| \(8\) | \((1,28,378,2940,12929,28980,27492,7752)\) |

## Assumptions and scope

The vertices are distinct and in strictly convex cyclic position; a chord joins two distinct labeled vertices. A noncrossing partition means that the convex hulls of distinct blocks are disjoint, or equivalently that there are no alternating four cyclic vertices \(a,b,c,d\) with \(a,c\) in one block and \(b,d\) in another. There is no restriction on the number or sizes of blocks. A support \(S\) is shattered if all \(2^{|S|}\) Boolean labelings of its queries are restrictions of some concept in \(\mathcal N_n\). A pair of chords crossing at their interiors is treated as meeting in the *geometric* union, even though it is not a graph vertex of the original support. Isolated labeled vertices are singleton geometric components.

## Proof

**Lemma 1 (minimal noncrossing closure of positive equalities).** For any chord set \(T\), form the planar union \(G_T\) of its closed chord segments and isolated labeled vertices. Let \(P_T\) group the labeled vertices by connected components of \(G_T\). Then \(P_T\) is the unique finest noncrossing partition in which the endpoints of each chord of \(T\) belong to the same block.

*Proof.* The ordinary endpoint-connected components force equalities along shared vertices. Moreover, if two chords cross in their interiors, then any noncrossing partition identifying the endpoints of both chords must also identify their two blocks: otherwise its two distinct blocks contain alternating endpoints. Thus every noncrossing partition satisfying the equalities is constant on every geometric component of \(G_T\); this remains true along a chain of crossings or common endpoints. Conversely, different geometric components cannot contain alternating pairs of labeled vertices: if one contained \(a,c\) and another contained \(b,d\) in alternating boundary order, simple polygonal paths within those disjoint geometric components joining each pair would have to cross inside the disk, by planar separation. Therefore \(P_T\) is noncrossing. It satisfies the prescribed equalities, hence is the finest such partition. \(\square\)

**Lemma 2 (Boolean realization).** Fix a support \(S\) and a selection \(T\subseteq S\) of queries assigned one; the remaining queries in \(S\setminus T\) are assigned zero. This labeling is realized exactly when, for every \(e=\{u,v\}\in S\setminus T\), the endpoints \(u,v\) lie in different connected components of \(G_T\).

*Proof.* Lemma 1 forces every partition realizing the positive answers to coarsen \(P_T\). A negative query whose endpoints already share a \(P_T\) block is impossible. If no negative query does, the partition \(P_T\) itself realizes all the answers. \(\square\)

**Deletion criterion.** Necessity follows from Lemma 2 by assigning all edges of \(S\setminus\{e\}\) one and the chosen edge \(e\) zero. For sufficiency, consider any set \(T\) of positive edges and any negative edge \(e\). The geometric union \(G_T\) is a subspace of \(G_{S\setminus\{e\}}\). If the endpoints of \(e\) are disconnected in the latter, they are disconnected in the former. Lemma 2 realizes every labeling. \(\square\)

**Algorithmic bound.** Represent each selected chord by a node, join nodes if their chords share a labeled endpoint or their interiors cross, and include incidences from labeled vertices to their chords. For each query \(e\), remove its chord-node and run breadth-first search for a path from its first endpoint to its second in the remaining incidence/intersection graph. All pairwise crossings are identified by cyclic inequalities, so a simple implementation takes polynomial time in \(n\) and \(|S|\). This is the geometric connected-component test, not the ordinary graph-forest test.

**VC dimension and extremal supports.** If \(S\) contains an ordinary graph cycle, deleting any cycle edge leaves its endpoints joined by the other cycle edges; thus \(S\) cannot be shattered. Hence every shattered support is an ordinary forest and has at most \(n-1\) edges. A boundary path on the cyclic vertices is noncrossing and its graph is a tree. Deleting any edge disconnects its endpoints geometrically, so the path is shattered. Hence the VC dimension equals \(n-1\). If a shattered set has size \(n-1\), its ordinary graph is a spanning tree. Suppose two of its chords cross. Those are disjoint tree edges; some third tree edge \(e\) lies on the unique tree path joining these two edges. Deleting \(e\) places the crossing pair in opposite ordinary components, but the geometric intersection reconnects them, in turn reconnecting the endpoints of \(e\). This contradicts the deletion criterion. Therefore the tree is noncrossing. The converse is immediate: a noncrossing tree has no interior intersections, and every tree edge is a bridge. The displayed extremal count is the established enumerator for noncrossing spanning trees, not a new enumeration formula.

**Littlestone dimension.** VC shattering of \(n-1\) queries gives a complete adaptive tree of depth \(n-1\). Conversely, consider *any* family of equivalence relations on \(n\) labeled elements, queried by pair equality. An informative first equality query \(\{u,v\}\) has a positive-answer subfamily in which \(u,v\) are identified. Its remaining answers are determined by an equivalence relation on at most \(n-1\) quotient elements; queries involving \(u\) and \(v\) become equivalent, and the particular equality query becomes constant. By induction, that branch has Littlestone dimension at most \(n-2\), regardless of its additional restrictions. A complete depth-\(n\) decision tree would require both branches of the first query to have depth at least \(n-1\), a contradiction. The base case \(n=1\) has no informative pair query. Thus \(\operatorname{Ldim}\le n-1\), with equality for \(\mathcal N_n\).

**Three-query layer.** For three distinct chords the deletion test can fail in exactly two ways. The first is an ordinary triangle, of which there are \(\binom n3\). The second is a pair of interior-crossing chords on four different endpoints, plus a third chord joining one endpoint of each crossing chord (one of the four sides of their convex quadrilateral). For each four-tuple there are four such triples. These families are disjoint and each failing three-query support has a unique obstructing pattern: after deleting one edge there are only two remaining chords, whose topological connections arise either through their shared labeled endpoint or through their interior crossing. Counting all three-edge subsets and subtracting the two forbidden types gives the formula.

**A genuinely four-edge obstruction.** On cyclic points \(0,1,2,3,4\), the set of edges \(\{01,03,12,24\}\) fails the deletion test for \(01\): after its removal, chords \(03\) and \(24\) cross, while \(12\) connects vertex \(1\) to the chord \(24\). Every three-edge subfamily passes. Thus the support complex is not characterized merely by forbidden triangles or the three-edge crossed-fork patterns. It is not, in general, a matroid: on four vertices, the maximal supports \(\{01,02,03\}\) and \(\{01,12,13\}\) are noncrossing spanning trees, but replacing \(03\) in the former with either \(12\) (a triangle) or \(13\) (a crossing with \(02\)) destroys maximal shattering.

## Verification

Run `python3 verify_geometric.py` to enumerate **all supports of cardinality at most \(n-1\)** for \(n=4,5,6,7,8\) using geometric chord intersections and independent deletion searches. Run `python3 verify_traces.py` for \(n=4,5,6,7\); this algorithm instead constructs all set partitions, filters the noncrossing ones by alternating quadruples and tests all Boolean truth patterns on each support. Run `python3 verify_closure.py` for \(n=4,5,6\); this third implementation repeatedly merges blocks with interlacing labels, then applies the deletion criterion. The scripts assert every displayed count and report success markers. These are finite checks of the stated census and structural mechanisms, not a substitute for the all-size proof above.

## Relationship to prior work

Classical noncrossing partitions and their Catalan enumeration are standard. The noncrossing bond-poset construction and its noncrossing no-broken-circuit complexes studied by Farmer, Hallam and Smyth concern ordinary graph bonds, order structure, Möbius data and crossing-free edges; their noncrossing forest enumerators are **not** the support-complex counts here. A pair of crossing chords already constitutes a shattered two-query support, so the present complex is strictly broader than the usual complex of crossing-free forests. Cohen, Dougherty, Harsh and Martin study noncrossing partition lattices for planar configurations and their rank counts, not the pair-query support-shattering test. Lin and Kim study \(k\)-noncrossing enumeration and provide the dated primary context. The top-dimensional noncrossing-tree count appears in OEIS A001764 and is explicitly credited, rather than claimed as a new sequence. The new claim is the deletion characterization and the resulting complete description of *which* chord sets admit every Boolean restriction, with its three-query layer and verified finite census. No claim of definitive historical priority is made.

## Limitations

The theorem assumes a convex cyclic geometry and **all** noncrossing partitions, not a fixed block count or nonconvex point configuration. The exact support f-vectors listed stop at eight labeled vertices; no general closed form for all intermediate layers is claimed. The exact top layer and the VC/Littlestone dimensions do have all-size proofs. Equivalent formulations in terms of closure lattices, query independence and geometric bond matroids warrant further priority checking. Independent external validation has not been performed.

## References

1. Z. Lin and D. Kim, *A combinatorial bijection on \(k\)-noncrossing partitions*, arXiv:1905.10526v1, first public 2019-05-25, https://arxiv.org/abs/1905.10526.
2. C. M. Farmer, J. Hallam and C. Smyth, *The Noncrossing Bond Poset of a Graph*, arXiv:2012.07212, https://arxiv.org/abs/2012.07212. The earlier Farmer–Hallam conference paper appeared at FPSAC 2019.
3. S. Cohen, M. Dougherty, A. D. Harsh and S. P. Martin, *Noncrossing Partition Lattices from Planar Configurations*, arXiv:2306.08119v1, first public 2023-06-13, https://arxiv.org/abs/2306.08119.
4. OEIS A001764, known enumeration of noncrossing spanning trees, https://oeis.org/A001764.
