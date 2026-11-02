# Minimal connected domination of full edge subdivisions: a tree-cover correspondence and sparse cardinality spectra

## Finding
Let \(G=(V,E)\) be a connected finite simple graph with \(n=|V|\ge3\). Write \(\operatorname{Sub}(G)\) for the graph obtained by replacing each edge \(e=uv\) by \(u-w_e-v\). A connected dominating set is **inclusion-minimal** if no proper subset is both connected and dominating. Let \(\mathcal C_{\operatorname{Sub}(G)}(z)\) enumerate these sets by size.

There is an exact bijection between inclusion-minimal connected dominating sets of \(\operatorname{Sub}(G)\) and triples \((S,T,\phi)\) satisfying all of the following:

1. \(S\subseteq V\) is a nonempty vertex cover, and \(G[S]\) is connected.
2. \(T\) is a spanning tree of \(G[S]\), with the empty-edge tree allowed when \(|S|=1\). Every degree-one vertex of \(T\) has a neighbor in \(V\setminus S\) in the original graph.
3. For each \(x\in V\setminus S\), the map \(\phi\) chooses one neighbor \(\phi(x)\in N_G(x)\cap S\).

The corresponding set is
\[
D(S,T,\phi)=S\cup\{w_e:e\in E(T)\}\cup\{w_{x\phi(x)}:x\in V\setminus S\},
\qquad |D(S,T,\phi)|=n+|S|-1.
\]
Write \(\tau_{\mathrm{ext}}(G,S)\) for the number of spanning trees of \(G[S]\) whose degree-one vertices each have a neighbor outside \(S\), taking \(\tau_{\mathrm{ext}}(G,S)=1\) for a singleton \(S\). Thus the entire cardinality distribution is
\[
\mathcal C_{\operatorname{Sub}(G)}(z)=
\sum_{\substack{\varnothing\ne S\subseteq V:\ S\text{ a vertex cover},\\G[S]\text{ connected}}}
\tau_{\mathrm{ext}}(G,S)
\prod_{x\in V\setminus S}|N_G(x)\cap S|\;z^{n+|S|-1}.
\]

For the complete bipartite graph \(K_{a,b}\), where \(a,b\ge2\), put \(m=\min(a-1,b-1)\) and let \(\left\{\begin{smallmatrix}r\\k\end{smallmatrix}\right\}\) denote a Stirling number of the second kind. Then the labeled inclusion-minimal connected-domination polynomial of its full edge subdivision is
\[
\boxed{\begin{aligned}
\mathcal C_{\operatorname{Sub}(K_{a,b})}(z)
={}&a^{b-1}\sum_{q=1}^{m}
\frac{b!}{(b-q)!}\left\{\begin{smallmatrix}a-1\\q\end{smallmatrix}\right\}
 z^{2a+b+q-1}\\
&+b^{a-1}\sum_{p=1}^{m}
\frac{a!}{(a-p)!}\left\{\begin{smallmatrix}b-1\\p\end{smallmatrix}\right\}
 z^{2b+a+p-1}.
\end{aligned}}
\]
Both summands count disjoint classes, even when their degrees coincide.

In particular, for every integer \(b\ge2\),
\[
\boxed{\mathcal C_{\operatorname{Sub}(K_{2,b})}(z)
=b2^{b-1}z^{b+4}+2bz^{2b+2}.}
\]
For \(b\ge4\), the only attained cardinalities are \(b+4\) and \(2b+2\): the entire interval \(b+5,\ldots,2b+1\), of length \(b-3\), is absent. These graphs are connected, bipartite, and \(2\)-degenerate. A second consequence, for every integer \(n\ge3\), is
\[
\mathcal C_{\operatorname{Sub}(K_n)}(z)
=n(n-1)^{n-2}z^{2n-2}.
\]

## Assumptions and scope
All vertices and edges are labeled, graphs are finite, simple, undirected and connected, and the full subdivision replaces **every** original edge once. The general classification requires at least three original vertices. This excludes \(K_2\), whose subdivided path has the middle subdivision vertex as its sole minimum connected dominating set and for which the singleton-vertex-cover construction is not minimal. The definition of a tree leaf used here is a vertex of tree-degree exactly one, so the one-vertex spanning tree has no leaves. The general theorem includes stars: when \(G=K_{1,n-1}\), the only triple has \(S\) equal to its center and yields the unique minimal connected dominating set of size \(n\). The enumerator counts inclusion-minimal sets, not only minimum-cardinality sets.

## Proof
**Step 1: necessary vertex cover and connectivity.** Let \(D\) be a connected dominating set of \(\operatorname{Sub}(G)\) with \(n\ge3\), and put \(S=D\cap V\). A single subdivision vertex cannot dominate all original vertices, and no other single vertex is universal, so \(|D|\ge2\). If an edge \(uv\) had both endpoints outside \(S\), its subdivision vertex \(w_{uv}\) would either be outside \(D\) and undominated, or be inside \(D\) and isolated in \(\operatorname{Sub}(G)[D]\). Thus \(S\) is a vertex cover. Every selected subdivision vertex has at least one selected original endpoint. Selected subdivision vertices with only one selected endpoint are leaves in the induced graph, and therefore cannot link distinct original vertices. Hence \(S\ne\varnothing\), \(G[S]\) is connected, and the selected subdivision vertices of edges entirely in \(S\) correspond to an edge set \(F\) spanning and connecting \(S\). Every omitted original vertex \(x\) must have at least one selected subdivision vertex on an edge from \(x\) to \(S\).

**Step 2: minimality of the selected subdivision vertices.** If \(F\) contained a cycle, deleting any subdivision vertex corresponding to an edge of that cycle would leave domination and connectivity intact. Hence inclusion-minimality forces \(F\) to be a spanning tree \(T\) of \(G[S]\), or the empty tree when \(|S|=1\). A selected subdivision vertex on an edge from \(x\notin S\) to \(S\) has no selected neighbor except its endpoint in \(S\); removing it cannot disconnect the remaining selection. Thus exactly one such vertex is selected for each \(x\notin S\), otherwise one could be deleted while still dominating \(x\). This uniquely specifies \(\phi\). Conversely, deleting any chosen internal subdivision vertex disconnects the selected original vertices, while deleting a chosen boundary subdivision vertex leaves its omitted original endpoint undominated.

**Step 3: minimality of selected original vertices.** Suppose \(|S|\ge2\). The induced selected subgraph is the one-subdivision of the tree \(T\), with one additional pendant subdivision vertex for each original vertex outside \(S\). Deleting an original vertex \(u\in S\) of tree-degree at least two disconnects this induced tree. If \(u\) is a tree leaf adjacent in \(G\) to some \(x\notin S\), deleting \(u\) either leaves \(w_{ux}\) undominated (when it was not selected) or isolates the selected vertex \(w_{ux}\) (when it was selected). Thus such a leaf is indispensable. On the other hand, if a tree leaf \(u\) has no neighbor outside \(S\), deleting \(u\) preserves connectivity: the selected subdivision vertex on its incident tree edge remains attached to the other endpoint. All original vertices are still dominated, and every omitted subdivision vertex on an edge incident with \(u\) has its other original endpoint in \(S\). Hence \(u\) would be dispensable. This proves the leaf condition. If \(|S|=1\), the vertex cover property and connectivity force \(G\) to be a star; \(n\ge3\) ensures at least two selected pendant subdivision vertices remain if its center is deleted, so the center is also indispensable. All chosen vertices are therefore essential precisely in the stated triples.

**Step 4: exact size and the arbitrary-graph polynomial.** The selected vertices consist of \(|S|\) originals, \(|S|-1\) internal edge-subdivision vertices, and \(n-|S|\) boundary subdivision vertices; thus their total is \(n+|S|-1\). The triple can be recovered uniquely from the selected originals, internal edge-subdivision vertices, and boundary edge-subdivision vertices. Summing over all eligible triples gives the first displayed polynomial.

**Step 5: bipartite specialization.** Write the shores of \(K_{a,b}\) as \(A,B\). A vertex cover includes all of \(A\) or all of \(B\). Consider \(S=A\cup Q\), with \(Q\subsetneq B\), \(|Q|=q\ge1\). Each vertex of \(A\) has a neighbor outside \(S\), but no vertex of \(Q\) does. Therefore \(T\) is a spanning tree of \(K_{a,q}\) with all \(q\) vertices of \(Q\) of tree-degree at least two. The relevant weighted spanning-tree identity is
\[
\sum_{T\text{ spanning tree of }K_{a,q}}
\prod_{u\in A}X_u^{\deg_T(u)-1}
\prod_{v\in Q}Y_v^{\deg_T(v)-1}
=\left(\sum_{u\in A}X_u\right)^{q-1}
 \left(\sum_{v\in Q}Y_v\right)^{a-1}.
\]
For completeness, weight each edge \(uv\) by \(X_uY_v\) and delete a row and column at a vertex \(v_0\in Q\) in the weighted Laplacian. Put \(X=\sum X_u\) and \(Y=\sum Y_v\). Write \(\boldsymbol{x}=(X_u)_{u\in A}\). Eliminating the remaining \(Q\)-rows yields the Schur complement
\(Y\operatorname{diag}(X_u)-\frac{Y-Y_{v_0}}{X}\boldsymbol{x}\boldsymbol{x}^{\mathsf T}\). By the rank-one determinant lemma its determinant is \((\prod X_u)Y^{a-1}Y_{v_0}\). Multiplying by the eliminated diagonal determinants \(X^{q-1}\prod_{v\ne v_0}Y_v\), the weighted matrix-tree theorem gives \((\prod X_u)(\prod Y_v)X^{q-1}Y^{a-1}\); division by the vertex products gives the identity.

The right-hand side encodes a word of length \(q-1\) over \(A\), and a word of length \(a-1\) over \(Q\). Every vertex of \(Q\) must appear at least once in the latter word, so the number of qualifying trees is \(a^{q-1}q!\left\{\begin{smallmatrix}a-1\\q\end{smallmatrix}\right\}\). Choosing \(Q\) contributes \(\binom bq\), and each of the \(b-q\) omitted vertices of \(B\) has \(a\) choices for \(\phi\). The total is consequently \(a^{b-1}\frac{b!}{(b-q)!}\left\{\begin{smallmatrix}a-1\\q\end{smallmatrix}\right\}\), at cardinality \(2a+b+q-1\). The analogous opposite-shore choice gives the second summation. The possibility \(S=V\) is excluded automatically, since every spanning tree on at least two vertices has a leaf with no neighbor outside \(S\). Surjections force \(q\le a-1\), and the proper-shore condition forces \(q\le b-1\), giving precisely the stated range.

**Step 6: gap and complete-graph consequences.** When \(a=2\), both surjection sums have only the index \(1\); their coefficients and exponents give the two-term polynomial. Distinct degrees are \(b+4\) and \(2b+2\), so exactly \(b-3\) intermediate integers are omitted when \(b\ge4\). The full subdivision is bipartite and is \(2\)-degenerate because its subdivision vertices have degree two and any induced subgraph containing none of them is edgeless. For \(G=K_n\), every vertex cover has size at least \(n-1\). The choice \(S=V\) is invalid, so \(S=V\setminus\{x\}\) for exactly one \(x\). All leaves of a spanning tree of \(K_{n-1}\) have a neighbor \(x\) outside \(S\). Cayley's tree count gives \((n-1)^{n-3}\) choices, \(n\) choices for \(x\), and \(n-1\) choices for \(\phi(x)\), giving the last formula.

## Verification
The standalone standard-library program `verify.py` independently reconstructs subdivision graphs, exhaustively tests connected domination and inclusion-minimality on actual vertex subsets, and compares its sets or full cardinality coefficients with the formulas. It checks every connected labeled base graph on three or four vertices, several five- and six-vertex bases, seven complete-bipartite parameter instances, and 144 further arithmetic parameter pairs. The validated run returned:

`VERIFY_OK general_graphs=47 biclique_graphs=7 direct_subsets=1280106 arithmetic_pairs=144`

The checked graph order/edge-subset ranges are finite; they are corroboration rather than an exhaustive certificate for the infinite theorem. Run with `python3 verify.py`. The all-order result follows from the proof above.

## Relationship to prior work
Abu-Khzam, Fernau, Gras, Liedloff and Mann (arXiv:2205.00086, first posted 2022-04-29; ESA 2022) establish algorithms and extremal bounds for enumerating minimal connected dominating sets, including on \(2\)-degenerate graphs. Their accessible full text does not state this full-subdivision tree-cover bijection or the complete bipartite Stirling polynomial. Sayadi (arXiv:1908.02174, 2019) gives algorithms and structural results for convex bipartite graphs, rather than the present exact incidence-family polynomial. Lokshtanov, Pilipczuk and Saurabh (arXiv:1611.00840, 2016) prove general exponential enumeration bounds, not this family-specific characterization.

A preceding calculation for minimal connected domination of the rook graph \(K_a\square K_b\) uses **the same degree-constrained bipartite-tree counts**. That tree kernel is not claimed as new here. The present result instead establishes a uniform correspondence for full edge subdivisions of arbitrary connected base graphs, counts the independent choices of boundary subdivision vertices, and obtains a two-spike cardinality spectrum within connected \(2\)-degenerate bipartite graphs. Ordinary domination and independent domination on full subdivisions are different properties and do not enforce the connected spanning-tree and external-leaf conditions.

## Limitations
No claim is made that the general graph sum is polynomial-time evaluable: its constrained spanning-tree terms may be expensive. For \(n=2\), the general correspondence is not asserted. All parameter counts concern labeled sets. The literature comparison supports provisional originality, not a proof that all earlier or unindexed work has been exhausted. No independent mathematical audit has been performed.

## References
1. F. N. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Connected Dominating Sets*, arXiv:2205.00086 (first posted 2022-04-29); conference version *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI:10.4230/LIPIcs.ESA.2022.1.
2. M. Y. Sayadi, *On the maximum number of minimal connected dominating sets in convex bipartite graphs*, arXiv:1908.02174 (first posted 2019-08-06).
3. D. Lokshtanov, M. Pilipczuk, S. Saurabh, *Below all subsets for Minimal Connected Dominating Set*, arXiv:1611.00840 (first posted 2016-11-02), SIAM J. Discrete Math. 32 (2018), 2332–2345.
4. The weighted matrix-tree theorem, its rank-one determinant calculation for complete bipartite graphs, and Cayley's labeled-tree theorem (classical combinatorial tools; the required specialization is derived above).
