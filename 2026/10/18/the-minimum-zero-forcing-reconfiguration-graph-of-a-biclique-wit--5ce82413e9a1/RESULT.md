# The minimum zero-forcing reconfiguration graph of a biclique with two matching edges deleted

## Finding
For integers \(a,b\ge3\), form the simple graph \(G_{a,b}=K_{a,b}-\{u_1v_1,u_2v_2\}\), with bipartition \(U=\{u_1,\ldots,u_a\}\) and \(V=\{v_1,\ldots,v_b\}\). Let \(\mathcal R_{a,b}\) have the minimum *ordinary* zero-forcing vertex sets as vertices, two adjacent exactly when one selected vertex is exchanged for an unselected vertex. Its graph is two copies of
\[
H_{a,b}=(K_{a-1}\square K_{b-1})-\{(0,0)\},
\]
with the two copies joined by exactly one cross edge for each boundary coordinate \((u,0)\), \(u\in\{3,\ldots,a\}\), and \((0,v)\), \(v\in\{3,\ldots,b\}\). The bridging edges are pairwise disjoint. There are no other cross edges. Consequently,
\[
|V(\mathcal R_{a,b})|=2(ab-a-b),\qquad |E(\mathcal R_{a,b})|=(ab-a-b)(a+b-4).
\]
The reconfiguration graph is connected, every vertex has degree \(a+b-4\), and
\[
\operatorname{diam}(\mathcal R_{a,b})=\begin{cases}3,&\min\{a,b\}=3,\\4,&a,b\ge4.\end{cases}
\]
The known size and enumeration of minimum zero-forcing sets are used as inputs, not claimed as new discoveries.

## Assumptions and scope
Graphs are finite, simple, and undirected. In ordinary zero forcing, initially blue vertices may successively force their unique white neighbors to blue. A blue starting set is *zero forcing* if a sequence of legal forces blues the entire graph. A *minimum* set has smallest possible cardinality. One token jump replaces exactly one blue starting vertex with one formerly white starting vertex, keeping the set minimum zero forcing. The theorem holds for every pair of integers \(a,b\ge3\) with two *independent* deleted cross edges, including \(a=3\) or \(b=3\). Coordinates labelled \(0\) are formal extra coordinate labels, never vertices of the original graph.

## Proof
Write \(T=\{1,2\}\). For a blue starting set \(S\), let its white complement be \(W=(\{u_i:i\in A\})\cup(\{v_j:j\in B\})\). A vertex in either part has at most one non-neighbor in the opposite part. If at least three vertices of a part are initially white, every opposing vertex sees at least two of these white vertices, so none of the three can ever become blue. Thus a zero-forcing set has at most two white vertices in each part. If exactly two white vertices lie in one part, they must include a special index in \(T\); otherwise no opposite vertex can force either one.

For four whites, necessarily \(|A|=|B|=2\), \(A\cap T\ne\varnothing\), and \(B\cap T\ne\varnothing\). An initial force requires one special index appearing in exactly one of the two white parts: a blue vertex opposite a white pair can have exactly one white neighbor precisely when its deleted-neighbor index belongs to that white pair but is itself blue. This says \(A\cap T\ne B\cap T\). Conversely, when the signatures differ, the possibilities, up to swapping the special indices and/or the two sides, are \(A=\{1,u\},B=\{2,v\}\), \(A=T,B=\{2,v\}\), and \(A=\{1,u\},B=T\), where \(u\ge3\) and \(v\ge3\). In the first case the blue vertex \(v_1\) forces \(u_u\), then blue \(u_2\) forces \(v_v\); in the second, \(v_1\) forces \(u_2\), then this newly blue \(u_2\) forces \(v_v\); in the third, \(u_2\) forces \(v_1\), then this newly blue \(v_1\) forces \(u_u\). There remains only one white on each side. Because \(a,b\ge3\), among the blue vertices in each opposite part there is one that is adjacent to the lone remaining white, so both finish forcing. Hence the criterion is also sufficient. The first paragraph bounds all forcing sets by four whites; these constructions achieve four, so the minimum blue set has size \(a+b-4\).

There are exactly six types of four-white complements, split into two families. Family \(P\) consists of
\[
(A,B)=(\{1,u\},\{2,v\}),\quad (T,\{2,v\}),\quad(\{1,u\},T),
\]
and family \(Q\) is obtained by interchanging the special labels \(1\) and \(2\) in both parts. In family \(P\), encode the left white pair \(\{1,u\}\) by coordinate \(u\ge3\), and the left white pair \(T\) by \(0\); encode the right white pair \(\{2,v\}\) by \(v\ge3\), and the right pair \(T\) by \(0\). All pairs of these coordinates occur except \((0,0)\). Use the analogous coordinates in family \(Q\). Since the blue complements all have the same cardinality, two solutions are adjacent precisely when their white pairs change in exactly one original vertex. Within either family, replacing a single member of \(A\) changes the left coordinate without changing the right, and replacing a member of \(B\) changes the right coordinate without changing the left. Thus each family induces \((K_{a-1}\square K_{b-1})-\{(0,0)\}\).

Across the two families, one can change only one white vertex precisely if the unchanged side has the same white pair in both families. The only such pair is \(T\). The other side may then replace special index \(1\) by \(2\), fixing its non-special index. Thus the entire cross-edge set consists of \(P(u,0)Q(u,0)\) for \(u=3,\ldots,a\) and \(P(0,v)Q(0,v)\) for \(v=3,\ldots,b\). These \(a+b-4\) bridge edges form a matching.

Each punctured rook graph has \((a-1)(b-1)-1=ab-a-b\) vertices. A full rook graph has degree \(a+b-4\); puncturing \((0,0)\) reduces the degree by one exactly on the boundary points \((u,0)\) and \((0,v)\). The unique cross edge at each boundary point restores that degree. Doubling the vertex count and using the handshake lemma give the asserted size, regularity, and edge count.

For graph distance, a punctured rook graph with at least two row labels and two column labels is connected and has diameter at most two: two distinct row and column coordinates can be linked through either corner, at least one of which is not the deleted \((0,0)\). Every interior point \((u,v)\), \(u,v\ne0\), is adjacent to a boundary point \((u,0)\), so every point is at distance at most one from a bridge endpoint. For arbitrary points in opposite copies, choose a bridge endpoint within one step of the first point; after crossing the bridge, at most two steps inside the other punctured rook graph reach the second point. This gives overall diameter at most four, and connectivity follows.

If both \(a,b\ge4\), select interior vertices \(P(u,v)\) and \(Q(u',v')\) with \(u\ne u'\) and \(v\ne v'\). Every cross-copy path uses at least one bridge. A three-step path would have to spend exactly one step reaching a boundary in each copy and one step crossing the same labelled bridge. The boundary vertices adjacent to the source have labels \((u,0)\) or \((0,v)\), whereas those adjacent to the target have labels \((u',0)\) or \((0,v')\), which do not match. Thus their distance is at least four.

If \(a=3\), there is only one nonzero left coordinate \(u=3\). To connect two points in different copies, if either point lies on the top boundary \((0,v)\), cross its labelled bridge: the other point is at distance at most two within its copy, so the total is at most three. If neither lies on the top boundary, each is \((u,0)\) or \((u,v)\), and both reach the single bridge \((u,0)\) in at most one step. Again the total is at most three. Symmetrically this holds when \(b=3\). Conversely, any two interior points in opposite copies require at least one move to a boundary from each and a bridge move, so their distance is at least three. This proves the diameter formula.

## Verification
The file `verify_two_deleted.py` is a standalone standard-library Python checker. It constructs \(G_{a,b}\) from its adjacency sets and, for each \(3\le a,b\le8\), exhaustively checks every initial blue subset by repeated force closure. It tests the four-white classification, impossibility of five or more white vertices, the exact minimum-set count, all token-jumping adjacency degrees, the edge count, connectivity, and the all-pairs shortest-path diameter. Its recorded output in `verification_output.txt` is:

`VERIFICATION_OK graph_cases=36 zero_forcing_initial_sets=254016 minimum_supports=1386 a,b=3..8`

The checker provides finite corroboration only; the proof above establishes the infinite parameter range.

## Relationship to prior work
Geneson, Haas, and Hogben (2020) introduced token-jumping reconfiguration graphs of minimum zero-forcing sets and proved several connectivity results. Boyer et al. (2018) studied zero-forcing-set enumeration. Bong et al. (2022) studied the distinct token-addition/removal model. Existing exact classifications and polynomial results for matching-deleted complete bipartite graphs already imply the minimum-set cardinality and eligible white complements used here. **Neither those previously known classifications nor the cited general reconfiguration results directly give the two-punctured-rook adjacency structure, cross-bridge geometry, or the precise diameter transition.** This finding claims these additional conclusions, not a new count of minimum sets. Potential unindexed equivalent reconfiguration results cannot be excluded.

## Limitations
The theorem applies only to two *independent* deleted edges of a complete bipartite graph with both parts of size at least three. It does not address three or more deleted edges, token sliding, or reconfiguration of nonminimum zero-forcing sets. Priority is qualified by accessible bibliographic coverage, and no independent scientific validation is claimed.

## References
1. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first public submission 2020-09-01, https://arxiv.org/abs/2009.00220.
2. N. H. Bong, J. Carlson, B. Curtis, R. Haas, L. Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668, https://arxiv.org/abs/2205.09668.
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910, https://arxiv.org/abs/1801.08910.
