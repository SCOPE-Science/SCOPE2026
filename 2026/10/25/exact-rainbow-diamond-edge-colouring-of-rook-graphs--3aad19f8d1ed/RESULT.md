# Exact rainbow-diamond edge-colouring of rook graphs

## Finding

For all integers \(2\le m\le n\), the D-chromatic index of the rook graph \(R_{m,n}=K_m\square K_n\) is
\[
\chi'_D(R_{m,n})=
\begin{cases}
2,&(m,n)=(2,2),\\
3,&(m,n)=(2,3),\\
5,&(m,n)=(3,3),\\
\binom{n}{2},&n\ge4.
\end{cases}
\]
In particular, for every \(n\ge4\), the rainbow-diamond edge-colouring lower bound from a single \(K_n\) row clique is attained simultaneously across all intersecting row and column cliques. A colouring with exactly \(\binom n2\) named colours is given below and can be constructed using a perfect matching in a regular bipartite disjointness graph.

## Assumptions and scope

All graphs are finite, simple, and undirected. A *diamond* is a not-necessarily-induced subgraph isomorphic to \(K_4\) with one edge deleted. An edge-colouring is *D-valid* when adjacent edges have different colours and all five edges of each diamond have different colours. The minimum possible palette size is \(\chi'_D\). In \(R_{m,n}\), vertices are cells \((i,a)\), with \(i\in\{0,\ldots,m-1\}\), \(a\in\{0,\ldots,n-1\}\); two distinct cells are adjacent precisely when they share a row or a column.

For the construction, coordinate arithmetic is in the cyclic group \(\mathbb Z/n\mathbb Z\). A colour is an unordered two-element subset of that group, not an ordered pair. The colouring is not asserted unique, and no number of optimal colourings is asserted.

## Proof

**Diamond localization.** Every triangle in a rook graph is contained entirely in a row clique or a column clique. Every edge belongs to exactly one such maximal line clique, because its endpoints share exactly one coordinate. A diamond consists of two triangles sharing an edge; consequently all of its vertices and edges lie in one row clique or one column clique. Conversely, in a clique of order at least four, every pair of distinct edges must receive different colours in any D-valid colouring: incident edges differ by properness; two disjoint edges belong to a common diamond formed on their four endpoints. Thus a D-valid colouring of a rook graph is exactly a proper edge-colouring whose restriction to every line clique of size at least four gives every clique edge a distinct colour.

**Lower bound.** When \(n\ge4\), each row is a \(K_n\), and all its \(\binom n2\) edges have different colours. Hence \(\chi'_D(R_{m,n})\ge\binom n2\).

**Disjoint-pair bijection.** Let \(\mathcal P=\binom{\mathbb Z/n\mathbb Z}{2}\). Construct a bipartite graph with a left and a right copy of \(\mathcal P\), joining \(F\) on the left to \(T\) on the right when \(F\cap T=\varnothing\). Every vertex has degree \(\binom{n-2}{2}>0\) when \(n\ge4\). Since this is a regular bipartite graph with equal part sizes, Hall's marriage theorem gives a perfect matching. It defines a bijection
\[
\psi:\mathcal P\longrightarrow\mathcal P,
\qquad F\cap\psi(F)=\varnothing\quad\text{for every }F\in\mathcal P.
\]

**Colour the square rook graph.** First take \(R_{n,n}\), indexing both coordinates by \(\mathbb Z/n\mathbb Z\), and use the \(\binom n2\) colours in \(\mathcal P\). For a horizontal edge in row \(i\) connecting \((i,a)\) and \((i,b)\), assign
\[
 c_H(i;\{a,b\})=\{a+i,b+i\}.
\]
For a vertical edge in column \(a\) connecting \((i,a)\) and \((j,a)\), let \(F=\psi^{-1}(\{i,j\})\) and assign
\[
 c_V(a;\{i,j\})=a+F=\{a+x:x\in F\}.
\]
The row-edge colours are distinct inside each row because translation is a bijection on \(\mathcal P\). The column-edge colours are distinct inside each column because the composite \(F\mapsto\psi(F)\mapsto a+F\) is bijective on \(\mathcal P\).

At a cell \((i,a)\), every incident horizontal-edge colour contains \(a+i\). For an incident vertical edge of colour \(a+F\), its endpoint row index \(i\) belongs to \(\psi(F)\). By disjointness, \(i\notin F\), so \(a+i\notin a+F\). Thus no horizontal-edge colour equals a vertical-edge colour at the same cell. All adjacent edges therefore receive different colours, and every row or column clique is rainbow. Diamond localization now proves this is a D-valid colouring of \(R_{n,n}\).

For \(2\le m\le n\), restrict the colouring to the induced subgraph on the first \(m\) rows. This is \(R_{m,n}\); its colouring remains D-valid and still uses all \(\binom n2\) colours on each complete row. Together with the lower bound this proves the asserted formula for \(n\ge4\).

**Small orders.** If \(n\le3\), all row and column cliques have at most three vertices, and diamond localization implies the graph has no diamonds. Thus D-valid means merely proper edge-colouring. The graph \(R_{2,2}\) is a four-cycle, with edge chromatic index two. The graph \(R_{2,3}\) is a triangular prism; colour the two triangle edges joining columns \(a,b\) by \(a+b\pmod3\), and colour the rung in column \(a\) by \(2a\pmod3\). This proper colouring uses three colours, matching its maximum degree.

Finally, \(R_{3,3}\) is four-regular with nine vertices and eighteen edges. Four colours would have to partition its edges into four matchings, each of size at most four, which is impossible since \(18>16\). A five-colour proper assignment is given by the following two arrays. Rows of \(H\) are the three horizontal cliques and rows of \(V\) are the three vertical cliques; in both arrays the columns list the edge-pairs \(\{0,1\},\{0,2\},\{1,2\}\):
\[
H=\begin{pmatrix}0&3&1\\2&3&0\\3&4&2\end{pmatrix},
\qquad
V=\begin{pmatrix}1&2&0\\3&4&1\\2&0&1\end{pmatrix}.
\]
Each cell meets four edges of pairwise different colours, as is also checked in the standalone verifier. The D-chromatic index is therefore five. This finishes all cases.

## Verification

Run `python3 verify.py` with a standard Python 3 installation; it requires no third-party packages. The program constructs a disjoint-pair perfect matching from scratch, makes the stated colouring, checks the properness and opposite-diamond-edge constraints independently, and additionally inspects every four-vertex subset for diamond subgraphs in the smaller cases. It verifies all \(33\) parameter pairs \(4\le n\le9\), \(2\le m\le n\), plus the three small cases. The recorded output is in `verify_output.txt`. Direct checks across finitely many sizes corroborate the construction; Hall's theorem and the preceding argument prove the unrestricted claim.

## Relationship to prior work

Runze Wang introduced D-colouring and proved general degree-dependent bounds, including the conjectured universal upper bound for maximum degree at most five [1]. Hu, Kong and Wang studied D-colouring of planar graphs and formulated the general clique/booksize lower bounds [2]. Neither inspected result gives the exact rook-graph index or the cyclic-label/disjoint-pair construction here. A published exact result for *complete multipartite graphs* concerns a different class: \(R_{m,n}\) with \(m\ge2,n\ge3\) has an induced four-vertex path and hence is not complete multipartite. The present proof reaches the clique lower bound sharply for every rook graph with at least four columns.

## Limitations

The result concerns two-factor Cartesian products of complete graphs; it does not assert a result for higher-dimensional Hamming graphs or count the number of optimal D-colourings. The finite checker is not a substitute for the infinite proof. Relevant indexed literature was searched, but possible equivalent formulations outside the inspected material remain a publication-priority uncertainty. Independent mathematical validation has not been performed.

## References

1. Runze Wang, *Proper edge coloring with rainbow diamonds*, arXiv:2606.06831, first submitted 2026-06-05. https://arxiv.org/abs/2606.06831
2. Xiaoxue Hu, Jiangxu Kong and Yiqiang Wang, *D-coloring of planar graphs*, arXiv:2607.14837, first submitted 2026-07-16. https://arxiv.org/abs/2607.14837
3. Hall's marriage theorem (standard regular-bipartite perfect-matching corollary).
