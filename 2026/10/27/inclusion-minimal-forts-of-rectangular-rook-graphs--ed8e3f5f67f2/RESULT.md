# Inclusion-minimal forts of rectangular rook graphs

## Finding

**Theorem.** Let \(p,q\ge2\) be arbitrary integers and let \(R_{p,q}=K_p\square K_q\). Its vertices are the \(pq\) labeled cells \((i,j)\), and cells are adjacent when they share a row or column. Identify any nonempty cell set \(F\) with an edge set \(H_F\) of the complete bipartite graph on \(p\) row vertices and \(q\) column vertices. A *fort* is a nonempty vertex set for which every exterior vertex has either zero or at least two neighbors in the set. A fort is *inclusion-minimal* when no proper nonempty subset is a fort.

All inclusion-minimal forts fall into exactly four disjoint families:

1. **Spanning star forests:** \(H_F\) spans all rows and columns, every nontrivial component is a star (a single edge counts as a star), and in **each** bipartition class either a degree-one vertex exists or **every** vertex has degree exactly two.
2. **Row-subdivision forests:** every row has degree exactly two, at least one column is isolated, and \(H_F\) is acyclic.
3. **Column-subdivision forests:** every column has degree exactly two, at least one row is isolated, and \(H_F\) is acyclic.
4. **Alternating cycles:** \(H_F\) is the edge set of one simple bipartite cycle of length \(2k\), \(2\le k\le\min(p,q)\), that does not use *both* bipartition classes completely. Equivalently, \(k<p\) or \(k<q\).

Here “spanning” means no isolated vertex on either side, and “forest” refers to the bipartite incidence graph \(H_F\), **not** the rook graph induced by \(F\). The four descriptions are disjoint, even at small orders.

Define the all-cardinality *minimal-fort polynomial*
\[
\mathcal F_{p,q}(z)=\sum_{F\text{ inclusion-minimal fort of }R_{p,q}}z^{|F|}.
\]
Let \([x^a y^b]\) denote coefficient extraction in formal power series and set
\[
\begin{aligned}
S(x,y,z)&=\exp\!\left(xyz+x(e^{zy}-1-zy)+y(e^{zx}-1-zx)\right),\\
B(x,y,z)&=\exp\!\left(x(e^{zy}-1-zy)\right),\\
C(x,y,z)&=\exp\!\left(y(e^{zx}-1-zx)\right),\\
A_{p,q}(z)&=p!q![x^p y^q]\big(S-B-C\big)\\
&\quad+\mathbf1_{q=2p}\frac{q!}{2^p}z^{2p}
+\mathbf1_{p=2q}\frac{p!}{2^q}z^{2q}.
\end{aligned}
\]
For \(v,e\ge0\), let \(U(v,e)\) be the number of simple forests with exactly \(e\) edges on a prescribed labeled \(v\)-vertex set **having at least one isolated vertex**. It is an explicit integer coefficient:
\[
U(v,e)=v![u^v t^e](1-e^{-u})
\exp\!\left(\sum_{h\ge1}\frac{h^{h-2}}{h!}u^h t^{h-1}\right),
\]
where the \(h=1\) summand is \(u\). Then the complete enumeration is
\[
\boxed{\begin{aligned}
\mathcal F_{p,q}(z)={}&A_{p,q}(z)+p!U(q,p)z^{2p}+q!U(p,q)z^{2q}\\
&+\sum_{\substack{2\le k\le\min(p,q)\\k<p\ \mathrm{or}\ k<q}}
\binom pk\binom qk\frac{k!(k-1)!}{2}z^{2k}.
\end{aligned}}
\]
All coefficients are nonnegative integers and the formula is finite at each \(p,q\). In particular, for \(2\le p\le q\),
\[
\min_{F}|F|=\min(q,4),\qquad
\max_{F}|F|=
\begin{cases}
2p,&q=p+1,\\
p+q-2,&q=p\ \text{or}\ q\ge p+2.
\end{cases}
\]
The result is a complete fort-hypergraph classification, not a formula for the number of all forts or for all zero-forcing sets.

## Assumptions and scope

All graphs are finite, simple, undirected, with \(p,q\ge2\), and the sets being enumerated are **inclusion-minimal forts** for the ordinary zero-forcing color-change rule. Empty selections are excluded. Every row and column vertex of \(H_F\) is retained, so “isolated row/column” is unambiguous. Variables in coefficient-extraction expressions are formal and may be truncated to the requested degree before calculation.

## Proof

**1. Exact external-neighborhood condition.** For each row \(i\) and column \(j\), let \(r_i\) and \(c_j\) denote the number of selected cells in that row and column. For an unselected cell \((i,j)\), its neighbors in \(F\) consist of the \(r_i\) selected cells of its row and the \(c_j\) selected cells of its column, with no overlap; thus
\[
|N_{R_{p,q}}(i,j)\cap F|=r_i+c_j.
\]
Consequently \(F\) is a fort exactly when
\[
\bigl(\text{no empty column}\ \lor\ \text{no degree-one row}\bigr)
\quad\text{and}\quad
\bigl(\text{no empty row}\ \lor\ \text{no degree-one column}\bigr).
\tag{1}
\]
Indeed an exterior cell with exactly one selected neighbor exists precisely at the intersection of a degree-one row and an empty column, or an empty row and a degree-one column.

**2. Both sides covered.** Suppose every row and column is incident to a selected cell. Then (1) holds automatically. A minimal fort must be an inclusion-minimal *bipartite edge cover*: otherwise deleting one edge while keeping every row and column covered would leave a fort. In any inclusion-minimal edge cover each selected edge has an endpoint of degree one. Therefore every component is a star; conversely each spanning star forest is a minimal edge cover.

Suppose a spanning star forest has a degree-one vertex in each side. A proper selected-edge subset cannot still cover both sides. If it covers all rows but omits a column, its rows must have degree at least two by (1), contradicting the original degree-one row (which would have to remain covered). The transposed case uses the original degree-one column. If it omits a row and a column, its non-isolated bipartite vertices would all require degree at least two by (1), and hence contain a cycle, impossible inside a forest.

If there is **no** degree-one row, each component is row-centered (all columns have degree one). For minimality, every row must have degree precisely two: a row of degree at least three permits one incident edge to be removed, leaving an empty column but all row degrees at least two, which is again a fort. Conversely, when every row has degree two, removing any edge either makes an empty column and a degree-one row or yields a subset with an empty row; no proper subset can satisfy (1), since its columns have degree at most one. The argument is symmetric if there is no degree-one column. Thus family 1 is necessary and sufficient.

**3. Exactly one side covered.** Assume all rows but not all columns are incident with \(F\). By (1), every row has degree at least two. If \(F\) is inclusion-minimal, no row may have degree three or more, since an incident edge could be deleted without creating a degree-one row. Thus all row degrees equal two. If \(H_F\) contains a bipartite cycle, that cycle alone is a fort (both its row and column degrees are two wherever nonzero), because at least one column of the original \(H_F\) is empty. Minimality forces \(F\) to be exactly that cycle. Otherwise \(H_F\) is acyclic and falls into family 2.

Conversely, an acyclic \(H_F\) with all row degrees two and at least one empty column satisfies (1). Any proper subset that remains a fort cannot still cover all rows (each initially has precisely two selected edges). It cannot cover all columns, either, since a column was already empty. It would therefore have an empty row and an empty column, forcing every non-isolated bipartite vertex to have degree at least two. Such a nonempty graph contains a cycle, contradicting acyclicity. Hence every family-2 member is minimal. The argument with rows and columns exchanged gives family 3.

**4. Both sides have isolated vertices.** By (1), every non-isolated row and column vertex of \(H_F\) has degree at least two. Consequently \(H_F\) contains a cycle, and the edge set of any one such cycle is itself a fort. Minimality forces the whole set to equal that cycle. Conversely a simple cycle which leaves at least one whole side uncovered satisfies (1). Every proper edge subset is acyclic and cannot cover an entire bipartition side in degree at least two (the original cyclic edges were necessary for that); hence no proper nonempty subset is a fort. A simple cycle covering both sides would require \(p=q=k\); its alternating perfect matching is already a proper fort, so this case must be excluded. This proves the four-way classification.

**5. Counting.** A spanning star-forest component is uniquely one of: a single edge (species weight \(xyz\)); a row-centered star with at least two column leaves (species weight \(x(e^{zy}-1-zy)\)); or a column-centered star with at least two row leaves (species weight \(y(e^{zx}-1-zx)\)). The labeled exponential formula gives \(S\). Forests with *some* degree-one vertex on both sides are counted by \(S-B-C\). An exceptional spanning star forest with no degree-one rows must have every row degree exactly two; it exists only when \(q=2p\), with \(q!/2^p\) possibilities, and the transpose contributes when \(p=2q\). This gives \(A_{p,q}(z)\).

For a family-2 fort, suppressing each row vertex (which has degree two) turns it into a distinct labeled edge between two columns. Acyclicity is precisely acyclicity of this resulting **simple** column graph: repeated column pairs would create a four-cycle in \(H_F\). Exactly \(p\) edges occur, and the graph has an isolated column. There are \(U(q,p)\) possible forests and \(p!\) assignments of the labeled rows to their edges, producing \(p!U(q,p)z^{2p}\). The forest EGF follows from Cayley's \(h^{h-2}\) labeled-tree count and deleting the singleton-free factor. The transpose gives \(q!U(p,q)z^{2q}\).

A cycle with \(k\) vertices in each bipartition class can be constructed by choosing the \(k\) rows and columns, then choosing one undirected cyclic order of alternating edges: \(k!(k-1)!/2\) arrangements. Only a cycle using all rows **and** all columns fails minimality. Summing gives the displayed polynomial.

**6. Cardinality extrema.** Assume \(2\le p\le q\). A spanning bipartite star forest covers every column, so has at least \(q\) edges. It has at least two star components (one star cannot cover two or more vertices on both sides), so has at most \(p+q-2\) edges; both bounds are attained by a suitable forest (a minimal edge cover of size \(q\) with a degree-one row, and two disjoint complementary stars respectively). The one-sided subdivision families have \(2p\) or \(2q\) edges, but the column-subdivision family cannot occur for \(p\le q\) since its forest would require \(p\ge q+2\). The row-subdivision family needs \(q\ge p+2\). Cycles have sizes \(2k\ge4\), with maximal size \(2p\) if \(q>p\), and \(2p-2\) if \(q=p\). A four-cycle is available whenever \(q\ge4\) and \(p\ge2\); the small \(q\le3\) cases attain their smaller minimum via spanning edge covers. Taking the minima and maxima gives the claimed piecewise values.

## Verification

A standalone standard-library verifier constructs the rook graph from its original adjacency definition and enumerates every nonempty cell subset of ten boards, from \(2\times2\) through \(4\times5\). It finds inclusion-minimal forts by testing the defining neighbor condition, verifies their structural membership, and independently counts the predicted polynomial by recursive labeled-star decomposition, simple-forest enumeration, and cycle counting. For all boards with at most sixteen cells it additionally checks membership of **every** subset in both directions. The ten boards contain \(1{,}156{,}934\) nonempty subsets in total. Every assertion passed. Run \(\texttt{python3 rook\_min\_fort\_verifier.py}\); exact checked outputs are stored in \(\texttt{rook\_min\_fort\_verification.txt}\). Finite tests supplement, but do not replace, the general proof.

## Relationship to prior work

Fetchie, Jacob, and Saavedra (2015, Theorem 4.3), as restated by Abara and Pelayo (2022, Theorem 3.7), already determine the **largest** cardinality of failed zero-forcing sets of rook graphs with a factor of order at least four: \(F(R_{p,q})=pq-4\). Consequently the minimum-fort size \(4\) in that range is **previously implied**, and is not a novelty claim here. Those scalar failed-set bounds do not classify every inclusion-minimal fort or determine its cardinality polynomial. Becker, Cameron, Hanely, Ong, and Previte (2024) study minimal-fort counts and product constructions, including join, corona and vertex-sum methods; they establish a general hypergraph/zero-forcing context but do not give a rectangular rook-graph four-family classification or its complete polynomial. Cameron, Hogben, Kenter, Mojallal, and Schuerger (2023; revised 2026) study fort hypergraphs and zero-forcing bounds for Cartesian products, without this exact enumeration. Brimkov, Cameron, and Grubbs (2025) construct certain minimal forts of Cartesian products, explaining only part of the general phenomenon, rather than classifying all rook-graph forts. The ordinary rook graph is the line graph of \(K_{p,q}\); findings for forts of the *underlying complete bipartite graph* are not equivalent to findings for forts of its **line graph**. The new content is the exhaustive incidence-structure classification and exact all-cardinality enumerator, not the definition of forts or the general correspondence with zero forcing.

## Limitations

The result concerns exactly two complete-graph Cartesian factors, ordinary forts, and inclusion-minimality. It does not classify all nonminimal forts, compute the zero-forcing polynomial, or assert a result for arbitrary line graphs. Literature priority cannot be certified exhaustively by database searches; a semantically equivalent unindexed result could remain undiscovered. Verification is finite plus a written proof, and independent validation has not been performed.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (public 2024-04-09), https://arxiv.org/pdf/2404.05963.
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1 (public 2023-10-27), https://arxiv.org/abs/2310.17904.
3. M. N. M. Abara and P. A. B. Pelayo, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1 (public 2022-02-10), https://arxiv.org/pdf/2202.04997, Theorem 3.7, citing K. Fetchie, B. Jacob, and D. Saavedra, *The failed zero forcing number of a graph*, Involve 8 (2015), 99–117, Theorem 4.3.
4. B. Brimkov, T. R. Cameron, and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826 (2025), https://arxiv.org/pdf/2507.10826.
