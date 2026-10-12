# Graphic-matroid adjoint spectra and vertex arboricity for radical-square-zero quiver algebras

## Finding

**Theorem.** Fix any prime power \(q\), a finite simple undirected graph \(G=(V,E)\) with \(n=|V|\geq1\) and \(m=|E|\geq0\), and an arbitrary orientation \(Q\) of all its edges. Let \(A_Q=\mathbf F_qQ/J^2\) be the radical-square-zero quotient of its path algebra. For \(a\in A_Q\), let \(\rho(a)=\operatorname{rank}_{\mathbf F_q}(b\mapsto ab-ba)\), and let
\[
\mathcal R_{Q,q}(T)=\sum_{a\in A_Q}T^{\rho(a)}.
\]
Write \(r_G(S)=n-c_G(S)\) for the graphic-matroid rank of the edge subset \(S\subseteq E\), where \(c_G(S)\) counts all components of the spanning subgraph \((V,S)\). A **flat** is an edge set \(Z\) such that every edge outside \(Z\) strictly increases its rank upon addition. For each flat, \(G/Z\) denotes the multigraph obtained by contracting every connected component of \((V,Z)\); flatness guarantees it has no loops, and parallel edges are allowed. Write \(\chi_{G/Z}(q)\) for its number of proper vertex \(q\)-colorings.

Then the entire rank distribution is
\[
\boxed{\mathcal R_{Q,q}(T)=\sum_{Z\text{ flat of }G}\chi_{G/Z}(q)q^{m-|Z|}\sum_{S\subseteq Z}(q-1)^{|S|}T^{m-|Z|+r_G(S)}.} \tag{1}
\]
Moreover, if \(c(G)\) is the number of connected components of \(G\), including isolated vertices, then \(q^{-c(G)}\mathcal R_{Q,q}(T)\) is determined solely by the graphic matroid \(M(G)\), independently of orientation, graph representation of that matroid, or characteristic beyond \(q\).

For a forest \(G\) with \(m\) edges and \(c(G)=n-m\), equation (1) becomes
\[
\boxed{\mathcal R_{Q,q}(T)=q^{c(G)}(1+(q^2-1)T)^m,\qquad
\operatorname{Pr}(A_Q)=\left(\frac{q^2+q-1}{q^3}\right)^m.} \tag{2}
\]
Here \(\operatorname{Pr}(A_Q)\) is the proportion of ordered pairs of elements that commute. For arbitrary \(G\) it is \(q^{-(n+m)}\mathcal R_{Q,q}(q^{-1})\).

Finally, write \(\operatorname{va}(G)\) for the **vertex arboricity**: the minimum number of vertex color classes such that the subgraph induced by every class is a forest. Then
\[
\boxed{\max_{a\in A_Q}\rho(a)=m\quad\Longleftrightarrow\quad\operatorname{va}(G)\leq q.} \tag{3}
\]
Thus the commutator image of some element equals the entire radical exactly when \(q\) colors suffice to partition the vertices into induced forests. For example, over \(\mathbf F_2\), a simple quiver on the underlying graph \(K_5\) has maximum adjoint rank \(9\), although its radical has dimension \(10\).

## Assumptions and scope

Every vertex contributes an idempotent \(e_v\) and every oriented edge one radical arrow \(\alpha_e\). The quotient kills all paths of length two, so its vector-space dimension is \(n+m\). Products of two radical arrows vanish and, for an arrow \(e:u\to v\), \(e_u\alpha_e=\alpha_e=\alpha_e e_v\); all other vertex-arrow products vanish. Arrows are not allowed to be loops, and at most one arrow joins any unordered vertex pair. Directed cycles are allowed because paths of length two are killed.

The theorem uses the *additive commutator* \(ab-ba\), not the dimension of a Lie algebra's Cartan subalgebra or module-theoretic endomorphism rank. All assertions hold over finite fields of arbitrary characteristic, including characteristic two. The underlying graph need not be connected. In the case of no edges, equation (2) gives \(\mathcal R=q^n\) and commuting probability one.

## Proof

1. **Exact commutator matrix.** Write \(a=\sum_{v\in V}d_ve_v+\sum_{e\in E}x_e\alpha_e\) and \(b=\sum_{v\in V}h_ve_v+\sum_{e\in E}y_e\alpha_e\). On each arrow \(e:u\to v\), direct multiplication yields
\[
[ a,b ]_e=(d_u-d_v)y_e-x_e(h_u-h_v). \tag{4}
\]
In particular every commutator belongs to the \(m\)-dimensional radical.

2. **Rank from equal-color edges.** Given the vertex labels \(d\), put \(Z=\{uv\in E:d_u=d_v\}\), and put \(S=\{e\in Z:x_e\neq0\}\). In the arrow coordinates outside \(Z\), the first term of (4) independently spans all \(m-|Z|\) coordinate directions as the corresponding \(y_e\) vary. Eliminating those coordinates leaves only the restrictions of the second term to \(Z\). On \(Z\), rows with \(x_e=0\) are zero, and all other rows form a nonzero diagonal rescaling of an oriented incidence matrix of the subgraph \((V,S)\). Its rank is \(n-c_G(S)=r_G(S)\) over **every field**, because a spanning forest supplies independent rows and each remaining cycle row is dependent. The two images lie in disjoint coordinate summands. Hence
\[
\rho(a)=m-|Z|+r_G(S). \tag{5}
\]
This argument proves the key matrix-rank step without assuming odd characteristic.

3. **Counting exactly equal-color edges.** The edge set \(Z=\{uv:d_u=d_v\}\) is automatically a graphic flat: equality is transitive along paths. Conversely, an assignment \(d\in\mathbf F_q^V\) has this exact equality set \(Z\) precisely when it gives a proper \(q\)-coloring of the contraction multigraph \(G/Z\). Therefore there are exactly \(\chi_{G/Z}(q)\) such assignments; if the contraction cannot be colored with \(q\) colors, the count is zero. For each assignment, \(x_e\) is freely chosen on every edge outside \(Z\), giving \(q^{m-|Z|}\) choices. On \(Z\), the exact nonzero support \(S\) has \((q-1)^{|S|}\) choices. Combining these counts with (5) gives equation (1) with no overcounting.

4. **Matroid invariance.** For any loopless multigraph \(H\), its chromatic polynomial obeys \(\chi_H(q)=q^{c(H)}\chi_{M(H)}(q)\), where the rightmost term is the characteristic polynomial of its cycle matroid, and loops give zero in both conventions. Since contraction of the flat \(Z\) does not change the number of graph connected components, \(c(G/Z)=c(G)\), and \(M(G/Z)=M(G)/Z\). Consequently \(q^{-c(G)}\chi_{G/Z}(q)=\chi_{M(G)/Z}(q)\). Every remaining term of (1) is a function of the ground set and rank function of \(M(G)\), establishing the asserted normalized matroid invariance. Orientation independence already follows from (5).

5. **Forests and commuting pairs.** In a forest, every edge subset is a flat, and \(r_G(S)=|S|\). Given \(Z\), the contraction \(G/Z\) is another forest with \(m-|Z|\) edges, so \(\chi_{G/Z}(q)=q^{c(G)}(q-1)^{m-|Z|}\). Substitution in (1), followed by summing independently over the \(m\) edges, gives \(q^{c(G)}(1+(q^2-1)T)^m\). The centralizer of \(a\) has cardinality \(q^{n+m-\rho(a)}\). Hence the number of ordered commuting pairs is \(\sum_a q^{n+m-\rho(a)}\), giving the probability identity stated after (2) and the forest simplification in (2).

6. **Full radical image and arboricity.** For any fixed vertex assignment \(d\) and its edge equality set \(Z\), choose every \(x_e\neq0\) on \(Z\). Then \(S=Z\), and equation (5) shows the maximal obtainable rank for this \(d\) is
\[
m-|Z|+r_G(Z)=m-(|Z|-r_G(Z)). \tag{6}
\]
The graph \((V,Z)\) is a disjoint union of the graphs induced by the color classes of \(d\). Its cycle-nullity \(|Z|-r_G(Z)\) is zero exactly when each induced color-class graph is a forest. Such a vertex assignment exists precisely when \(\operatorname{va}(G)\le q\). Because every commutator lies in the radical, rank \(m\) is equivalent to surjectivity onto the radical, proving (3). For \(K_5\) over two colors at least three vertices share a color, hence \(|Z|-r_G(Z)\ge1\); a split into classes of sizes two and three attains cycle-nullity one. Thus the exact maximum rank is nine.

## Verification

Run `python3 artifacts/verify_graph_rank.py` with the Python standard library. The checker builds commutator matrices directly in prime fields, independently enumerates exact vertex colorings and arrow support patterns, and independently evaluates the flat-sum formula. Exhaustive direct computations agree for the one-edge quiver, triangles, paths, stars, squares and the diamond graph in characteristics two and three, where computational sizes permit, and a \(K_5\) check over \(\mathbf F_2\) confirms maximum rank nine. Several cases additionally brute-force every ordered commuting pair. The script returns `VERIFY_OK`; it is a finite consistency check, **not** a proof for infinitely many graphs or prime-power fields. The proof above supplies the unrestricted theorem.

For example, for the triangle over \(\mathbf F_2\), the rank polynomial has coefficients \((2,6,32,24)\) in degrees zero through three, while for the four-vertex path over \(\mathbf F_2\) it has coefficients \((2,18,54,54)\). The star on four vertices has the identical latter distribution as the forest formula predicts.

## Relationship to prior work

Vaso's 2021 treatment of radical-square-zero bound quiver algebras gives criteria for higher cluster-tilting subcategories in terms of quivers, not distributions of ranks of inner commutators. Dutta, Basnet and Nath (2018) study commuting probabilities and centralizers in finite rings and treat several small-centralizer cases, not this graphic-matroid formula. A published finite Kronecker path-algebra result gives exact commutator fibers and centralizers for a **two-vertex** parallel-arrow family; the simple one-edge case of the present theorem is covered by that known result. Its theorem neither handles arbitrary underlying simple graphs and cycles nor implies the matroid-invariance or vertex-arboricity assertions. The graphic-matroid characteristic polynomial and graph vertex arboricity are classical; the claim here is the exact connection to the whole inner-commutator rank spectrum of radical-square-zero quiver algebras.

## Limitations

The exact formula may be exponential to evaluate directly on general graphs; no polynomial-time evaluation algorithm or complexity lower bound is asserted. Parallel arrows and loops are outside scope: parallel arrows can change the rank-one edge spaces, so the simple-graph hypothesis is substantive. The full commutator-fiber distribution at each nonzero radical element, as opposed to the rank distribution and zero fiber, is not classified. The result counts labeled algebra elements, not algebra isomorphism classes. Related generic bilinear-map or matroidal counting formulas may exist under terminology not found in the literature comparison; independent external validation remains pending.

## References

1. Laertis Vaso, “\(n\)-cluster tilting subcategories for radical square zero algebras,” arXiv:2105.05830v1, first publicly posted 12 May 2021, primary MSC 16G20. https://arxiv.org/abs/2105.05830
2. J. Dutta, D. K. Basnet and R. K. Nath, “Commuting probabilities of \(n\)-centralizer finite rings,” arXiv:1803.04111v1, first publicly posted 12 March 2018. https://arxiv.org/abs/1803.04111
3. “Commutator fibers and commuting probabilities of finite Kronecker path algebras,” public mathematical research record (2026), record suffix 75cb49b6c27d, https://github.com/published-finding corpus/2026 .
4. G. Chartrand, H. V. Kronk, and C. E. Wall, “The point-arboricity of a graph,” Israel Journal of Mathematics 6 (1968), 169–175. See also the definition summarized at https://mathworld.wolfram.com/VertexArboricity.html .
5. Standard graphic-matroid identities: cycle matroid rank, contraction, and chromatic/characteristic-polynomial relation, as in J. Oxley, *Matroid Theory*, second edition, Oxford University Press (2011).
