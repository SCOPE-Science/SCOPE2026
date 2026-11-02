# Frozen optima and twin double-brooms in the domination exchange graph of ladders

## Finding
Let \(L_n=P_2\square P_n\) be the ordinary two-row ladder with \(n\) columns. Its **minimum-domination token-sliding graph** \(\mathcal T_n\) has one vertex for each dominating set of size \(\gamma(L_n)\); two vertices are joined if one selected ladder vertex can be replaced by an *adjacent* ladder vertex, retaining domination and cardinality.

**Theorem.** For every integer \(k\ge4\), \(\gamma(L_{2k})=k+1\), and \(\mathcal T_{2k}\) is the disjoint union of two copies of the tree \(B_{k-1}\) and \(2k-4\) isolated vertices. Here \(B_h\) is formed from a path of \(h\) edges by attaching two new leaves to each endpoint. In particular, each nontrivial component has \(k+4\) vertices, \(k+3\) edges and diameter \(k+3\), while
\[
 |V(\mathcal T_{2k})|=4k+4,\qquad |E(\mathcal T_{2k})|=2k+6,
 \qquad c(\mathcal T_{2k})=2k-2.
\]
The complete degree distribution is \(2k-4\) vertices of degree zero, eight of degree one, \(2k-4\) of degree two and four of degree three. For odd \(n\ge5\), \(\gamma(L_n)=(n+1)/2\) and \(\mathcal T_n\) consists of two isolated vertices. The small even ladder \(L_6\) instead has two seven-vertex double-brooms and three isolates. The number \(4k+4\) of optimal sets for the even ladders is a previously tabulated count and is not the novelty claim: the structural classification of their **adjacency-constrained** exchanges is.

## Assumptions and scope
Label ladder vertices \((i,r)\) for column \(i\in\{1,\ldots,n\}\) and row \(r\in\{0,1\}\). Edges are rungs \((i,0)(i,1)\) and horizontal edges \((i,r)(i+1,r)\). A dominating set covers every vertex by its closed neighborhood. Its cardinality is the number of selected vertices, not the number of columns occupied. A legal exchange replaces \((i,r)\) with a neighboring unselected vertex and preserves minimum domination; arbitrary token jumps are *not* edges. All graphs and counts here are ordinary finite simple graphs.

Represent a selection as a word of length \(n\) over \(\{0,U,D,X\}\), where \(0\) selects no row, \(U\) selects row zero, \(D\) selects row one and \(X\) selects both. A nonzero column dominates both vertices in its column. An empty column is dominated exactly when its adjacent nonempty columns, interpreted as row masks, jointly contain both rows. Endpoint adjacency outside the ladder is empty. This criterion is necessary and sufficient.

## Proof
**1. Minimum size and the zero-gap obstruction.** An internal selected vertex dominates at most four vertices, and an endpoint vertex at most three. For odd \(n=2k+1\), \(2n>4k\), so every dominating set has at least \(k+1\) vertices. For even \(n=2k\), a dominating set of \(k\) vertices would have to cover the \(4k\) vertices with no overlaps and no selected endpoint vertex. Both vertices of the first column would then require selected neighbors in the second column, forcing the symbol \(X\) there, which already overlaps both its own selected closed neighborhoods. Hence \(\gamma(L_{2k})\ge k+1\). The explicit words constructed below attain these lower bounds.

For a dominating set \(S\), define the nonnegative overlap sum
\[
 \Omega(S)=\sum_{v\in V(L_n)}\bigl(|N[v]\cap S|-1\bigr)=4|S|-e(S)-2n,
\]
where \(e(S)\) is the number of selected endpoint vertices. Every \(X\) column contributes at least two units to \(\Omega\), since both of its selected vertices dominate both column vertices. An occurrence \(00\) in the column word forces \(X00X\): each of the two empty columns must be dominated from its unique available nonempty outside neighbor, hence both outside neighbors contain both rows. For odd minimum sets \(\Omega\le2\), so \(00\) is impossible. For even minimum sets \(\Omega\le4\); if \(00\) occurs, its two forced \(X\) columns exhaust all overlap, and \(e(S)=0\). These two \(X\) columns, say at \(a\) and \(a+3\), cover all of the six consecutive columns \(a-1,\ldots,a+4\), with every covered vertex receiving at least one dominating incidence. Any additional selected vertex is forbidden from touching these columns, or the overlap budget would be exceeded. If column \(a-2\) exists, neither row of it can be selected (that would also cover column \(a-1\)), and covering both rows of \(a-2\) from column \(a-3\) requires a third \(X\), impossible; the right-hand argument is symmetric. Thus the only even minimum word containing \(00\) has \(n=6\) and is \(0X00X0\). In particular, **all minimum words for even \(n\ge8\) and odd \(n\ge5\) have no consecutive zero columns**.

**2. Exhaustive word classification.** Let \(d\) be the number of \(X\) columns, \(m\) the number of occupied columns and \(z\) the number of empty columns. A minimum set has \(m+d=|S|\), so for even \(n=2k\) we have \(m=k+1-d\) and \(z=k-1+d\). The no-\(00\) constraint implies \(z\le m+1\), whence \(d\le1\).

If \(d=0\), the endpoint columns must be occupied. There are \(k+1\) singletons and \(k-1\) empty columns in the \(k\) gaps between the singletons. Exactly one gap has no intervening empty column; call its index \(j\in\{1,\ldots,k\}\). All other gaps contain one empty column, across which rows must alternate. Thus, for \(r,s\in\{0,1\}\), the word \(A(r,j,s)\) consists of \(k+1\) singleton selections indexed \(\ell=1,\ldots,k+1\), with
\[
 c_\ell=\begin{cases}2\ell-1,&\ell\le j,\\2\ell-2,&\ell\ge j+1,\end{cases}
 \qquad
 \rho_\ell=\begin{cases}r\oplus((\ell-1)\bmod2),&\ell\le j,\\s\oplus((\ell-j-1)\bmod2),&\ell\ge j+1.\end{cases}
\]
The symbol \(\oplus\) is addition modulo two. No row condition is imposed across the unique consecutive-singleton gap. These are \(4k\) distinct minimum words.

If \(d=1\), there are \(k\) empty and \(k\) occupied columns, so exactly one endpoint is empty, all internal gaps contain one zero, and the neighbor of that empty endpoint is the unique \(X\). The four possibilities are \(L_s\) and \(R_s\), \(s\in\{0,1\}\). For \(L_s\), column one is empty, column two is \(X\), and columns \(4,6,\ldots,2k\) contain alternating singletons beginning with row \(s\) at column four. For \(R_s\), column \(2k\) is empty, column \(2k-1\) is \(X\), and columns \(2k-3,2k-5,\ldots,1\) contain alternating singletons beginning with row \(s\) at column \(2k-3\). Every displayed word dominates and has \(k+1\) selected vertices. This proves there are exactly \(4k+4\) minima for even \(n\ge8\).

For odd \(n=2k+1\ge5\), the same argument permits at most one \(X\). With one \(X\), there would be \(k+1\) zeros and \(k\) occupied columns, which requires *both* endpoints to be empty. These would force distinct \(X\)'s at columns two and \(n-1\), a contradiction. With no \(X\), all \(k\) zeros are internal and all gaps contain one zero. The occupied columns are \(1,3,\ldots,2k+1\), and rows alternate. There are exactly two such minima, neither reachable from the other by one adjacent exchange.

**3. Exact sliding adjacencies.** For even \(n=2k\ge8\), abbreviate
\[
 q_r(j)=r\oplus(j\bmod2),\qquad P_{r,j}=A(r,j,q_r(j)).
\]
A direct comparison of the selected column positions and row bits in the formulas above yields *all* legal edges (undirected):
\[
 P_{r,j}P_{r,j+1}\quad(1\le j<k),
\]
\[
 P_{r,1}L_r,\quad P_{r,1}A(1-r,1,q_r(1)),
\]
\[
 P_{r,k}R_{q_r(k)},\quad P_{r,k}A(r,k,1-q_r(k)),
\]
for each \(r\in\{0,1\}\), with no other edges.

For completeness, the comparison exhausts the possible types. Two \(A\) words with different gap locations can differ at only one column position precisely when the locations are consecutive; checking the unchanged selected row bits forces \(s=q_r(j)\) and the succeeding suffix bit \(q_r(j+1)\). At a fixed gap, a one-token rung exchange can change the first row parameter only if \(j=1\), or the second only if \(j=k\); the displayed endpoint edges are the resulting and only possibilities. An \(L_s\) word has its lone double selection at column two, so an adjacent exchange to an \(A\) word necessarily puts the shifted token in column one, forcing \(j=1\) and \(A(s,1,1-s)=P_{s,1}\). The \(R_s\) case is the reflection, forcing \(j=k\) and the indicated row. Different endpoint-double words cannot be one adjacent exchange apart when \(k\ge4\). The checker verifies this exhaustive pair rule independently for a range of parameters, but the classification here follows from the explicit symbolic comparison, not the checked range.

For fixed \(r\), the vertices \(P_{r,1},\ldots,P_{r,k}\) form a path of \(k-1\) edges. Each endpoint has precisely two additional leaves, giving \(B_{k-1}\). The two values of \(r\) give disjoint components; there are \(2k+8\) nonisolated words and \((4k+4)-(2k+8)=2k-4\) isolates. The vertex, edge, component, degree and diameter formulas follow. For \(n=6\), the preceding exceptional word \(0X00X0\) accounts for the additional isolated vertex; the remaining words yield two seven-vertex trees, as also verified directly.

## Verification
The package includes `verify_direct.py`, which independently constructs closed neighborhoods, enumerates every subset of the necessary cardinalities for \(5\le n\le12\), and builds the exact legal sliding graph; it checks the claimed counts, component sizes and degree distributions. The separate `verify_templates.py` generates all symbolic words and independently compares every actual legal edge against the predicted edge list for \(4\le k\le26\), including each claimed degree and isolate count. Executed with ordinary Python 3, both programs complete with `DIRECT_EXHAUSTIVE_LADDER_PASS` and `SYMBOLIC_TEMPLATE_AND_EXCHANGE_PASS`. Finite checks are corroboration: only the preceding proofs establish all \(k\).

## Relationship to prior work
Fricke, Hedetniemi, Hedetniemi and Hutson (2011) introduced the adjacent-swap \(\gamma\)-graph model used here, but its general definition alone does not give this infinite ladder classification. Haas and Seyffarth's 2012 study uses addition/deletion of a single vertex and permits larger intermediate dominating sets; that is a different reconfiguration graph. Lakshmanan and Vijayakumar (2010), and the subsequent modified-\(\gamma\)-graph literature, also study exchanges without necessarily requiring the two swapped vertices to be adjacent; consequently their edge relations are not this theorem's edge relation. Published tabulations of the number of minimum dominating sets of ladders already contain the bare vertex count and are not claimed new.

Bhatt and Bhatt's 2024 article *Certain findings on the gamma graph of some graphs* treats, in its ladder theorem, the gamma graph of the **middle graph** of the ladder, rather than the gamma graph of the original ladder. Their separate 2024 *Some Results on Gamma Graphs* includes Cartesian products of paths and cycles in its abstract but was inaccessible in full; it is a residual priority risk even though the stated adjacency is unrestricted one-vertex exchange. The present result concerns the complete graph of **adjacency-constrained** optimal exchanges, not just enumeration of optimal sets or unconstrained token jumping.

## Limitations
The theorem concerns width-two ordinary ladders and minimum dominating sets under *adjacent* one-token slides; it makes no claim about wider grids, token jumping or addition/deletion models. The computational checks cannot certify the infinite statement by themselves. A historical equivalent under another terminology, particularly the inaccessible 2011 foundational article's unexamined full text and the inaccessible 2024 Cartesian-product article, remains a priority risk. Independent validation has not been performed.

## References
- G. H. Fricke, S. M. Hedetniemi, S. T. Hedetniemi, K. R. Hutson, *\(\gamma\)-Graphs of Graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 517–531. DOI: `10.7151/dmgt.1562`.
- S. A. Lakshmanan and A. Vijayakumar, *The gamma graph of a graph*, AKCE International Journal of Graphs and Combinatorics 7 (2010), 53–59.
- R. Haas and K. Seyffarth, *The \(k\)-Dominating Graph*, arXiv:`1209.5138v1`, publicly posted 2012-09-24; later Graphs and Combinatorics 30 (2014), 609–617.
- A. Suzuki, A. E. Mouawad, N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:`1401.5714v1` (2014).
- V. Anusuya and R. Kala, *Modified \(\gamma\) Graph of Some Grid Graphs*, Palestine Journal of Mathematics 9 (2020), 691–697.
- K. Bhatt and T. Bhatt, *Certain findings on the gamma graph of some graphs*, The Scientific Temper 15 (2024), 15–17, DOI: `10.58414/SCIENTIFICTEMPER.2024.15.spl-2.03`.
- K. Bhatt, *Some Results on Gamma Graphs*, Vidhyayana 10 (2024), DOI: `10.58213/8jee9p96` (full text inaccessible).
