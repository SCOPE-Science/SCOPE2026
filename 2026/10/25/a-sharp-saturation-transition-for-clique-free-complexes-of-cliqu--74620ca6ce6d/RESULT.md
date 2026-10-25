# A sharp saturation transition for clique-free complexes of clique bouquets

## Finding
Fix an integer \(t\geq 3\) and nonnegative integers \(q_1,\ldots,q_t\). Start with a central clique \(C=\{c_1,\ldots,c_t\}\cong K_t\). At \(c_i\), attach \(q_i\) further copies of \(K_t\), each sharing exactly \(c_i\) with the central clique and having \(t-1\) new private vertices. Different attached cliques have disjoint private vertex sets, and there are no other edges. Denote the resulting block graph by \(G(t;q_1,\ldots,q_t)\) and put \(q=\sum_iq_i\).

Let \(\mathsf{CF}_t(G)\) be the simplicial complex consisting of vertex subsets inducing no \(K_t\). Then for **every** choice of these parameters there is an integral homotopy equivalence
\[
\mathsf{CF}_t(G(t;q_1,\ldots,q_t))\simeq
\begin{cases}
S^{(q+1)(t-2)},&\min_iq_i=0,\\
\mathrm{pt},&\min_iq_i\geq1.
\end{cases}
\]
Thus the addition of the first attached clique at the last previously unoccupied central vertex changes the homotopy type from a sphere to a contractible complex. The result covers arbitrary, unequal numbers of attached cliques at the central vertices.

## Assumptions and scope
All graphs are finite, simple, and undirected. Each attached clique has order **exactly** \(t\), not merely at least \(t\). For the empty collection of attachments, \(q=0\), the complex is the boundary \(\partial\Delta^{t-1}\simeq S^{t-2}\). The statement concerns the homotopy type of the entire abstract complex over the integers, not only reduced homology over a field; there is no uniform bound on \(q\) or \(t\). Graphs with additional edges, larger attached cliques, or additional levels of attachment are not covered.

## Proof
**1. All forbidden sets.** Write \(W_{ij}\) for the \(t-1\) private vertices in the \(j\)-th clique attached at \(c_i\), and \(U_i=\bigsqcup_{j=1}^{q_i}W_{ij}\). Because two distinct clique blocks meet in at most one vertex and have no cross-block edges, the only \(t\)-cliques are the central \(C\) and the sets \(\{c_i\}\cup W_{ij}\). Hence the clique-free complex is precisely the independence complex of this explicit \(t\)-uniform hypergraph.

**2. Ignore the central forbidden clique.** Let \(X\) be the complex defined by forbidding only the attached \(t\)-cliques. On the disjoint vertex blocks \(\{c_i\}\cup U_i\), it factors as \(X=A_1*\cdots*A_t\). If \(q_i=0\), the factor \(A_i\) is a single vertex and hence contractible; for this case set \(B_i=\{\varnothing\}\), the formal \((-1)\)-sphere used as the unit for joins. If \(q_i>0\), put
\[
B_i=\mathop{\ast}_{j=1}^{q_i}\partial\Delta(W_{ij}),\qquad
A_i=\Delta(U_i)\cup\bigl(c_i*B_i\bigr).
\]
The two displayed pieces of \(A_i\) are contractible and meet exactly in \(B_i\). The join of \(q_i\) simplex boundaries is \(B_i\cong S^{q_i(t-2)-1}\); the homotopy pushout therefore gives \(A_i\simeq\Sigma B_i\simeq S^{q_i(t-2)}\). It follows that if every \(q_i>0\),
\[
X\simeq S^{D},\qquad D=q(t-2)+t-1,
\]
whereas if any \(q_i=0\), \(X\) is a cone and hence contractible.

**3. Reintroduce the central forbidden clique.** Let \(K=\mathsf{CF}_t(G)\), let \(L=B_1*\cdots*B_t\), and let \(B=\Delta(C)*L\). Here \(B\) is the closed star of the face \(C\) inside \(X\); removing from \(X\) all faces containing \(C\) yields \(K\). Thus
\[
X=K\cup B,\qquad K\cap B=P:=\partial\Delta(C)*L.
\]
The complex \(B\) is contractible, and \(P\cong S^{E}\) with \(E=(q+1)(t-2)\). This includes \(q=0\), where the empty join \(L=\{\varnothing\}\) and \(P=\partial\Delta(C)\).

**4. The unsaturated case.** If at least one \(q_i=0\), both \(X\) and \(B\) are contractible. The reduced integral Mayer--Vietoris sequence for \(X=K\cup B\) gives an isomorphism \(\widetilde H_\ast(P;\mathbb Z)\to\widetilde H_\ast(K;\mathbb Z)\), induced by inclusion. If \(q=0\), directly \(K=P\). Otherwise \(E\geq2\), and the complexes \(K\) and \(P\) are simply connected by the elementary argument in step 6. The integral homology Whitehead theorem then upgrades the inclusion \(P\hookrightarrow K\) to a homotopy equivalence. This gives \(K\simeq S^E\).

**5. The saturated case and its unit connecting map.** Suppose all \(q_i\geq1\), so \(D=E+1\). Choose for each \(i\) an oriented fundamental cycle \(z_i\) of the simplicial sphere \(B_i\). Because \(\Delta(U_i)\) is contractible, choose a chain \(u_i\) there with \(\partial u_i=z_i\). The cycle \(\gamma_i=c_i*z_i-u_i\), with the standard oriented join signs, generates \(\widetilde H_{q_i(t-2)}(A_i;\mathbb Z)\): this follows from the Mayer--Vietoris boundary isomorphism for \(A_i=\Delta(U_i)\cup(c_i*B_i)\). The oriented join \(\Gamma=\gamma_1*\cdots*\gamma_t\) therefore generates \(\widetilde H_D(X;\mathbb Z)\) by the integral homology join formula. Exactly one expanded term of \(\Gamma\) contains every vertex of \(C\), namely \(C*(z_1*\cdots*z_t)\). All other terms lie in \(K\). Consequently, the connecting map in the Mayer--Vietoris sequence
\[
\widetilde H_D(X;\mathbb Z)\longrightarrow\widetilde H_{D-1}(P;\mathbb Z)
\]
sends \([\Gamma]\) to \(\pm[\partial\Delta(C)*(z_1*\cdots*z_t)]\), a primitive generator of the target. It is therefore multiplication by \(\pm1\). The same sequence now gives \(\widetilde H_\ast(K;\mathbb Z)=0\) in every degree, including degree zero. Step 6 shows \(K\) is simply connected. As a simply connected acyclic finite CW complex, \(K\) is contractible by the Hurewicz and Whitehead theorems.

**6. Fundamental-group check.** If \(t\geq4\), no forbidden clique has at most three vertices, so \(K\) contains the complete two-skeleton of the simplex on its full vertex set; hence it is simply connected. If \(t=3\) and \(q>0\), the one-skeleton of \(K\) is complete. Every triangle in this one-skeleton either is a face or is the boundary of one of the forbidden triangles: the central triangle or a petal triangle. The boundary of the central triangle bounds a cone of three allowed triangles with apex any private vertex. For a forbidden petal triangle, use as cone apex a central vertex with zero petals in the unsaturated case, or a private vertex in a petal at a *different* central vertex in the saturated case. Each proposed cone triangle contains at most two vertices of a forbidden clique, so belongs to \(K\). Every loop in a complete one-skeleton is a product of triangular loops, which proves simple connectivity. This completes the integral homotopy proof.

## Verification
The standalone program `verify_bouquet.py` constructs **all** faces directly from the forbidden \(t\)-cliques for each of 57 parameter tuples with \(t\in\{3,4,5\}\) and total graph order at most 13. It computes boundary ranks over \(\mathbb F_2\) by independent face enumeration and confirms every predicted Betti vector; it separately checks alternating face sums. It processed 130,478 complete faces in total. Run `python3 verify_bouquet.py`; the recorded output is `verification_output.txt`. These finite tests do **not** establish the theorem for unbounded parameters; the integral, infinite-parameter result rests on the argument above.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623v1, February 10, 2026), prove general \((t-2)\)-decomposability/shellability for \(t\)-clique-free complexes of block graphs and study clique attachments and higher clique whiskerings. The constructed graphs are block graphs, but shellability does not itself identify either of the precise homotopy types or the saturation threshold. Their Section 4 attachment results characterize shellability rather than sphere dimensions.

Kim, *Topology of independence complexes and cycle structure of hypergraphs* (arXiv:2408.14321v2), proves an at-most-one total Betti-number theorem for hypergraphs without Berge cycles of length divisible by three and a general suspension reduction. The forbidden-clique hypergraph here is an incidence tree, so those broad restrictions are compatible with this result, but do not state its exact dimension and saturation criterion. The proof above gives a direct integral homotopy classification rather than identifying it from a field Betti bound alone.

## Limitations
The result assumes a single central \(K_t\) and exclusively pendant \(K_t\) blocks attached at its individual vertices. It does not classify arbitrary block graphs, arbitrary clique-whiskered graphs, larger cliques, or hypergraphs with cyclic incidence. The novelty comparison is limited by possible unindexed or inaccessible prior literature; no claim of bibliographic uniqueness or independent certification is made. The numerical tests check mod-two homology in a bounded range and cannot substitute for the integral proof.

## References
1. Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first public version February 10, 2026), https://arxiv.org/html/2602.09623v1.
2. Jinha Kim, *Topology of independence complexes and cycle structure of hypergraphs*, arXiv:2408.14321 (first public version August 26, 2024; later HTML version consulted), https://arxiv.org/html/2408.14321v2.
3. Yuji Muta and Naoki Terai, *On minimal free resolutions of the cover ideals of clique-whiskered graphs*, arXiv:2505.04248 (May 7, 2025), https://arxiv.org/abs/2505.04248. Mentioned solely as related work on clique-whiskered graph ideals, not as evidence of an equivalent topological theorem.
