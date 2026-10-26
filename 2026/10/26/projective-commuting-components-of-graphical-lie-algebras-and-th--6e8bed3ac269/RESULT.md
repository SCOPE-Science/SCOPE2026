# Projective commuting components of graphical Lie algebras and the connected-domination enumerator

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite simple graph, with \(n=|V|\ge2\), no isolated vertices, and let \(q\ge2\) be any prime power. Form the two-step nilpotent graphical Lie algebra \(L_G\) over \(\mathbb F_q\) with independent edge-bracket generators as specified below. Let \(\mathcal P_q(G)\) be its **projective commuting graph**, whose vertices are the one-dimensional subspaces of \(L_G/Z(L_G)\), two distinct vertices being adjacent when their representatives bracket to zero.

Let \(H_1,\ldots,H_t\) be the connected components of the complement \(\overline G\), with respective vertex sets \(V_i\), sizes \(m_i\), and induced graphs \(G_i=G[V_i]\). Write \([a]_q=(q^a-1)/(q-1)\). For every \(i\) define the connected-domination enumerator
\[
D_i(q)=\sum_{\substack{\varnothing\ne S\subseteq V_i\\G_i[S]\text{ connected}\\N_{G_i}[S]=V_i}}(q-1)^{|S|-1}.
\]
In particular, \(D_i(q)=1\) when \(m_i=1\). Then:

1. For every \(i\) with \(m_i\ge2\), **one** connected component of \(\mathcal P_q(G)\) contains precisely the projective points supported within \(V_i\) whose supports are *not* connected dominating sets of \(G_i\). This component has exactly \([m_i]_q-D_i(q)\) vertices and diameter at most \(4+\operatorname{diam}(H_i)\).
2. These are **all** the connected components having more than one vertex. All remaining points are isolated. In particular, the number of isolated vertices is exactly
\[
I_q(G)=[n]_q-\sum_{i=1}^t\bigl([m_i]_q-D_i(q)\bigr).
\]
Equivalently, a projective point is isolated if and only if its support is a connected dominating set of \(G\). Every point supported across two or more of the sets \(V_i\) is therefore isolated.

**Tree specialization.** If \(G=T\) is a tree on \(n\ge3\) vertices with \(\ell\) leaves, then
\[
\boxed{I_q(T)=q^{\ell}(q-1)^{n-\ell-1}.}
\]
If \(T\) is not a star, the other \([n]_q-I_q(T)\) projective points form one connected component; if \(T\) is a star, its unique nontrivial component is a clique on \([n-1]_q\) vertices. Thus the isolated-point count determines the number of tree leaves once \(n\) and \(q\) are specified.

## Assumptions and scope

The input graph is finite, undirected, simple, and has no isolated vertices. The field may have any prime-power order, including characteristic two. Put \(W=\mathbb F_q^V\) with canonical basis \((e_v)_{v\in V}\), and put \(Z=\mathbb F_q^E\) with edge basis \((z_{uv})_{\{u,v\}\in E}\), fixing one orientation of every edge. Define \(L_G=W\oplus Z\) with \(Z\) central and \([e_u,e_v]=z_{uv}\) or \(-z_{uv}\) according to that orientation for each edge, and zero for nonedges. This is an alternating class-two Lie bracket even in characteristic two. The no-isolated-vertices assumption implies \(Z(L_G)=Z\), because for a nonzero vertex vector there is an incident edge with a nonzero coefficient in one of its brackets with a vertex basis element. Hence projective points of the central quotient correspond exactly to projective lines \([x]\in\mathbb P(W)\).

For \(x\in W\setminus\{0\}\), its **support** is \(\operatorname{supp}(x)=\{v:x_v\ne0\}\). The closed graph neighborhood \(N_G[S]\) includes \(S\) and every neighbor of a member of \(S\). A nonempty set \(S\) is **connected dominating** if \(G[S]\) is connected and \(N_G[S]=V\). These conventions include single-vertex connected sets; a one-vertex graph has the unique connected dominating set consisting of its vertex. Graph diameter is taken only for components of size at least two.

## Proof

**1. Coordinate centralizers.** For any \(x,y\in W\), linear independence of the central edge generators gives the exact criterion
\[
[x,y]=0\quad\Longleftrightarrow\quad x_u y_v-x_v y_u=0\text{ for every }\{u,v\}\in E.
\]
Fix nonzero \(x\) with support \(S\). If \(v\notin S\) is adjacent to some \(u\in S\), the \(uv\)-equation gives \(y_v=0\). For an edge with both endpoints in \(S\), the equation is equivalent to equality of the ratios \(y_u/x_u=y_v/x_v\). Hence such ratios are constant on each connected component of \(G[S]\). Coordinates outside \(N_G[S]\) are entirely unconstrained. Therefore the vector-space dimension of the commuting centralizer of \(x\) within \(W\) is
\[
\dim_{\mathbb F_q}C_W(x)=c(G[S])+n-|N_G[S]|,
\]
where \(c(G[S])\) denotes the number of connected components of the nonempty induced graph. This number equals one exactly when \(S\) is connected dominating. Because \(\langle x\rangle\subseteq C_W(x)\), the projective point \([x]\) is isolated precisely in that case. Otherwise, a distinct projective line in the commuting centralizer gives at least one neighbor.

**2. Complement blocks prohibit cross-block edges.** Let \(V_1,\ldots,V_t\) be the component sets of \(\overline G\). Every pair of vertices belonging to different \(V_i\) is an edge of \(G\); thus \(G\) is the complete join of the induced graphs \(G_i\). If a support \(S\) meets at least two complement blocks, then \(G[S]\) is connected (every two vertices in one block are joined through a support vertex in another block) and \(S\) dominates every vertex of \(G\) (each vertex is adjacent to a supported vertex in a different block, unless it is itself supported). By step 1, such a projective point is isolated.

Suppose \(x\) is supported in exactly one block \(V_i\). If \(y\) has a nonzero coordinate outside \(V_i\), then any supported coordinate of \(x\) gives, on the corresponding cross-block edge, a nonzero coefficient in \([x,y]\). Hence \([x,y]\ne0\). Therefore no commuting edge can connect two different support blocks, and no commuting edge can leave the points supported entirely in a fixed \(V_i\).

**3. Connectivity within each nonsingleton block.** Fix \(i\) with \(m_i\ge2\). By definition, \(H_i=\overline G[V_i]\) is connected. Its edges are exactly the pairs of basis points \([e_u],[e_v]\) which commute. All these basis points are nonisolated (each vertex has a neighbor in the connected graph \(H_i\)) and they form a connected subgraph isomorphic to \(H_i\).

Let \([x]\) be any other nonisolated projective point supported in \(V_i\), with support \(S\). By step 1, either \(G_i[S]\) is connected but \(S\) does not dominate \(V_i\), or \(G_i[S]\) is disconnected. In the first case, choose \(v\in V_i\setminus N_{G_i}[S]\). Then \([x]\) commutes with the basis point \([e_v]\).

In the second case, let \(T\) be the vertex set of a connected component of \(G_i[S]\), and let \(x_T\) be obtained by restricting \(x\) to \(T\). There are no edges of \(G_i\) between \(T\) and \(S\setminus T\), so the coordinate criterion gives \([x,x_T]=0\). The connected set \(T\) cannot dominate \(V_i\): a vertex of \(S\setminus T\) lies outside its closed neighborhood. Thus some \(v\in V_i\setminus N_{G_i}[T]\) exists, and \([x_T]\) commutes with \([e_v]\). In either case, \([x]\) is within graph distance at most two of a basis point in its block. Consequently all nonisolated points supported in \(V_i\) lie in one connected component, and any two are at distance at most \(2+\operatorname{diam}(H_i)+2\).

If \(m_i=1\), its sole supported projective point is isolated: the singleton set is connected dominating in \(G_i\), and all its other graph-neighbors are in cross-block joins. Steps 2–3 prove the complete component classification.

**4. Exact component sizes.** The number of one-dimensional subspaces of \(\mathbb F_q^{V_i}\) is \([m_i]_q\). For each nonempty support \(S\subseteq V_i\) of size \(s\), there are precisely \((q-1)^s/(q-1)=(q-1)^{s-1}\) projective points with this support. By step 1, exactly \(D_i(q)\) of the points supported in the block are isolated. This proves its claimed nontrivial component size. There are \([n]_q\) projective points in all, and disjointness of the nontrivial components gives the displayed formula for \(I_q(G)\).

**5. The tree calculation.** Let \(T\) be a tree on at least three vertices, and let \(J\) be its set of nonleaves. The induced graph \(T[J]\) is connected and nonempty. Any connected dominating vertex set must contain every vertex of \(J\): deleting a nonleaf vertex separates the tree into at least two branches, and a connected set omitting it can intersect at most one branch and therefore cannot dominate the other. Conversely, every set containing \(J\) is connected dominating, since any additional vertices are leaves adjacent to \(J\). Hence the connected dominating sets are precisely \(J\cup A\), \(A\subseteq V(T)\setminus J\). By counting exact supports,
\[
I_q(T)=\sum_{A\subseteq V(T)\setminus J}(q-1)^{|J|+|A|-1}
=(q-1)^{n-\ell-1}q^\ell.
\]
If \(\overline T\) is disconnected, then \(T\) is a complete join across its complement blocks; acyclicity forces one block of size \(n-1\) and one singleton block, so \(T\) is a star. Conversely the complement of a star has precisely those two blocks. For a nonstar tree, the complement is connected, and the already proved component theorem provides exactly one nontrivial component. For a star, every projective point supported on its leaves commutes with every other such point, giving a clique of size \([n-1]_q\); all remaining points are isolated. Lastly, for fixed \(n,q\), the count is strictly increasing with \(\ell\), since the ratio between successive leaf counts is \(q/(q-1)>1\), so \(\ell\) is recovered uniquely.

## Verification

Run `python3 verify.py` from this package. The script builds projective points over \(\mathbb F_2\) and \(\mathbb F_3\), computes their edge brackets directly, and determines *actual* commuting-graph connected-component partitions. Separately, it obtains the predicted partition from complement components and connected-dominating supports. The full partitions, isolated-vertex counts, and tree leaf formulas are compared.

The test covers every labeled graph without isolated vertices on \(2,3,4,5\) vertices over both prime fields, all \(1,296\) labeled trees on six vertices over \(\mathbb F_2\), and a systematic sample of six-vertex trees over \(\mathbb F_3\). The recorded run printed `VERIFY_OK 2950 direct bracket component comparisons`. This is finite corroboration only; the proof above establishes the claim for every prime-power field order and graph size.

## Relationship to prior work

The graphical Lie-algebra construction comes from the graph-indexed class-two Lie-algebra literature; the detailed constructions of Godoy Molina and Lagos (2023) provide the immediate input setting. Ha, Quang, Le, and Nguyen (2024) study connectivity and diameter of **elementwise** Lie-algebra commuting graphs \(L\setminus Z(L)\), with general iterative tests and special low-derived-dimension classifications. Here the vertex set is instead the **projective central quotient**, and the conclusion is an explicit graph-by-graph decomposition indexed by the co-components of an arbitrary input graph, together with exact component cardinalities and tree leaf counts.

Sriwongsa (2025) studies the *projective noncommuting graph* over the central quotient, the complement of the present graph. In particular, Sriwongsa's Theorem 2.12 establishes for **any** Lie algebra that a single projective noncommuting-graph vertex dominates precisely when its centralizer is its own line plus the center. Under complementary adjacency this is exactly the general **isolated-projective-commuting-point criterion**; that criterion by itself is therefore **not claimed as new**. The new assertions are the specialized connected-domination enumeration for edge-distinct graph algebras and, more substantially, the exact classification, sizes, and diameter bounds of **all nontrivial connected components** of the complementary projective commuting graph. Chareh Khah Moghaddam, Erfanian, and Shamsaki (2024) likewise study an elementwise noncommuting graph. The isolated-projective-point criterion is already a specialization of the general dominating-vertex theorem just credited and can also be recovered from known support-centralizer rank calculations. The new proof uses that criterion as an input and separately establishes the nonisolated **connectivity components** and their explicit graph-theoretic sizes.

## Limitations

The result assumes independent edge-bracket generators and no isolated vertices in the graph. It is not a claim about Lie algebras with arbitrary dependent edge brackets, weighted central quotients, or graphs with extra central vertex directions. The connected components are classified and bounded in diameter; exact diameters and internal adjacency spectra of the nontrivial components are not determined. The number of isolated projective points recovers the leaf number within the class of trees at known field order and size, not the tree isomorphism type. The finite verifier uses only prime fields of orders two and three. An equivalent formulation may exist under alternative graph-algebra or commutation-geometry terminology; independent publication-priority verification has not been performed.

## References

1. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272v1 (first posted 2023-08-01). https://arxiv.org/abs/2308.00272
2. H. V. Ha, H. D. Quang, V. A. Le, and T. T. M. Nguyen, *Diameter of Commuting Graphs of Lie Algebras*, arXiv:2405.06521v1 (2024-05-10). https://arxiv.org/abs/2405.06521
3. A. Chareh Khah Moghaddam, A. Erfanian, and A. Shamsaki, *On the non-commuting graph associated to a finite-dimensional Lie algebra*, arXiv:2406.15902v1 (2024-06-22). https://arxiv.org/abs/2406.15902
4. S. Sriwongsa, *Non-commuting graphs of projective spaces over central quotients of Lie algebras*, arXiv:2505.00726v1 (2025-04-27). https://arxiv.org/abs/2505.00726
