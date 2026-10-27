# The diameter-two single-cycle flip graph of perfect matchings in Fisher-transformed prisms

## Finding

Let \(n\ge 3\), let \(P_n=C_n\square K_2\) be the simple \(n\)-gonal prism graph, and let \(F(P_n)\) denote its **triangle (Fisher) expansion**: each vertex is replaced by a triangle whose three vertices are attached to the three original incident edges. Let \(\mathcal R_n\) have the perfect matchings of \(F(P_n)\) as vertices, with two *distinct* matchings adjacent if their symmetric difference consists of exactly one connected alternating cycle. There is no restriction on the length of this cycle.

Write \(\mathcal I_n\subset\mathbb F_2^n\) for the \(n(n-1)\) characteristic vectors of nonempty **proper** circular intervals of the cyclic set \(\{0,1,\ldots,n-1\}\). Let \(H_n=\operatorname{Cay}(\mathbb F_2^n,\mathcal I_n)\). Then, as simple undirected graphs,

\[
\boxed{\mathcal R_n\cong H_n\vee H_n,}
\]

where the join adds every edge between two disjoint copies of \(H_n\). Consequently \(\mathcal R_n\) has \(2^{n+1}\) vertices, is regular of degree \(2^n+n(n-1)\), has \(2^n(2^n+n(n-1))\) edges, and has diameter exactly two. Its distance distribution, from *every* vertex, is

\[
\boxed{\bigl(1,\;2^n+n(n-1),\;2^n-n(n-1)-1\bigr).}
\]

The familiar \(2^{n+1}\) perfect-matching count belongs to the earlier Fisher correspondence; the claimed refinement is the **complete single-alternating-cycle exchange graph**, including the uniform two-flip bound and the exact degree and join decomposition.

## Assumptions and scope

Indices on the two rims are taken modulo \(n\). Denote the vertices of \(P_n\) by \(u_i,v_i\), with rim edges \(u_i u_{i+1}\), \(v_i v_{i+1}\), and rung edges \(u_i v_i\). A *circular interval* is a set of \(\ell\) consecutive indices, for some \(1\le\ell\le n-1\); the full circle is excluded. Each interval is counted as a set, not as an ordered walk. The graph \(H_n\) has vertex set \(\mathbb F_2^n\), with distinct \(x,y\) adjacent exactly when \(x+y\) is a circular-interval characteristic vector. All binary additions below are in \(\mathbb F_2\).

The only flips allowed in \(\mathcal R_n\) reverse the edges on **one** alternating simple cycle. Replacing edges on two disjoint cycles simultaneously does not count as one move.

## Proof

**1. Matching–even-subgraph correspondence.** For a finite cubic graph \(G\), associate to a perfect matching \(M\) of its triangle expansion the subset \(S(M)\subseteq E(G)\) of original edges whose connecting edges in the expansion are **absent** from \(M\). At a replaced vertex, the number of absent connecting edges is either zero or two: if zero, all three external edges are in \(M\); if two, the remaining external edge and the unique internal edge joining the other two triangle vertices are in \(M\). Therefore \(S(M)\) has degree zero or two at every vertex. Conversely any such even edge subset determines exactly one perfect matching by this local rule. This is the Fisher correspondence, previously known and not asserted here as new.

Suppose \(M,N\) correspond to even subgraphs \(S,T\). Their symmetric difference \(M\triangle N\) has, at each base vertex incident to \(S\triangle T\), a single alternating path inside the triangle joining the two affected external sockets; it has no edges in triangles outside \(S\triangle T\). Since the cubic base has degrees zero or two in \(S\triangle T\), that base symmetric difference is a disjoint union of simple cycles. The alternating-cycle components of \(M\triangle N\) project *bijectively* to these simple-cycle components. Thus \(M,N\) are adjacent in \(\mathcal R_n\) if and only if \(S\triangle T\) is a single nonempty simple cycle of \(P_n\).

**2. Explicit cycle-space coordinates.** Every even subgraph \(S\subseteq E(P_n)\) is uniquely encoded by \((a,x)\in\mathbb F_2\times\mathbb F_2^n\) as follows:

\[
1_{v_iv_{i+1}\in S}=x_i,\quad
1_{u_iu_{i+1}\in S}=a+x_i,\quad
1_{u_iv_i\in S}=x_{i-1}+x_i.
\]

Indeed, parity at \(v_i\) forces the rung formula, and parity at \(u_i\) forces \(1_{u_iu_{i+1}\in S}+x_i\) to be independent of \(i\), equal to \(a\). Conversely these equations give even degrees at every vertex. Hence all \(2^{n+1}\) coordinate pairs occur exactly once.

**3. Which coordinate differences are simple cycles?** The difference of the two encodings is obtained by coordinatewise addition, say \((b,y)\).

If \(b=1\), exactly one of the top and bottom horizontal edges at each index \(i\) is selected: the top one for \(y_i=0\), the bottom one for \(y_i=1\). The rung at index \(i\) is selected precisely when this row choice switches between index \(i-1\) and \(i\). Following the successive horizontal edges and the connecting rungs gives a **single simple cycle** winding once around the prism, for *every* one of the \(2^n\) choices of \(y\).

If \(b=0\), both horizontal edges at index \(i\) are selected precisely when \(y_i=1\). Each maximal proper circular run of ones contributes its own simple cycle, using the two corresponding rim paths and the two endpoint rungs. The empty support gives no cycle; the all-ones support gives **two disjoint rim cycles**. The resulting subgraph is a single simple cycle precisely when \(y\) is a nonempty proper circular interval. For \(n\ge3\), there are exactly \(n\) possible starting positions and \(n-1\) permitted lengths, giving \(n(n-1)\) such vectors.

**4. Full graph and metric.** Partition all coordinate pairs into the two classes \(a=0\) and \(a=1\). Step 3 says every pair in opposite classes is adjacent. Inside either class, adjacency is exactly addition by a vector from \(\mathcal I_n\). This gives \(\mathcal R_n\cong H_n\vee H_n\). Each vertex has \(2^n\) neighbors across the classes and \(n(n-1)\) within its class. Consequently the stated degree, edge count, and distance-one count hold. Any two nonadjacent vertices lie in the same class and have a two-edge path through any vertex in the other class. There are genuinely nonadjacent pairs since \(2^n-n(n-1)-1>0\) for all integers \(n\ge3\): it equals one at \(n=3\) and increases thereafter. Hence the diameter is exactly two, with the claimed remaining distance-two count. \(\square\)

## Verification

The standalone programs `verify_cayley.py` and `verify_matchings.py` use only the Python standard library. The first independently enumerates all simple cycles of the base prism, spans its binary cycle space, and checks the degree and two-step covering for \(3\le n\le9\). The second directly enumerates the perfect matchings of the **expanded** graphs, independently tests when their symmetric differences form a single connected alternating cycle, and checks every pair against the predicted join/interval adjacency for \(3\le n\le7\). The recorded standard outputs are included as `verify_cayley.out` and `verify_matchings.out`. Both checks completed and matched the exact formulas. These finite tests support, but do not replace, the preceding all-\(n\) proof.

## Relationship to prior work

Ciucu, Liu and Yang established the Fisher graph matching–even-subgraph bijection and the universal perfect-matching count, including the value used here; their theorem does **not** supply the full single-cycle flip adjacency or diameter of the prism expansion. Grimmett and Li use the triangle Fisher transformation in a different study of self-avoiding walks. Bošković (2026) develops general flip-connectivity and cycle-length bounds for decorated graphs, including clique decorations, but gives no exact prism-family flip-graph join decomposition, degree, or diameter-two formula in the inspected text. The complete exchange graph is the refinement established above.

## Limitations

The statement concerns Fisher expansions of \(C_n\square K_2\), for \(n\ge3\), and allows alternating cycles of *arbitrary* length. It makes no assertion that fixed-length or bounded-short-cycle flips have diameter two, no mixing-time assertion, and no characterization for arbitrary cubic base graphs. Published equivalences using different terminology may remain unindexed. No external independent audit is claimed.

## References

1. M. Ciucu, Y. Liu, C. Yang, “Perfect matchings of Fisher graphs of cubic graphs,” *Kyushu J. Math.* 66 (2012), 291–302. DOI: 10.2206/kyushujm.66.291. See Proposition 5 and Theorem 1. Primary MSC (2010): 82B20, 05A15.
2. G. R. Grimmett and Z. Li, “Self-avoiding walks and the Fisher transformation,” arXiv:1208.5019v1 (first public 2012-08-24), *Electron. J. Combin.* 20 (2013), P47. DOI: 10.37236/2659. Primary subject: combinatorics; source lists MSC 05C30, 82B20.
3. V. Bošković, “Flip dynamics on perfect matchings beyond bipartite and planar graphs,” arXiv:2607.16101 (2026). See Sections 2–3 for the older correspondence and general flip bounds.
