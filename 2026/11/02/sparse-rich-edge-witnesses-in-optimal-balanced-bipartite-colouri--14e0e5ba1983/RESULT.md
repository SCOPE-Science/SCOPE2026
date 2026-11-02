# Sparse rich-edge witnesses in optimal balanced bipartite colourings

## Finding
For a proper edge-colouring \(\varphi\) of a finite simple graph, call an edge **rich** when its distinct adjacent edges all receive different colours. The colouring is **rich-neighbor** when every edge having an adjacent edge is adjacent to a rich edge *other than itself*. Let \(R_\varphi\) be the set of rich edges. For an edge-containing graph \(G\), let \(\chi'_{\mathrm{rn}}(G)\) denote the least number of colours in a rich-neighbor colouring, and define the **optimal rich-edge support number**
\[
\rho(G)=\min\{|R_\varphi|:\varphi\text{ is a rich-neighbor colouring using exactly }\chi'_{\mathrm{rn}}(G)\text{ colours}\}.
\]

**Theorem.** For every integer \(n\ge2\),
\[
\boxed{\rho(K_{n,n})=\begin{cases}4,&n=2\text{ or }3,\\n,&n\ge4.\end{cases}}
\]
For each \(n\ge4\) and each split \(2\le d\le n-2\), there is an optimal \((2n-1)\)-colouring whose **entire** rich-edge graph consists of two disjoint-centre stars with \(d\) and \(n-d\) edges, respectively, their leaf sets partitioning one bipartition class. Thus the lower bound of \(n\) simultaneous local witnesses is attained with the optimal number of colours. The size-three exception cannot attain that sparsity under the optimal five-colour palette.

## Assumptions and scope
Graphs are finite, simple, undirected and nonempty. The graph \(K_{n,n}\) has two labelled bipartition classes with \(n\) vertices apiece. Edge colours are names, so relabelling colours does not change richness. Two distinct edges are adjacent exactly when they share a vertex; a rich edge does **not** count as its own rich neighbor. The minimum in \(\rho\) ranges over colourings using precisely the chromatic-index optimum for the rich-neighbor rule, not over arbitrary larger palettes. For \(n\ge3\), this optimum is \(2n-1\), established by Kong (2026); for \(n=2\) it is four. An elementary palette lower bound and the constructions below recover these values in the cases needed here.

## Proof
**1. Universal lower bound.** If \(R\) is the rich-edge set of any rich-neighbor colouring of \(K_{n,n}\), the endpoints incident with \(R\) constitute a vertex cover: an edge whose endpoints touch no rich edge has no adjacent rich edge. The complement of a vertex cover in a complete bipartite graph cannot contain one vertex from each side. Therefore every vertex in at least one entire bipartition class is incident with \(R\). Each rich edge meets exactly one vertex of that class, so \(|R|\ge n\).

**2. Construction for all \(n\ge4\).** Fix \(d\) with \(2\le d\le n-2\). Write the first bipartition class as \(\{a,b\}\sqcup U\), with \(|U|=n-2\), and the second as \(P\sqcup Q\), with \(|P|=d\) and \(|Q|=n-d\). Take three disjoint palettes: \(X\) and \(Y\) with \(|X|=|Y|=n-1\), and a singleton \(\{z\}\). Thus there are exactly \(2n-1\) available colours.

On the rectangle \((\{b\}\cup U)\times P\), use \(X\) so that every column contains every member of \(X\) exactly once and every row uses pairwise distinct colours. This is possible by the cyclic Latin-rectangle formula \(x_{(r+j)\bmod(n-1)}\), where \(r=0,\ldots,n-2\) indexes the rows and \(j=0,\ldots,d-1\) indexes the columns. Independently, on \((\{a\}\cup U)\times Q\), use \(Y\) by the analogous cyclic Latin rectangle. Hence the row of \(a\) already uses \(n-d\) distinct members of \(Y\), and the row of \(b\) already uses \(d\) distinct members of \(X\).

Colour the remaining \(d\) edges \(aP\) using **all** unused members of \(Y\) and the additional colour \(z\). Colour the remaining \(n-d\) edges \(bQ\) using **all** unused members of \(X\) and that same colour \(z\). Every row and column has distinct colours: the row of \(a\) uses exactly \(Y\cup\{z\}\), the row of \(b\) uses exactly \(X\cup\{z\}\), and each row in \(U\) uses distinct colours in the disjoint palettes \(X\) and \(Y\). Every column of \(P\) uses all \(X\) and one new colour from \(Y\cup\{z\}\); every column of \(Q\) uses all \(Y\) and one from \(X\cup\{z\}\). The two occurrences of \(z\) are in different rows and different columns.

A properly coloured edge joining vertices with palettes \(S,T\) is rich precisely when \(S\cap T\) is the singleton containing the colour of that edge: any other common colour occurs on two distinct edges adjacent to it. By the displayed palettes, every edge in \(aP\cup bQ\) is rich. Conversely, for an edge \(up\) with \(u\ne a\) and \(p\in P\), the row at \(u\) contains \(d\ge2\) different \(X\)-colours, all belonging to the column palette at \(p\), so \(up\) is not rich. Similarly every \(uq\) with \(u\ne b\) and \(q\in Q\) is not rich, since the intersection contains \(n-d\ge2\) different \(Y\)-colours. **The complete rich-edge set is exactly \(aP\cup bQ\), of size \(n\).** These two stars each have at least two edges and jointly touch every vertex of \(P\sqcup Q\). Each edge, including each rich edge, therefore has a *different* rich edge as a neighbor.

Every rich edge of \(K_{n,n}\) has \(2n-2\) adjacent edges, whose colours must be distinct and also differ from its own colour under a proper colouring. Consequently every rich-neighbor colouring needs at least \(2n-1\) colours. Our construction uses exactly that many, so it is optimal. Combining with Step 1 proves \(\rho(K_{n,n})=n\) for all \(n\ge4\).

**3. The two small orders.** For \(n=2\), \(K_{2,2}\) is a four-cycle. In a three-colour proper edge-colouring its only rich edges are the two opposite edges, which have no rich neighbors. Four colours are necessary and sufficient (assign all four edges distinct colours). In any optimal four-colour assignment to four edges, all four are distinct and consequently all four edges are rich. Thus \(\rho(K_{2,2})=4\).

For \(n=3\), the five-colour proper edge-colouring given by the matrix
\[
\begin{pmatrix}0&1&2\\1&3&4\\2&4&3\end{pmatrix}
\]
has exactly four rich edges, at matrix positions \((1,2),(1,3),(2,1),(3,1)\) in one-based indexing. They form two adjacent two-edge stars and constitute an open edge-dominating set. Any rich edge of \(K_{3,3}\) forces at least five colours, so this colouring is optimal.

It remains to exclude only three rich edges. At least three are necessary by Step 1. In any optimal \((2n-1)\)-colouring of \(K_{n,n}\), the rich-edge graph contains no (not necessarily induced) three-edge path. Indeed, suppose \(u_1v_1,u_2v_1,u_2v_2\) are all rich, with distinct \(u_i\) on one side and distinct \(v_i\) on the other. Let \(C\) be the \((2n-1)\)-colour palette, \(S\) the \(n\)-colour palette at \(v_1\), and \(T=C\setminus S\). Put \(\alpha=\varphi(u_1v_1)\), \(\beta=\varphi(u_2v_1)\), \(\gamma=\varphi(u_2v_2)\). Richness implies
\[
\Phi(u_1)=T\cup\{\alpha\},\quad \Phi(u_2)=T\cup\{\beta\},\quad
\Phi(v_2)=(S\setminus\{\beta\})\cup\{\gamma\}.
\]
Here \(\gamma\in T\) and \(\alpha\ne\beta\). The edge \(u_1v_2\) would need a colour in \(\Phi(u_1)\cap\Phi(v_2)=\{\alpha,\gamma\}\), but \(\alpha\) is already used at \(u_1\) and \(\gamma\) is already used at \(v_2\), a contradiction. Therefore the rich-edge graph has no three-edge path. It has no cycle of length three since it is bipartite. Since a rich edge must have another rich edge adjacent to it, a three-edge rich subgraph must therefore be a single three-edge star.

Such a star cannot have all three edges rich with five colours. If its center is a vertex \(v\), the three other-side vertices \(u_i\) are its rich leaves. Their palettes off their edges to \(v\) must lie in the complementary palette \(C\setminus\Phi(v)\), containing just two colours. Hence the remaining \(K_{3,2}\) would be properly edge-coloured using two colours, impossible because it has a vertex of degree three. The same argument applies if the star is centered in the other bipartition class. So at least four rich edges are necessary, and the displayed colouring attains four. This completes all cases. \(\square\)

## Verification
The independent edge-neighborhood checker `verify.py` constructs the actual coloured adjacency matrices without using the palette-intersection lemma as a test. It examines every row and column for properness, computes rich edges directly by collecting the colours on **distinct adjacent edges**, and checks the open rich-neighbor condition for each edge. It verifies every split \(2\le d\le n-2\) and each \(4\le n\le11\), plus the two small orders and unbalanced control cases. All 83 construction cases passed. As a separate small-order check, it enumerates the normalized proper five-colour matrices of \(K_{3,3}\) and finds minimum rich-edge count four among the valid rich-neighbor colourings (36 normalized witnesses). It also confirms that the three-colour four-cycle example fails the open-neighbor rule. Run `python verify.py` using Python's standard library; no network or other dependency is required.

These finite tests are diagnostics. The infinite theorem follows from the explicit Latin rectangles, palette intersections, elementary vertex-cover bound, and the small-order obstruction proof above.

## Relationship to prior work
J. Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:2610.21036v1 (first publicly posted October 15, 2026), Theorem 1.2 and Section 3.1, already prove \(\chi'_{\mathrm{rn}}(K_{n,n})=2n-1\) for \(n\ge3\), with the size-two exception. **The minimum palette size is prior work and is not claimed new.** Kong's balanced-case construction explicitly certifies \(2n-2\) rich edges (two stars of size \(n-1\)), whereas the theorem here certifies just \(n\), meets the universal edge-support lower bound for all \(n\ge4\), and proves the sharp size-three exception. An edge-dominating-set calculation alone does not imply realizability at the optimal palette size. The general linear bound in Kashima–Petruševski–Sedlar–Škrekovski (arXiv:2610.16446v1) concerns colour count rather than the minimum size of the rich-edge witness set. Terminological aliases include total edge domination in the line graph and sparse local-colour certificates; neither by itself determines the joint colour/support optimum.

## Limitations
This proves the *number* of rich edges minimized among *optimal-palette* colourings, not a classification or enumeration of all such colourings and not a formula for arbitrary bipartite graphs. While the motivating source's complete relevant section was inspected, historical priority across all possible equivalent terminology has not been independently certified. A prior exact edge-domination result does not by itself settle this palette-constrained question. No independent mathematical audit has been performed.

## References
1. J. Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:2610.21036v1, first public 2026-10-15, https://arxiv.org/html/2610.21036v1 (especially Theorem 1.2, Lemma 2.1, Section 3.1).
2. M. Kashima, M. Petruševski, J. Sedlar, and R. Škrekovski, *The rich-neighbor chromatic index is linear in the maximum degree*, arXiv:2610.16446v1, first public 2026-10-12, https://arxiv.org/abs/2610.16446.
3. L. Chen, Y. Tan, and X. Zhou, *On the Rich-Neighbor Edge-Colorings of Subcubic Graphs*, Graphs and Combinatorics 41, 89 (2025), https://doi.org/10.1007/s00373-025-02949-y.
